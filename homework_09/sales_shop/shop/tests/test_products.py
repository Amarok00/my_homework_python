from http import HTTPStatus
from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.test import TestCase
from django.urls import reverse

from ..models import Product

UserModel: Type[AbstractUser] = get_user_model()


class ProductListViewTestCase(TestCase):
    fixtures = ["categories-fixture.json", "product-fixture.json"]

    def test_ok(self):
        url = reverse("shop:products")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "shop/products.html")
        self.assertEquals(response.status_code, HTTPStatus.OK)
        products_qs = (
            Product.objects.filter(~Q(status=Product.Status.ARCHIVED))
            .order_by("id")
            .only("id")
            .all()
        )
        self.assertQuerysetEqual(
            qs=products_qs,
            values=(p.pk for p in response.context["products"]),
            transform=lambda p: p.pk,
        )
