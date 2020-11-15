from django.contrib import admin
from .models import Place, Review

# Register your models here.


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('place', 'writer', 'comment', 'stars',)
