from rest_framework import serializers
from .models import Book,Category,Author












#==========================AUTHOR======================
class AuthorListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class AuthorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'                        






#=========================BOOK=======================
class BookListSerializers(serializers.ModelSerializer):
    author=AuthorListSerializers()
    author=author.fields['name']
    categories=serializers.StringRelatedField(many=True)
    
    class Meta:
        model=Book
        fields='__all__'

class BookDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'        

#====create====
class BookSerializers(serializers.ModelSerializer):
    
    categories = serializers.SlugRelatedField(
        many=True, 
        queryset=Category.objects.all(),
        slug_field='name'
    )
    class Meta:
        model = Book
        fields = ['id', 
                  'title ', 'categories',
                  'publisher_year','author',
                  'update_date','price', 
                  'description', 'stock']



#========================CATEGORY======================
class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'


class CategoryDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'        
