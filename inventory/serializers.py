from rest_framework import serializers
from .models import Book,Category,Author


#=========================BOOK=======================
class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class BookDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'        



#========================CATEGORY======================
class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'        



#==========================AUTHOR======================
class AuthorListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class AuthorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'                        
