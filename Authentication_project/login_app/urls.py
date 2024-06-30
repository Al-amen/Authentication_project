
from django.urls import path
from login_app import views

app_name = 'login_app'

urlpatterns = [
    path('index/',views.index,name = "index"),
    path('register/',views.register, name='register'),
]
