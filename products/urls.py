from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name="index" ),
    path('book/<int:id>', views.producud_detail , name="producud_detail" ),
]
