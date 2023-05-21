from django.contrib import admin
from .models import categorias,productos,categoria_Intermedia
# Register your models here.

admin.site.register(categorias)
admin.site.register(productos)
admin.site.register(categoria_Intermedia)
