from django.db.models import Q
from django.views.generic import ListView, TemplateView
from rest_framework.permissions import AllowAny
from products_module.models import Product, ProductCategory


class ProductsListView(ListView):
    permission_classes = [AllowAny]
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    queryset = Product.objects.filter(Q(is_published=True) & Q(soft_deleted=False))
    # django pagination
    paginate_by = 1


class CategoriesComponent(TemplateView):
    template_name = 'components/products_list/categories_component.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesComponent, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
