from django.urls import path
from .views import add_book , book_list ,  book_detail

urlpatterns = [
    path('', book_list , name='book_list'),
    path('add_book/', add_book , name='add-book'),
    path('book_detail/<int:pk>/', book_detail, name='book-detail')
]