from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo

# Create your tests here.

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='Test Todo', body='This is a test todo')

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.body, "This is a test todo")
        self.assertEqual(str(self.todo), "Test Todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Test Todo")