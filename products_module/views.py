from django.db.models import Q
from django.views.generic import ListView, TemplateView
from rest_framework.permissions import AllowAny
from products_module.models import Product, ProductCategory, ProductBrand


class ProductsListView(ListView):
    permission_classes = [AllowAny]
    queryset = Product.objects.filter(is_published=True, soft_deleted=False)
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        slug = self.request.GET.get('slug')
        brand = self.request.GET.get('brand')
        min_price = self.request.GET.get('min-price')
        max_price = self.request.GET.get('max-price')
        print(min_price, max_price, 'maxxxxxx')
        context['brands'] = ProductBrand.objects.all()

        '''filter with query parameters'''
        if slug or brand:
            context['products'] = Product.objects.filter(Q(brand__slug__exact=brand) |
                                                         Q(category__slug__exact=slug),
                                                         is_published=True,
                                                         soft_deleted=False)
        elif max_price or min_price:
            context['products'] = Product.objects.filter(price__lte=max_price.split(' ')[0],
                                                         price__gte=min_price.split(' ')[0],
                                                         is_published=True,
                                                         soft_deleted=False)
        return context


class CategoriesComponent(TemplateView):
    template_name = 'components/products_list/categories_component.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesComponent, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
