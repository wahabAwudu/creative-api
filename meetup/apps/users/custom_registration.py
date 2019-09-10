# from rest_auth.registration.serializers import RegisterSerializer
# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email
# from allauth.utils import get_username_max_length
# from allauth.account import app_settings as allauth_settings
# from rest_framework import serializers

# from meetup.apps.wallet.models import Wallet
# from meetup.apps.users.models import User, OwnerProfile
# from meetup.apps.vehicles.models import VehicleSettings


# class CustomRegistrationSerializer(RegisterSerializer):
#     username = serializers.CharField(
#         max_length=get_username_max_length(),
#         min_length=allauth_settings.USERNAME_MIN_LENGTH,
#         required=True
#     )
#     email = serializers.EmailField(required=True, write_only=True)
#     # phone = serializers.CharField(write_only=True, required=True)
#     password1 = serializers.CharField(write_only=True, required=True)
#     # password2 = serializers.CharField(write_only=True, required=True)

#     def get_cleaned_data(self):
#         return {
#             'username': self.validated_data.get('username', ''),
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             # 'phone': self.validated_data.get('phone', ''),
#         }

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         self.custom_signup(request, user)
#         setup_user_email(request, user, [])
#         # save new account
#         user.is_account_owner = True
#         user.save()

#         # new owner profile
#         owner_profile = OwnerProfile(owner=user, use_global_vehicle_settings=True)
#         owner_profile.save()

#         # new vehicle settings
#         new_settings = VehicleSettings(user=user, refresh_rate=0, speed_limit=0)
#         new_settings.save()
    
#         # new wallet
#         user_wallet = Wallet(user=user, current_balance=0.00)
#         user_wallet.save()

#         return user
