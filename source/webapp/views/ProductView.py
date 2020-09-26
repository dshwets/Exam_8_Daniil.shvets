from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ProductForm
from webapp.models import Product


class Products_view(ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'


class Watch_product_view(DetailView):
    template_name = 'products/watch_product.html'
    model = Product

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     if not self.object.is_active:
    #         raise Http404
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)


class Create_product_view(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_product.html'
    # permission_required = 'webapp.add_project'

    def get_success_url(self):
        return reverse('watch_product', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update_product.html'
    # permission_required = 'webapp.change_project'

    def get_success_url(self):
        return reverse('watch_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('index_view')
    permission_required = 'webapp.delete_project'

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = super().get_success_url()
    #     print(self.object.is_active)
    #     self.object.is_active = False
    #     self.object.save()
    #     return HttpResponseRedirect(success_url)