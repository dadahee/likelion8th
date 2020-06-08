from django import forms
from .models import Todo
from lab06 import settings

class TodoForm(forms.ModelForm):
    date = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, help_text="Formats: YYYY-MM-DD", required=True)
    class Meta:
        model = Todo
        fields = '__all__' # 북마크의 모든 필드를 가져오자!