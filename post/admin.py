from django.contrib import admin
from .models import Place, Review

# Register your models here.


@admin.register(Place)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class UserAdmin(admin.ModelAdmin):
    pass
