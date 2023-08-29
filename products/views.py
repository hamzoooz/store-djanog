from django.shortcuts import render
from products.models import Producs
# Create your views here.
def index(request):
    # carousel_images = CaruselImage.objects.all()[0:5]
    # return render(request, 'inc/slider.html' , {"carousel_images":carousel_images})


    # user, rating, create_at, update_at, status, trending, meta_tilte, meta_keyword, meta_description, available, title, url, category, published_data, number_of_views, small_descrption, quantity, original_price, selling_price, tags, abrov)user, rating, create_at, update_at, status, trending, meta_tilte, meta_keyword, meta_description, available, title, url, category, published_data, number_of_views, small_descrption, quantity, original_price, selling_price, tags, abrov)
    trending_books = Producs.objects.filter( available='publised', trending=True)[0:10]
    recent_books = Producs.objects.filter( available='publised').order_by('-create_at')[0:10]
    random_books = Producs.objects.filter(available='publised').order_by('?')[0:10]
 
    return render(request, 'products\index.html', {
    "trending_books":trending_books,
    "recent_books":recent_books,
    "random_books":random_books,
    })
    
    
def producud_detail(request, id):
    books = Producs.objects.get( available='publised' , id=id)
    return render(request, 'products\product_detail.html' , { "books":books} )