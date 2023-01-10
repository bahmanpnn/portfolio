from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view(), name='home_page_dark'),
    path('light', views.IndexPageLight.as_view(), name='home_page_light'),
]
