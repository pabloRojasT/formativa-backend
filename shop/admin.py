from django.contrib import admin

# Register your models here.
from .models import producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'fecha_creacion', 'fecha_actualizacion')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('fecha_creacion', 'fecha_actualizacion')

admin.site.register(producto, ProductoAdmin)

