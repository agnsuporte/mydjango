from django.contrib import admin
from .models import Category, Product, Variations


class VariationsInLine(admin.TabularInline):
    model = Variations
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationsInLine]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Variations)
