import folium

from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class MapView(APIView):
    @staticmethod
    def get(request):
        map = folium.Map(location=[24.1724, 72.4346], zoom_start=12)

        # Add a marker to the map
        folium.Marker(
            location=[24.1724, 72.4346],
            popup="Palanpur, Gujarat, India",
            icon=folium.Icon(color="green"),
        ).add_to(map)

        # Convert the map to HTML
        map_html = map.get_root().render()

        return render(request, "map.html", {"map_html": map_html})
