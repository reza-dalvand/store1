from django.db.models import Q
from django.views.generic import ListView, TemplateView
from rest_framework.permissions import AllowAny
from products_module.models import Product, ProductCategory, ProductBrand


class ProductsListView(ListView):
    permission_classes = [AllowAny]
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    paginate_by = 1

    def get_queryset(self):
        slug = self.request.GET.get('slug')
        brand = self.request.GET.get('brand')
        min_price = self.request.GET.get('min-price')
        max_price = self.request.GET.get('max-price')
        sort_by = self.request.GET.get('sort-by')
        search = self.request.GET.get('search')
        queryset = Product.objects.filter(is_published=True, soft_deleted=False)

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
        if sort_by:
            context['sort_by'] = sort_by
        return context


class CategoriesComponent(TemplateView):
    template_name = 'components/products_list/categories_component.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesComponent, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
