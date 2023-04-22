from django import forms
from .models import Todo


class TodoCreateForm(forms.Form):
    '''create a simple form '''
    title = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()


class TodoUpdateForm(forms.ModelForm):
    '''Create a form for update todos.this class create a form base on todo models'''
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')
