from django.urls import path
from world_map import views as world_map_views

urlpatterns = [path("", world_map_views.MapView.as_view(), name="map-view")]
