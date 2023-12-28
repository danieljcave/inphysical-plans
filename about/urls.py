from django.urls import path
from . import views
from .views import ShowProfilePageView, EditProfile, DeleteProfile


urlpatterns = [
    path('<int:pk>/profile/', ShowProfilePageView.as_view(),
         name="show_profile_page"),
    path('<int:pk>/edit_profile_page/', EditProfile.as_view(),
         name='edit_profile_page'),
    path('<int:pk>/delete_profile/', DeleteProfile.as_view(),
         name='delete_profile'),
]
