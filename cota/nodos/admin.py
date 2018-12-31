from django.contrib import admin
from .models import Book, Category, CategoryStudy
from .forms import BookForm, BookForm, CategoryForm

# Register your models here.
class CategoryStudyAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('categoria_estudio', 'created', 'updated')
    list_filter = ('categoria_estudio', 'updated')

class TestInline(admin.TabularInline):
    form = CategoryForm
    model = Category
    fk_name = 'for_inline'

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    list_display = ('name', 'cat_estudio', 'created', 'updated')
    list_filter = ('cat_estudio', 'updated')
    search_fields = ('name', 'cat_estudio__categoria_estudio')
    ordering = ('cat_estudio', 'name')
    date_hierarchy = 'created'
    form = CategoryForm
    inlines = [TestInline]



class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    search_fields = ('titulo', 'autor','usuario__username', 'categorias__name')
    readonly_fields = ('created', 'updated')
    list_filter = ('categorias__cat_estudio', 'usuario__username')
    list_display = ('titulo', 'autor', 'lista_categorias', 'created', 'updated')
    fields = ['titulo','autor','descripcion','imagen',('editorial','isbn'),'procedencia',
                'year',('link_texto', 'link'), ('cate_estudio', 'categorias'),'resumen','usuario','created','updated',
                'pais', ('mapWidth', 'mapHeight'), ('long', 'lat'), 'periodo']
    form = BookForm

admin.site.register(CategoryStudy, CategoryStudyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
