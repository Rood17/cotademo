from django.urls import path
from django.conf.urls import url
from . import views

from dal import autocomplete
from .views import LinkedDataView
from .models import Category, Book

from django.views import generic
from .forms import BookForm


urlpatterns = [
    # Default Apps
    path('d_mapa/', views.Mapa, name="Mapa"),
    path('lista/', views.Lista, name="Lista"),
    path('constelaciones/', views.Nodos, name='Nodos'),

    
    # Resultados Apps
    path('resultados_constelaciones/', views.resultadosNodos, name="rNodos"),
    path('resultados_lista/', views.resultadosLista, name="rLista"),
    path('mapa/', views.resultadosMapa, name="rMapa"),


    # Fail
    path('sin_resultados/', views.sin_resultados, name='sinResultados'),

    # Pág relaciones
    path('category/<int:category_id>/', views.category, name="category" ),
    path('resultados_constelaciones/category/<int:category_id>/', views.category, name="category" ),
    path('resultados_mapa/category/<int:category_id>/', views.category, name="category" ),
    path('mapa/category/<int:category_id>/', views.category, name="category" ),
    path('constelaciones/category/<int:category_id>/', views.category, name="category" ),
    
    # Pág Categorias de estudio
    path('mapa/categoria_estudio/<int:cate_id>/', views.categoria_estudio, name="categoria_estudio" ),
    path('resultados_mapa/categoria_estudio/<int:cate_id>/', views.categoria_estudio, name="categoria_estudio" ),
    path('constelaciones/categoria_estudio/<int:cate_id>/', views.categoria_estudio, name="categoria_estudio" ),
    path('resultados_constelaciones/categoria_estudio/<int:cate_id>/', views.categoria_estudio, name="categoria_estudio" ),


    # Modals
    path('mapa/info_libro/<int:book_id>/', views.info_libro, name="info_libro" ),
    path('resultados_mapa/info_libro/<int:book_id>/', views.info_libro, name="info_libro" ),
    path('constelaciones/info_libro/<int:book_id>/', views.info_libro, name="info_libro" ),
    path('resultados_constelaciones/info_libro/<int:book_id>/', views.info_libro, name="info_libro" ),

    # User-Info
    path('user_info', views.user_info, name="user_info"),
    path('ruser_info', views.ruser_info, name="ruser_info"),


    # prueba autocomplete
    path('api/get_auto/', views.get_auto, name="get_auto"),
    # Autocomplete Nodos
    path('api/get_auto_nodos', views.get_auto_nodos, name="get_auto_nodos"),
    # Autocomplete Mapa y Lista
    path('api/get_auto_myl/', views.get_auto_myl, name="get_auto_myl"),
    
    # Autocomplete Admin
    url(
        '^linked_data/$',
        LinkedDataView.as_view(
            model=Category, 
            create_field=''
        ),
        name='linked_data_rf'
    ),

    # MANY2MANY
    url(
        'categorias-autocomplete/$',
        autocomplete.Select2QuerySetView.as_view(
            model=Category,
            create_field='',
        ),
        name='categorias-autocomplete',
    ),
]