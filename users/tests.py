from django.test import TestCase
from .models import User

class UserTest(TestCase):
    def setUp(self):
        new_user = User(username="arab_tester", email="metesteremail@gmail.com")
        new_user.set_password('metester50')
        new_user.save()

    def test_user(self):
        user = User.objects.get(username="arab_tester")
        self.assertEqual(user.username, "arab_tester")

