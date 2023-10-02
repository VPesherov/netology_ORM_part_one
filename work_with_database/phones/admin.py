from django.contrib import admin
from .models import Phone

# Register your models here.
@admin.register(Phone) # указывает для какого класса наша админка
class PhoneAdmin(admin.ModelAdmin): # обязательно наследуемся от admin.ModelAdmin
    list_display = ['id', 'name', 'image', 'price', 'release_date', 'lte_exists', 'slug']
    prepopulated_fields = {"slug": ("name",)}
