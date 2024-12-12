from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products

@csrf_exempt
def product_list(request):
    """
    API to fetch all products or filter them based on the 'q' query parameter.
    """
    if request.method == "GET":
        query = request.GET.get("q", "")  # Get the search query
        if query:
            results = Products.objects.filter(name__icontains=query)
        else:
            results = Products.objects.all()

        data = [
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
            for product in results
        ]

        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Invalid HTTP method"}, status=400)
