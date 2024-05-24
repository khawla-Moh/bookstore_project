from rest_framework import generics

from .models import Book,Category,Author
from .import serializers

#==================Book=========================
class BooklistAPI(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookListSerializers

class BookDetailAPI(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookListSerializers
    
#==================Category=====================
class CategorylistAPI(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.CategoryListSerializers

class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.CategoryDetailSerializers
        

#=======================Author================
class AuthorlistAPI(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.AuthorListSerializers

class AuthorDetailAPI(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.AuthorDetailSerializers       