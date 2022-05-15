from housingApp.models import reserved
from .views import productsViewset
from rest_framework import routers

reserve = routers.DefaultRouter()
reserve.register("reserved", productsViewset,
basename='reserved'),