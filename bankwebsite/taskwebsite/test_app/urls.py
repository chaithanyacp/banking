from django.urls import path
from . import views
app_name='test_app'
urlpatterns = [
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('customer_form',views.customer_form, name='customer_form'),
]
