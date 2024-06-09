from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.todo = Todo.objects.create(
            title="First todo",
            body="A body of text here"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First todo")

    def test_api_listview(self):
        resp = self.client.get(reverse("todo_list"))
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(resp, self.todo)

    def test_api_detailview(self):
        resp = self.client.get(reverse(
            "todo_detail",
            kwargs={"pk": self.todo.id},
        ), format='json')

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(resp, "First todo")