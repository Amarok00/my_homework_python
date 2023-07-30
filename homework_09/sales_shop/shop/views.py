from typing import Any, Dict, Optional

from celery.result import AsyncResult
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)
from django.db.models import Q
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import CategoryForm
from .models import Category, Order, Product
from .tasks import notify_order_saved


class HelloView(View):
    def get(self,request: HttpRequest)->HttpResponse:
        return HttpResponse("<h1>Hello View</h1>")

class CategoriesListView(ListView):
    # model = Category
    queryset = Category.objects.filter(~Q(archived=True)).all()


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    # fields = "name" , "description"
    # success_url = reverse
    success_url = reverse_lazy("shop:categories")


class CategoryUpdateView(UpdateView):
    # template_name = ...
    template_name_suffix = "_update_form"
    model = Category
    form_class = CategoryForm
    # success_url =reverse_lazy("shop:category",{})
    # slug_url_kwarg = ""
    # field = "description"

    def get_success_url(self) -> str:
        return reverse("shop:category", kwargs={"pk": self.object.pk})


class CategoryDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required ="shop.delete_category"
    # model = Category
    success_url = reverse_lazy("shop:categories")
    queryset = Category.objects.filter(~Q(archived=True)).all()

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        # return HttpResponseRedirect(success_url)
        return redirect(success_url)


class ShopIndexView(TemplateView):
    template_name = "shop/index.html"


class ProductsView(ListView):
    template_name = "shop/products.html"
    queryset = (
        Product.objects.filter(~Q(status=Product.Status.ARCHIVED))
        .order_by("id")
        .select_related("category")
        .defer(
            "description",
            "created_at",
            "update_at",
            "category__description",
        )
        .all()
    )
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product


class OrdersListView(UserPassesTestMixin,ListView):
    def test_func(self) :
        return self.request.user.is_staff
    template_name = "shop/orders.html"
    context_object_name = "orders"
    queryset = (
        Order.objects.order_by("id")
        .select_related("user", "payment_details")
        .prefetch_related("products")
        .all()
    )


class CategoriesWithProductsTree(LoginRequiredMixin, TemplateView):
    template_name = "shop/categories_with_products_tree.html"

    extra_context = {
        "categories": Category.objects.order_by("id").prefetch_related("products").all()
    }
    # def get_context_data(self, **kwargs: Any):
    #     context = super().get_context_data(**kwargs)
    #     categories = Category.objects.order_by("id").prefetch_related("products").all()
    #     context.update(categories=categories)
    #     return context


@login_required
def get_task_info(request: HttpRequest, task_id: str) -> HttpResponse:
    task_result: AsyncResult = notify_order_saved.AsyncResult(task_id)
    return JsonResponse(
        {
            "task_id": task_result.task_id,
            "status": task_result.status,
            "name": task_result.name,
            # "backend":str(task_result.backend)
        }
    )
