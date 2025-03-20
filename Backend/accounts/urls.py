from django.urls import path
from .views import *

urlpatterns =[
    path('accounts/create', create_account, name='create_account'),
    path('accounts/login', login_account, name='login_account'),
    path('accounts/authorization_check', authorization_check, name='coba_authentication'),
    path('accounts/logout', logout_account, name='logout_account'),
]