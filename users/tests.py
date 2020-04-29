from django.test import TestCase
from .models import User, OwnerProfile, ManagerProfile

class UserTest(TestCase):
    def setUp(self):
        new_user = User(username="arab_tester", email="metesteremail@gmail.com")
        new_user.set_password('metester50')
        new_user.save()

        owner_profile = OwnerProfile(owner=new_user, use_global_vehicle_settings=True)
        owner_profile.save()
        
        manager = User(username="arab_manager", email="arabmanager@gmail.com")
        manager.set_password("manager2020")
        manager.save()

        manager_profile = ManagerProfile(owner=new_user, manager=manager)
        manager_profile.save()

    def test_user(self):
        user = User.objects.get(username="arab_tester")
        self.assertEqual(user.username, "arab_tester")

        owner_profile = OwnerProfile.objects.get(owner=user)
        self.assertEqual(owner_profile.use_global_vehicle_settings, True)

        manager_profile = ManagerProfile.objects.get(owner=user)
        self.assertEqual(manager_profile.manager.username, "arab_manager")

