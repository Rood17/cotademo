from dal import autocomplete, forward
from .models import Category, Book
from django import forms


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('name', 'cat_estudio', 'catest')
        widgets = {
            'catest': autocomplete.ModelSelect2Multiple(
                url='linked_data_rf',
                forward=(forward.Field(src="cat_estudio", dst="possessor"),
                         forward.Const(val=42, dst="secret"))
            )
        }
    class Media:
        js = (
            'linked_data.js',
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')
        widgets = {
            'categorias': autocomplete.ModelSelect2Multiple(
            'categorias-autocomplete'
            )
        }

class BookOutsideForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('__all__')
        widgets = {
            'categorias': autocomplete.ModelSelect2(
                'categorias-autocomplete'
            )
        }