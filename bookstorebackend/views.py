from .models import Products
from .serializers import serialize_products
from django.http import JsonResponse

def product_list(request):
    products = Products.objects.all()  # Fetch all products
    product_data = [
        {
            'id': product.id,
            'name': product.name,
            'overview': product.overview,
            'long_description': product.long_description,
            'price': product.price,
            'poster': product.poster,
            'image_local': product.image_local.url if product.image_local else None,
            'rating': product.rating,
            'in_stock': product.in_stock,
            'size': product.size,
            'best_seller': product.best_seller,
        }
        for product in products
    ]
    return JsonResponse(product_data, safe=False)
