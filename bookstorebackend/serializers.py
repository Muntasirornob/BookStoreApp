from .models import Products
from typing import Iterable, List, Dict, Any

def serialize_products(products: Iterable[Products]) -> List[Dict[str, Any]]:
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'overview': product.overview,
            'long_description': product.long_description,
            'price': product.price,
            'poster': product.poster,
            'image_local': product.image_local,
            'rating': product.rating,
            'in_stock': product.in_stock,
            'size': product.size,
            'best_seller': product.best_seller,
        })
    return data
