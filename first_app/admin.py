from tkinter import Image

from django.contrib import admin
from first_app.models import Topic, Product, Category,Fruit
class FruitAdmin(admin.ModelAdmin):
    fields = ['title', 'image']
    list_display = ['name','title', 'image']
    list_filter = ['name']
    search_fields = ['name',]
    list_editable = ['title']
# Register your models here.
admin.site.register(Topic)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Fruit,FruitAdmin)