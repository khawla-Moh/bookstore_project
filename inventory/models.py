from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Book(models.Model):

    title=models.CharField(max_length=150)
    price=models.FloatField()
    image=models.ImageField(upload_to='book')
    publisher_year=models.DateTimeField()
    update_date=models.DateField(auto_now_add=True)
    tags=TaggableManager()
    stock = models.PositiveIntegerField(default=0)
    description=models.TextField(max_length=700)
    #stock=models.
    author=models.ForeignKey('Author',related_name='book_auhtor',on_delete=models.CASCADE)
    #author=models.ManyToManyField('Author')
    categories=models.ManyToManyField('Category')
    slug=models.SlugField(blank=True,null=True,unique=True)
    
    
    def Categories(self):
        return ','.join([c.name for c in self.categories.all()] )
    
    """   def Authors(self):
        return ','.join([a.name for a in self.author.all()] )
    """

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


    def __str__(self):
        return self.title



class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Author(models.Model):
    name=models.CharField(max_length=20)
    bio=models.TextField(null=True,blank=True)
  

    def __str__(self):
        return self.name 
