from http import HTTPStatus
from typing import Type

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.test import TestCase
from django.urls import reverse

UserModel: Type[AbstractUser] = get_user_model()


class GetTaskInfoTestCase(TestCase):
    def setUp(self) -> None:
        self.username = "user_testing"
        self.password = "supersecretpassword!23A"
        self.user: AbstractUser = UserModel.objects.create_user(
            username=self.username,
            password=self.password,
        )
        print("created user", self.user)

    def test_anon_user_no_access(self):
        url = reverse("shop:get-order-task", kwargs={"task_id": "123"})
        response = self.client.get(url)
        # self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse("site_auth:login") + f"?next={url}")

    def test_get_task_info_pending(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        task_id = "42"
        url = reverse("shop:get-order-task", kwargs={"task_id": task_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertJSONEqual(
            response.content,
            {
                "task_id": task_id,
                "status": "PENDING",
                "name": None,
            },
        )
