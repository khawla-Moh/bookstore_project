import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
import random
from inventory.models import Book,Category,Author






def ADD_Book(n):
    fake=Faker()
    #category=Category.objects.all()
    author=Author.objects.all()
    category=[Category.objects.all() for _ in range(10)]
    #author=[Author.objects.all() for _ in range(10)]
    images=['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg','07.jpg','08.jpg','09.jpg','10.jpg']
    for _ in range(n):
           books=[]
           book= Book.objects.create(
            
            title=fake.name(),
            price=round(random.uniform(20.99,99.99),2),
            image=f"inventory/{images[random.randint(0,9)]}",
            description=fake.text(max_nb_chars=500),
            publisher_year=fake.date(),
            stock=fake.random_int(1,1000),
            author=author[random.randint(0,len(author)-1)]
            
           )
           #book.author.set(fake.random_choices (author,fake.random_int(1,3)))
           book.categories.set(fake.random_choices (category,fake.random_int(1,3)))
           books.append(book)
            
             
            #categories=category[random.randint(0,len(category)-1)]
           
    print("add book")
    return books

""" 
            title=fake.title(),
            price=fake.price,
            image=f"inventory/{images[random.randint(0,9)]}",
            publisher_year=fake.publisher_year(),
            
            tags=fake.tags(),
            description=fake.description(max_nb_chars=500),
            author=author[random.randint(0,len(author)-1)],
            categories=category[random.randint(0,len(category)-1)]
"""

print(ADD_Book(100))



  
#add categories
#def add_category(n):
#    fake=Faker()
#    categories=Category.objects.all()

#    for _ in range(n):
#        Category.objects.create(
#            name=fake.name()
#        )

#    print('add categories sucessfully')    


#print(add_category(20)) 


#add author
#def add_author(n):
#    fake=Faker()
#    authors=Author.objects.all()

#    for _ in range(n):
#        Author.objects.create(
#            name=fake.name()
#        )

#    print('add categories sucessfully')    


#print(add_author(50))  
 
