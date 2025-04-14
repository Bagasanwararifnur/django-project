from django.urls import path
from .views import *

urlpatterns =[
    path('accounts/create', create_account, name='create_account'),
    path('accounts/login', login_account, name='login_account'),
    path('accounts/authorization_check', authorization_check, name='coba_authentication'),
    path('accounts/email_test', send_email_test, name='email_test'),
    path('accounts/change_password', change_password, name='change_password'),
    path('accounts/forgot_password',forgot_password,name='forgot_password'),
    path('accounts/reset_password', change_password_forgot_password, name='reset_password'),
    path('accounts/logout', logout_account, name='logout_account'),
    path('accounts/email_page', email_page, name='email_page'),
    path('accounts/template_email', template_email, name='template_email')
]