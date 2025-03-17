from django.urls import path
from .views import PlantList

urlpatterns = [
    path('api/plants/', PlantList.as_view(), name='plant-list'),  # Use .as_view() to call the class-based view
]
