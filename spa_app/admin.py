from django.contrib import admin
from .models import FoodStore

class FoodStoreAdmin(admin.ModelAdmin):
	list_display = ['title', 'quantity', 'distance', 'active']
	list_editable = ['active']
admin.site.register(FoodStore, FoodStoreAdmin)
