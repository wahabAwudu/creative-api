from django.test import TestCase
from .utils import generate_key
from .models import Key

class KeyTestCase(TestCase):
    key = None
    def setUp(self):
        new_key = generate_key()
        key = Key.objects.create(text=new_key, used=False)
        self.key = new_key

    def test_models(self):
        key = Key.objects.get(text=self.key)
        self.assertEqual(key.text, self.key)