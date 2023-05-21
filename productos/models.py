from django.db import models

class categorias(models.Model):
    nomCategoria = models.CharField(max_length=100)#imagen = models.ImageField(upload_to="cat_imgs/")#Modifica
    imagen = models.URLField(blank=False, null=False)
    
class categoria_Intermedia(models.Model):
    nomCategoria_Intermedia = models.CharField(max_length=100)
    foto = models.URLField(blank=False, null=False)
    categoria = models.ForeignKey(categorias, null=True, on_delete=models.SET_NULL)

class productos(models.Model):
    nomProducto = models.CharField(max_length=100)
    nomMarca = models.CharField(max_length=100)
    intprecio = models.DecimalField(max_digits=6, decimal_places=0) # foto = models.ImageField(upload_to="cat_imgs/") Opcion 1 de imagen
    foto = models.URLField(blank=False, null=False)
    categoria_Intermedia = models.ForeignKey(categoria_Intermedia, null=True, on_delete=models.SET_NULL)