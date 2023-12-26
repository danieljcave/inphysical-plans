from django.urls import path
from . import views
from .views import ShowProfilePageView


urlpatterns = [
    path('<int:pk>/profile/', ShowProfilePageView.as_view(),
         name="show_profile_page"),

]
