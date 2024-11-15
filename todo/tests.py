from django.test import TestCase

# Create your tests here.
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='Test Todo', body='This is a test todo')

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'Test Todo')
        self.assertEqual(self.todo.body, "This is a test todo")
        self.assertEqual(str(self.todo), "Test Todo")