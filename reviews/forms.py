from django import forms
from books.widgets import CustomClearableFileInput
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('book_id', 'user_id')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'