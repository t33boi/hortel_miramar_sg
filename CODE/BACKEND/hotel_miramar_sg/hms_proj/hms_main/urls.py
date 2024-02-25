from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    
    path('rooms/',views.room,name='rooms'),
    path('book/<int:pk>/',views.book_room,name='book_room'),
    path('checkout/', views.check_out,name='check_out'),
    
    path('checkout/delete/<int:pk>',views.check_out_delete,name='check_out_delete'),
]