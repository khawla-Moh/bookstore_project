from rest_framework import generics,filters
from rest_framework.pagination import PageNumberPagination
from .models import Book,Category,Author
from .import serializers
from django_filters.rest_framework import DjangoFilterBackend








#==================Category=====================
class CategorylistAPI(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.CategoryListSerializers

class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=serializers.CategoryDetailSerializers
        

#=======================Author================
class AuthorlistAPI(generics.ListAPIView):
    queryset=Author.objects.all()
    serializer_class=serializers.AuthorListSerializers

class AuthorDetailAPI(generics.RetrieveAPIView):
    queryset=Author.objects.all()
    serializer_class=serializers.AuthorDetailSerializers       











#==================Book=========================
class BooklistAPI(generics.ListAPIView):
    queryset=Book.objects.all()
    serializer_class=serializers.BookListSerializers
    filter_backends =[DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields ={
        
        'price': ["in", "exact"], # note the 'in' field
        'categories': ["exact"],
        'author': ["exact"],
        
        'stock':["exact"],
    }
    ordering_fields = ['title','price','stock']  
    pagination_class=PageNumberPagination
   
#=============================================
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

