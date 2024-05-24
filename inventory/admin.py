from django.contrib import admin

from .models import Book,Category,Author
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display=['title','Categories','author','price']
    list_filter=['title','author','price']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

class AuthorAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(Book,BookAdmin)    
admin.site.register(Category,CategoryAdmin)    
admin.site.register(Author,AuthorAdmin)    
