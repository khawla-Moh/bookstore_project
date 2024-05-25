from rest_framework import generics

from .models import Book,Category,Author
from .import serializers







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











#==================Book=========================
class BooklistAPI(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookListSerializers

class BookDetailAPI(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookListSerializers

#======================ADD BOOK(CREATE)=============
class BookCreateAPI(generics.CreateAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookSerializers
#======================Retrive Book===============
class BooKUpdateAPI(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookDetailSerializers

#==============Delete Book======================
class BooKDeleteAPI(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookDetailSerializers   

