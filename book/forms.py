from django import forms


class CreateBookForm(forms.Form):
    name = forms.CharField(label='Book name', max_length=100)
    author = forms.CharField(label='Author name', max_length=100)
    published_year = forms.IntegerField(label='Published year')
