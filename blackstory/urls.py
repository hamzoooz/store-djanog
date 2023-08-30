from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('ckeditor/', include('ckeditor.urls')),
    
    
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    
    
    

    
    # main apps
    # path('', include('cart.urls')),
    # path('', include('core.urls')),
    # path('', include('books.urls')),
    # path('', include('users.urls')),
    # path('', include('carts.urls')),
    # path('', include('search.urls')),
    # path('', include('wishlist.urls')),
    # path('', include('order.urls')),
    # path('', include('tools.urls')),
    # path('', include('_manage.urls')),
    # path('', include('comments.urls')),
    # path('', include('qoutes.urls')),    
    # path('', include('rating.urls')),
    # path('', include('follow.urls')),
    # path('', include('chatapp.urls')),
    # path('', include('adds.urls')),
    # path('', include('apis.urls')),
    
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
    
# urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'core.views.error_404_view'