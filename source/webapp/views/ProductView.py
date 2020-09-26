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

    def get_context_data(self, **kwargs):
        kwargs['reviews'] = self.object.reviews.all()
        if not self.request.user.groups.filter(name='Moderators'):
            kwargs['reviews'] = kwargs['reviews'].filter(status=True)
        average = 0
        if kwargs['reviews']:
            for review in self.object.reviews.all():
                average += review.mark
            average = average / self.object.reviews.count()
        kwargs['avg_rating'] = round(average, 1)
        return super().get_context_data(**kwargs)


class Create_product_view(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create_product.html'
    permission_required = 'webapp.add_product'


    def get_success_url(self):
        return reverse('watch_product', kwargs={'pk': self.object.pk})


class ProductUpdateView(PermissionRequiredMixin ,UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update_product.html'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('watch_product', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    success_url = reverse_lazy('index_view')
    permission_required = 'webapp.delete_product'
