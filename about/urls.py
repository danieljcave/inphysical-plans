from django.urls import path
from . import views


urlpatterns = [
    path('about/profile/', views.ProfileView, name="profile"),

]
