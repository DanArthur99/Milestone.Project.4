from django import forms
from books.widgets import CustomClearableFileInput
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('book', 'user',)
        labels = {
            'title': 'Title',
            'user_rating': 'Rating',
            'content': 'Write Your Review!'
        }
    
    user_rating = forms.ChoiceField(
        choices=(
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
            (6, 6),
            (7, 7),
            (8, 8),
            (9, 9),
            (10, 10),
        )
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0 form-control'