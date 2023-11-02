from django.db.models import Q
from django.views.generic import ListView, TemplateView, DetailView
from rest_framework.permissions import AllowAny
from products_module.models import Product, ProductCategory, ProductBrand, ProductGallery


class ProductsListView(ListView):
    permission_classes = [AllowAny]
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    paginate_by = 1

    # model = Product

    def get_queryset(self):
        slug = self.request.GET.get('slug')
        brand = self.request.GET.get('brand')
        min_price = self.request.GET.get('min-price')
        max_price = self.request.GET.get('max-price')
        sort_by = self.request.GET.get('sort-by')
        search = self.request.GET.get('search')
        queryset = Product.objects.select_related('category', 'brand').filter(is_published=True, soft_deleted=False)

        if search:
            queryset = queryset.filter(Q(category__name__icontains=search) |
                                       Q(brand__name__icontains=search) |
                                       Q(name__icontains=search))

        if slug or brand:
            queryset = queryset.filter(Q(brand__slug__exact=brand) | Q(category__slug__exact=slug))
        if max_price or min_price:
            queryset = queryset.filter(price__lte=int(max_price.split(' ')[0]), price__gte=int(min_price.split(' ')[0]))
        match sort_by:
            case 'new':
                return queryset.order_by('-created_at')
            case 'cheep':
                return queryset.order_by('price')
            case 'expensive':
                return queryset.order_by('-price')

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        sort_by = self.request.GET.get('sort-by')
        context['brands'] = ProductBrand.objects.all()
        context['categories'] = ProductCategory.objects.select_related('parent').all()
        if sort_by:
            context['sort_by'] = sort_by
        return context


class ProductsDetailView(DetailView):
    permission_classes = [AllowAny]
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(ProductsDetailView, self).get_context_data(**kwargs)
        category = self.object.category
        context['related_products'] = category.products_category.exclude(id=self.kwargs.get('pk'))
        context['products_galleries'] = ProductGallery.objects.select_related('product').filter(
            product_id=self.object.id)
        return context
