from django.http import HttpResponse
from django.shortcuts import render

from book.models import Book
from reader.models import Reader
from reader.forms import CreateReaderForm


def create_reader(request):
    if request.method == 'POST':
        form = CreateReaderForm(request.POST)
        if form.is_valid():
            reader_first_name = form.cleaned_data['first_name']
            reader_last_name = form.cleaned_data['last_name']
            reader_age = form.cleaned_data['age']
            reader = Reader.objects.create(first_name=reader_first_name, last_name=reader_last_name, age=reader_age)
            reader.save()
            book = Book.objects.all()[len(Book.objects.all())-1]
            return HttpResponse("Last added book is " + book.author + "'s " + book.name + " which was published in " + str(book.published_year))
    form=CreateReaderForm()
    return render(request, 'create_reader.html', {'form': form})
