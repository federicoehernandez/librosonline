from django.contrib import admin
from vistaprevia.models import Producto
from vistaprevia.models import Categoria


# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    fields = ["fecha_publicacion", "producto", "imagen", "categoria"]


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
