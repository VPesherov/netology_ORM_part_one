import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()

    # [{}, {}, {}]
    books = [{'name': b.name, 'author': b.author, 'pub_date': b.pub_date} for b in book_objects]
    context = {'books': books}
    return render(request, template, context)


def books_date_view(request, date):
    template = 'books/books_list.html'
    page_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    # print(page_date)

    book_objects = Book.objects.filter(pub_date=page_date)
    book_objects1 = Book.objects.filter(pub_date__lt=page_date)[:1]
    book_objects2 = Book.objects.filter(pub_date__gt=page_date)[:1]
    print(book_objects1, book_objects2)
    # book_objects = Book.objects.all()
    books = [{'name': b.name, 'author': b.author, 'pub_date': b.pub_date} for b in book_objects]
    paginator = Paginator(books, 10)
    page = paginator.get_page(page_date)
    context = {'books': books, 'page': page, 'pub_date': page_date}
    return render(request, template, context)