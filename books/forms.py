from django import forms
from .widgets import CustomClearableFileInput
from .models import Book, Genre


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        exclude = ('rating',)
        labels = {
            'author': 'Author',
            'name': 'Name',
            'sku': 'Sku',
            'language': 'Language',
            'pages': 'Pages',
            'year': 'Year of Publish',
            'country': 'Country of Origin',
            'genres': 'Genres',
            'price': 'Price',
            'imageLink': 'Image'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        genre_set = Genre.objects.all()
        friendly_names = [(g.id, g.get_friendly_name()) for g in genre_set]
        genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        required=True
        )
        self.fields['genres'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 form-control'

