from .models import Category, Product


def category_links(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def product_links(request):
    products = Product.objects.all()
    return dict(products=products)