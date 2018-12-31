from django.core import serializers
from django.core.serializers import serialize
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from itertools import chain
from dal import autocomplete
from .models import Book, Category, CategoryStudy
import json 


# jquery autocomplete
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

# Autocomplete Outside
try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy
from django.views import generic

from .forms import BookForm, BookOutsideForm


# APPS VIEWS

# Default Nodos
def Nodos(request): 

    # Actualiza el fichero categorias.json y books.json desde la BD

    # JSON Relaciones
    relaciones = list(Category.objects.all())
    rel23 = [{"id":r.pk, "label":"[ " + r.name + " ]"}for r in relaciones]
    rel2 = json.dumps(rel23, skipkeys=False, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
    rel3 = "datac = '" + rel2 + "';"

    # Fichero relaciones
    fich_rel = ('nodos/static/nodos/data/categorias.json')
    archivo_rel = open(fich_rel, 'w+')
    archivo_rel.writelines(rel3)
    archivo_rel.close()

    # JSON LIBROS
    lista = list(Book.objects.all())
    # data = serializers.serialize('json', lista)
    data21 = [{"id": 999999, "label":"" , "shape": "", "image": "", "relacion":'',"nombre":"Dos", "libro":{ "autor":'', "isbn":'', "editorial":"","link":''},"anio":""}]
    link_cat = "category"
    data22 = [{"id":o.pk + int(1000000), "label":o.titulo, "shape": "image","image":o.imagen.url, "relacion":[ i.id for i in o.categorias.all() ], "nombre":'Dos', "libro":{"titulo":o.titulo, "autor": o.autor, "isbn":o.isbn, "editorial":o.editorial, "link":o.link, "cat_id":[ i.id for i in o.cate_estudio.all() ], "cat_estudio":[ "[ " + i.categoria_estudio + " ]" for i in o.cate_estudio.all() ], 'relaciones':['[ ' + i.name + ' ]' for i in o.categorias.all()],"id": o.pk }, "anio":o.year} for o in lista]
    data23 = data21 + data22
    data2 = json.dumps(data23) 
    # skipkeys=False, ensure_ascii=False, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False)
    data3 = "" + data2 + ""


    # Fichero libros
    fich = ('nodos/static/nodos/data/books.json')
    books = open(fich, 'w+')
    books.writelines(data3)
    books.close()

    # Diccionarios
    context = {'data3':data3,'rel3':rel3}

    return render(request, 'nodos/d-nodos.html', context)

# Default Mapa
def Mapa(request):

    # JSON Mapa
    mapaInfo = list(Book.objects.all())
    if '1900' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='00'))
    if '1910' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='10'))
    if '1920' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='20'))
    if '1930' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='30'))
    if '1940' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='40'))
    if '1950' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='50'))
    if '1960' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='60'))
    if '1970' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='70'))
    if '1980' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='80'))
    if '1990' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='90'))
    if '2000' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='2m'))
    if '2010' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='21'))
    if '2020' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='22'))


    data_map = [{"id":i.pk, "nombre":i.titulo,"type":"image","url":"/media/mapa/mmapa.png", "width":i.mapWidth, "height":i.mapHeight, "latitude":i.lat, "longitude":i.long,"attrsHover":{"transform":"s1.8"},"myText":{"autor":i.autor,"imagen":i.imagen.url,"cat_id":[ o.id for o in i.cate_estudio.all() ], "relacion":[ "[ " + o.name + " ]" for o in i.categorias.all() ], "cat_estudio":[ "[ " + o.categoria_estudio + " ]" for o in i.cate_estudio.all() ], "isbn":i.isbn, "editorial":i.editorial, "link":i.link}}for i in mapaInfo] 
    data_map2 = json.dumps(data_map)
    # Se borró datacd = ' '; - 27/12/18
    data_map3 = "" + data_map2 + ""
 
    # Fichero Mapa
    fich = ('nodos/static/nodos/data/ciudades.json')
    mapaf = open(fich, 'w+')
    mapaf.writelines(data_map3)
    mapaf.close()

    # Prueba II
    mapaf = open(fich, 'w+')
    mapaf.writelines(data_map3)
    mapaf.close() 

    # Diccionarios
    context = {'data_map3':data_map3, 'mapaInfo':mapaInfo}

    return render(request, 'nodos/d-mapa.html', context)

# Default Lista
def Lista(request):
    lista = Book.objects.all()

    cate = Book.objects.all()
    cates = CategoryStudy.objects.all()
    
    # Filtros Lista
    if 'title' in request.GET:
        lista = Book.objects.all().order_by('titulo')

    if 'author' in request.GET:
        lista = Book.objects.all().order_by('autor')

    if 'year' in request.GET:
        lista = Book.objects.all().order_by('year')
    
    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    # Diccionarios
    context = {'cates':cates ,'lista':lista, 'params':params}

    return render(request, 'nodos/d-lista.html', context)

# Nodos Search View
def resultadosNodos(request):
    # En books se pondría el límite a los libros
    books = list(Book.objects.all())
    busqueda = request.GET.get('qss', None)
    search = Book.objects.rel_search(busqueda)
    busqueda_index = {}
    data21 = [{"id": 999999, "label":"" , "shape": "", "image": "", "relacion":'',"nombre":"Dos", "libro":{ "autor":'', "isbn":'', "editorial":"","link":''},"anio":""}]
    data2 = []
    data3 = []
    data22 = []
    data23 = []
    libroM = []
    s2 = []
    r = []
    s3 = []


    # Si se busca libro o autor: Imprimir todos los libros
    if len(search) < 1:
        busqueda_index = busqueda  

        # Json
        data22 = [{"id":o.pk + int(1000000), "label":o.titulo, "shape": "image","image":o.imagen.url, "relacion":[ i.id for i in o.categorias.all() ], "nombre":'Dos', "libro":{"titulo":o.titulo, "autor": o.autor, "isbn":o.isbn, "editorial":o.editorial, "link":o.link, "cat_id":[ i.id for i in o.cate_estudio.all() ], "cat_estudio":[ "[ " + i.categoria_estudio + " ]" for i in o.cate_estudio.all() ], 'relaciones':['[ ' + i.name + ' ]' for i in o.categorias.all()],"id": o.pk }, "anio":o.year} for o in books]


    # Si se busca alguna categoría
    else:
        busqueda_index = 'stop'

        # Todas las relaciones en search
        for o in search:
            rel2 = o.categorias.all()
            m = {"id":o.pk, "label":o.titulo}
            # m = {"id":o.pk + int(1000000), "label":o.titulo, "shape": "image","image":o.imagen.url, "relacion":[ i.id for i in o.categorias.all() ], "nombre":'Dos', "libro":{"titulo":o.titulo, "autor": o.autor, "isbn":o.isbn, "editorial":o.editorial, "link":o.link, "cat_id":[ i.id for i in o.cate_estudio.all() ], "cat_estudio":[ "[ " + i.categoria_estudio + " ]" for i in o.cate_estudio.all() ], 'relaciones':['[ ' + i.name + ' ]' for i in o.categorias.all()],"id": o.pk }, "anio":o.year}
            libroM.append(m)

            for i in rel2:
                a = i.name
                r.append(a)

        # Traducir relaciones de serach en libros
        for i in range(len(r)):
            search3 = Book.objects.rel_search(str(r[i])).distinct()
            
            for o in search3:
                b = {"id":o.pk, "label":o.titulo}
                data2.append(b)
        

        # Ordenar y Eliminar libros repetidos
        titulolM = []
        for i in libroM:
            titulolM.append(i['label'])

        titulod2 = []
        for i in data2:
            titulod2.append(i['label'])

        listaB = titulolM
        listaR = titulod2

        data3 = listaB + listaR
        data5 = []
        for i in data3:
            if i not in data5:
                data5.append(i)

        # Lista Search con Lbúsqueda y relaciones Completa
        s2 = data5

        # Búsqueda Query final
        data22 = []
        for i in range(len(s2)):
            search5 = Book.objects.search(str(s2[i])).distinct()
            
            for o in search5:
                # json
                c = {"id":o.pk + int(1000000), "label":o.titulo, "shape": "image","image":o.imagen.url, "relacion":[ i.id for i in o.categorias.all() ], "nombre":'Dos', "libro":{"titulo":o.titulo, "autor": o.autor, "isbn":o.isbn, "editorial":o.editorial, "link":o.link, "cat_id":[ i.id for i in o.cate_estudio.all() ], "cat_estudio":[ "[ " + i.categoria_estudio + " ]" for i in o.cate_estudio.all() ], 'relaciones':['[ ' + i.name + ' ]' for i in o.categorias.all()],"id": o.pk }, "anio":o.year}
                data22.append(c)

        for i in data22:
            if 'label' in i:
                print(i['id'])

        # (s3 - Para Imprimir Query en html)
        s3 = search


    # Json
    # se quitó data = ''; de data3 27/12/18
    data23 = data21 + data22
    data2 = json.dumps(data23) 
    data3 = "" + data2 + ""
    
    # Fichero libros // ya no es necesario 27/12/18
    fich = ('nodos/static/nodos/data/books.json')
    books = open(fich, 'w+')
    books.writelines(data3)
    books.close()

        
    # Diccionarios
    page = 'nodos/r-nodos.html'
    context = {"data3":data3,"s3":s3,"s2":s2, "busqueda":busqueda,"busqueda_index":busqueda_index}

    return render(request, page, context)


# Mapa Search View
def resultadosMapa(request):
    mapaInfo = list(Book.objects.all())
    query = request.GET.get('q', None)
    mapaInfo = Book.objects.search(query)

    if '1900' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='00'))
    if '1910' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='10'))
    if '1920' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='20'))
    if '1930' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='30'))
    if '1940' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='40'))
    if '1950' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='50'))
    if '1960' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='60'))
    if '1970' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='70'))
    if '1980' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='80'))
    if '1990' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='90'))
    if '2000' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='2m'))
    if '2010' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='21'))
    if '2020' in request.GET:
        mapaInfo = list(Book.objects.filter(periodo__icontains='22'))

    # Resultados Búsqueda
    resul_map = [{"id":i.pk, "nombre":i.titulo,"type":"image","url":"/media/mapa/mmapa.png", "width":i.mapWidth, "height":i.mapHeight, "latitude":i.lat, "longitude":i.long,"attrsHover":{"transform":"s1.8"},"myText":{"autor":i.autor,"imagen":i.imagen.url,"cat_id":[ o.id for o in i.cate_estudio.all() ], "relacion":[ "[ " + o.name + " ]" for o in i.categorias.all() ], "cat_estudio":[ "[ " + o.categoria_estudio + " ]" for o in i.cate_estudio.all() ], "isbn":i.isbn, "editorial":i.editorial, "link":i.link}}for i in mapaInfo] 
    resul_map2 = json.dumps(resul_map)
    resul_map3 = "" + resul_map2 + ""

    # Fichero Mapa
    fich = ('nodos/static/nodos/data/ciudades.json')
    with open(fich, 'w') as mapaf:
        mapaf.writelines(resul_map3)
        mapaf.truncate()
        mapaf.close()

    with open(fich, 'r') as mapaf:
        mapaf.close()
    

    
    context =  {'query':query, 'mapaInfo':mapaInfo, 'resul_map3':resul_map3}

    return render(request, 'nodos/r-mapa.html', context)

# Lista Search view 
def resultadosLista (request):
    nresul = Book.objects.all().order_by('-created')[:3]
    query = request.GET.get('q', None)
    lista = Book.objects.search(query)
    
    # Filtros Lista
    if 'title' in request.GET:
        lista = lista.order_by('titulo')

    if 'author' in request.GET:
        lista = lista.order_by('autor')

    if 'year' in request.GET:
        lista = Book.objects.search(query).order_by('year')
    
    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = { 'nresul':nresul, 'lista':lista, 'params':params, 'query':query}
    
    return render(request, 'nodos/r-lista.html', context)

#  Relaciones View
def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    lista = Book.objects.filter(categorias=category)

    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = {'lista':lista, 'category':category, 'params':params}
    return render(request, "nodos/categorias.html", context)

# Categorias de estudio
def categoria_estudio(request, cate_id):
    cate = get_object_or_404(CategoryStudy, id=cate_id)
    lista = Book.objects.filter(categorias__cat_estudio=cate).distinct()
    
    listaa = Category.objects.filter(cat_estudio=cate).distinct()

    # Pagination
    paginator = Paginator(lista, 3)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()


    context = {'cate':cate,'listaa':listaa, 'lista':lista, 'params':params}
    return render(request, "nodos/categorias_estudio.html", context)

# Info_libro / Modals
def info_libro(request, book_id):
    libro = get_object_or_404(Book, id=book_id)
    lista = Book.objects.filter(titulo=libro)

   
    context = {'libro':libro, 'lista':lista}
    return render(request, "nodos/info_libro.html", context)

# User Info
def user_info(request):
    lista = Book.objects.all()

    cate = Book.objects.all()
    
    # Filtros Lista
    if 'title' in request.GET:
        lista = Book.objects.all().order_by('titulo')

    if 'author' in request.GET:
        lista = Book.objects.all().order_by('autor')

    if 'usuario' in request.GET:
        lista = Book.objects.all().order_by('usuario')

    if 'created' in request.GET:
        lista = Book.objects.all().order_by('created')

    if 'updated' in request.GET:
        lista = Book.objects.all().order_by('updated')
    
    # Pagination
    paginator = Paginator(lista, 10)
    page = request.GET.get('page')
    lista = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    # Diccionarios
    context = {'cate':cate ,'lista':lista, 'params':params}

    return render(request, 'nodos/user_info.html', context)

# R-User-Info
def ruser_info(request):
    nresul = Book.objects.all().order_by('-created')[:3]
    query = request.GET.get('q', None)
    listaa = Book.objects.search(query)
    
    # Filtros Lista
    if 'title' in request.GET:
        listaa = Book.objects.all().order_by('titulo')

    if 'author' in request.GET:
        listaa = Book.objects.all().order_by('autor')

    if 'usuario' in request.GET:
        listaa = Book.objects.all().order_by('usuario')

    if 'created' in request.GET:
        listaa = Book.objects.all().order_by('created')

    if 'updated' in request.GET:
        listaa = Book.objects.all().order_by('updated')
    
    # Pagination
    paginator = Paginator(listaa, 3)
    page = request.GET.get('page')
    listaa = paginator.get_page(page)

    # Safe filter paginator
    get_dict_copy = request.GET.copy()
    params = get_dict_copy.pop('page', True) and get_dict_copy.urlencode()

    context = { 'nresul':nresul, 'listaa':listaa, 'params':params, 'query':query}
    
    return render(request, 'nodos/r-user_info.html', context)


# Sin resultados
def sin_resultados(request):

    # Diccionarios
    context = {}

    return render(request, 'nodos/sin_resultados.html', context)
    
# AUTOCOMPLETE


# Autocomplete de prueba
def get_auto(request):
    q = request.GET.get('term', '')
    if request.is_ajax():
        q = request.GET.get('term', '')
        cat = Category.objects.filter(name__icontains=q)
        book = Book.objects.filter(titulo__icontains=q)
        results = []
        for name in cat:
            name_json = {}
            name_json['label'] = name.name
            name_json['category'] = "Categorias"
            results.append(name_json)

        results2 = []
        for name in book:
            name_json = {}
            name_json['label'] = name.titulo
            name_json['category'] = "Títulos"
            results2.append(name_json)

        q_chain = results2 + results
        data = json.dumps(q_chain)
    else:
        data = 'Funcionan los for ahora por el ajax.' 
    mimetype = 'application/json'

    context = {data}
    return HttpResponse(context, mimetype)

# Autocomplete Nodos
def get_auto_nodos(request):
    q = request.GET.get('term', '')
    if request.is_ajax():

        q = request.GET.get('term', '')
        cat = Category.objects.filter(name__icontains=q)
        book = Book.objects.filter(titulo__icontains=q)
        autor = Book.objects.filter(autor__icontains=q)

        results = []
        for name in autor:
            name_json = {}
            name_json['label'] = name.autor
            name_json['category'] = " Autor "
            results.append(name_json)

        results2 = []
        for name in book:
            name_json = {}
            name_json['label'] = name.titulo
            name_json['category'] = " Título "
            results2.append(name_json)


        q_chain = results2 + results
        data = json.dumps(q_chain)
    else:
        data = 'Funcionan los for ahora por el ajax.' 
    mimetype = 'application/json'

    context = {data}
    return HttpResponse(context, mimetype)

# Autocomplete Mapa y Lista
def get_auto_myl(request):
    if request.is_ajax():
        
        q = request.GET.get('term', '')
        cat = Category.objects.filter(name__icontains=q)
        book = Book.objects.filter(titulo__icontains=q)
        autor = Book.objects.filter(autor__icontains=q)

        results = []
        for name in cat:
            name_json = {}
            name_json['label'] = name.name
            name_json['category'] = "Categorias"
            results.append(name_json)

        results2 = []
        for name in book:
            name_json = {}
            name_json['label'] = name.titulo
            name_json['category'] = "Títulos"
            results2.append(name_json)

        results3 = []
        for name in autor:
            name_json = {}
            name_json['label'] = name.autor
            name_json['category'] = "Autor"
            results2.append(name_json)

        q_chain = results2 + results3 + results
        data = json.dumps(q_chain)
    else:
        data = 'Funcionan los for ahora por el ajax.' 
    mimetype = 'application/json'

    context = {data}
    return HttpResponse(context, mimetype)

# Autocomplete Admin
class LinkedDataView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = super(LinkedDataView, self).get_queryset()

        possessor = self.forwarded.get('possessor', None)
        secret = self.forwarded.get('secret', None)

        if secret != 42:
            return qs.none()

        if possessor:
            return qs.filter(cat_estudio_id=possessor)

        return qs




