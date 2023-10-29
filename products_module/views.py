from django.db.models import Q
from django.views.generic import ListView, TemplateView
from rest_framework.permissions import AllowAny
from products_module.models import Product, ProductCategory


class ProductsListView(ListView):
    permission_classes = [AllowAny]
    context_object_name = 'products'
    template_name = 'products/products_list.html'
    paginate_by = 1

    def get_queryset(self):
        slug = self.request.GET.get('slug')
        if slug:
            return Product.objects.filter(is_published=True, soft_deleted=False,
                                          category__slug=slug)
        return Product.objects.filter(is_published=True, soft_deleted=False)


class CategoriesComponent(TemplateView):
    template_name = 'components/products_list/categories_component.html'

    def get_context_data(self, **kwargs):
        context = super(CategoriesComponent, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context
