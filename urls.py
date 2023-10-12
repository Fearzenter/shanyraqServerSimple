from django.urls import path

from shServ.views import home, SlaveAPIView, GuardianAPIView, GuardianCompanyAPIView, registration, authorization, \
    RegisterFormView, LoginUser, logout_user

urlpatterns = [
    path('', home, name='home'),
    path('registration/', RegisterFormView.as_view(), name='registration'),
    path('authorization/', LoginUser.as_view(), name='authorization'),
    path('logout/', logout_user, name='logout'),
    path('api/v1/slavelist', SlaveAPIView.as_view(), name='slavelist'),
    path('api/v1/guardianlist', GuardianAPIView.as_view(), name='guardianlist'),
    path('api/v1/guardiancompanylist', GuardianCompanyAPIView.as_view(), name='guardiancompanylist'),
]