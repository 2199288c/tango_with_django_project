import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    #Create list of dictionaries containing pages we want
    #to add into each category
    #Then create dict of dict for categories

    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "views":666 ,},
        {"title":"How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views":123 ,},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "views":10,}]

    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01",
         "views": 499,},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/",
         "views":321 ,},
        {"title":"How to Tango with Django",
         "url":"htp://www.tangowithdjango.com/",
         "views":19 ,}]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev",
         "views":27 ,},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "views":21 ,}]

    cats = {"Python": {"pages": python_pages, "views":128, "likes":64},
            "Django": {"pages": django_pages, "views":64, "likes":32},
            "Other Frameworks": {"pages": other_pages, "views":32, "likes":16}}

#If you want to add more categories or pages add them to dicts above
#
#The code below goes through cats dict then adds each category and then
#adds all the associated pages for that category

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

#print out the categories we have added
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.views=views
    c.save()
    return c

#Start exec here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    
