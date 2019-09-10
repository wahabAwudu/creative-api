from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from allauth.account.views import ConfirmEmailView

# import from generals apps
from meetup.apps.users.views import (
    UserModelViewSet,
    null_view,
    VerifyEmailView,
)
from meetup.apps.meetups.views import MeetupModelViewSet, QuestionModelViewSet

router = routers.DefaultRouter()
router.register('users', UserModelViewSet, base_name='users')
router.register('meetups', MeetupModelViewSet, base_name='meetups')
router.register('questions', QuestionModelViewSet, base_name='questions')

# admin endpoints
admin_router = routers.DefaultRouter()
admin_router.register('users', UserModelViewSet, base_name='admin_users')

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^docs/', include('rest_framework_docs.urls')),

    # App Specific url & namespaces
    url(r'^api/v1/', include(router.urls, namespace='api')),
    url(r'^api/v1/admin/', include(admin_router.urls, namespace='admin_api')),

    # Authentication Setup urls
    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/rest-auth/registration/token-auth/', obtain_jwt_token),
    url(r'^api/v1/rest-auth/registration/refresh-token/', refresh_jwt_token),

    # custom auth urls
    url(r'^api/v1/rest-auth/registration/account-email-verification-sent/', null_view, name='account_email_verification_sent'),
    url(r'^verify-email/(?P<key>\d+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
    url(r'^api/v1/rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', null_view, name='password_reset_confirm'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
