from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView 


urlpatterns = [
    path('', views.home, name='home'),
    path('contacto', views.contacto, name='contacto'),
    path('galeria', views.galeria, name='galeria'),


    # estos sson los temples para ver el formulario en la pagina de termomarket se llama asi
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-producto/', views.listar_productos, name='listar_producto'),

    # resive un <id> para poder modificar el producto con el id selecionado
    path('modificar-producto/<id>/',
         views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/',
         views.eliminar_producto, name='eliminar_producto'),
    path('registro',
         views.registro, name='registro'),

    path('agregar-al-carrito/',
          views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/',
          views.ver_carrito, name='ver_carrito'),
    path('comprar/',
          views.procesar_compra, name='procesar_compra'),
    path('actualizar-carrito/',
          views.actualizar_carrito, name='actualizar_carrito'),
    path('eliminar-del-carrito/',
          views.eliminar_del_carrito, name='eliminar_del_carrito'),

    path('logout/', LogoutView.as_view(), name='logout'),
]
