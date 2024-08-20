from django.shortcuts import render
from rest_framework import viewsets
from .models import Food
from .serializers import FoodSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


from django.http import HttpResponse,JsonResponse
import requests
def hello_world(request):
    return HttpResponse("")

# views.py
app_id = 'a65cb04a'
app_key = 'b9637cd791eb7f7449555024969506d8	—'

def get_food_data(request, food):
    url = f"https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={app_key}&ingr={food}"
    response = requests.get(url)
    data = response.json()
    
    if "hints" not in data:
        return JsonResponse({"error": "No data found for {}".format(food)})
    
    food_nutrients = data["parsed"][0]["food"]["nutrients"]
    return JsonResponse(food_nutrients)
