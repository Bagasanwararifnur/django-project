from django.urls import path
from .views import *

urlpatterns =[
    path('accounts/create', create_account, name='create_account'),
    path('accounts/login', login_account, name='login_account'),
    path('accounts/coba_authentication', coba_authentication, name='coba_authentication'), 
]