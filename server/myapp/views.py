from rest_framework.views import APIView
from rest_framework.response import Response

class PlantList(APIView):
    def get(self, request):
        # Fake data (replace with real data from DB later)
        fake_plants = [
            {"id": 1, "name": "alo", "price": "10.00"},
            {"id": 2, "name": "Tulip", "price": "5.50"},
            {"id": 3, "name": "Sunflower", "price": "7.20"}
        ]
        return Response(fake_plants)
