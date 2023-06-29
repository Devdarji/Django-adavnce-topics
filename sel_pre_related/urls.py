from django.urls import path
from sel_pre_related import views

urlpatterns = [path("", views.HomeView.as_view(), name="home-view")]
