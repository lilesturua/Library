from django.http import HttpResponse
from django.shortcuts import render

from book.forms import CreateBookForm
from book.models import Book


def create_book(request):
    if request.method == 'POST':
        form=CreateBookForm(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data['name']
            author_name=form.cleaned_data['author']
            book_published_year=form.cleaned_data['published_year']
            book = Book.objects.create(name=book_name, author=author_name, published_year=book_published_year)
            book.save()
            return HttpResponse("book " + book_name + " by " + author_name + " was published in " + str(book_published_year))
    form = CreateBookForm
    return render(request, 'create_book.html', {'form': form})

