from .models import Products
from .serializers import serialize_products
from django.http import JsonResponse

def product_list(request):
    products = Products.objects.all()  # Get all products from the database
    return JsonResponse(serialize_products(products), safe=False)  # Serialize and return as JSON
