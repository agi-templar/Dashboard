from django.http import JsonResponse

from dashboardapp.models import Restaurant
from dashboardapp.serializers import RestaurantSerializer

# Return all the restaurants in the databse in JSON format
def customer_get_restaurants(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"restaurants": restaurants})
