from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('zarejestruj', views.signup, name='zarej'),
    path('zaloguj', CustomLoginView.as_view(), name='login'),
    path('wyloguj', LogoutView.as_view(), name='logout'),

]

