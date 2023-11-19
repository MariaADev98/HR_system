from django import forms

class TaskForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    content = forms.CharField(widget=forms.Textarea(), label='Содержание')
    autor = forms.CharField(max_length=100, label='Автор')
    status = forms.CharField(max_length=3, label='Статус')