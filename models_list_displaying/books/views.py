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

    book_objects = Book.objects.filter(pub_date=page_date)
    book_objects1 = Book.objects.filter(pub_date__lt=page_date)[:1]
    book_objects2 = Book.objects.filter(pub_date__gt=page_date)[:1]
    # print(book_objects1[0].pub_date, len(book_objects1), len(book_objects2))
    prev_page = book_objects1[0].pub_date if len(book_objects1) > 0 else None
    next_page = book_objects2[0].pub_date if len(book_objects2) > 0 else None
    # print(prev_page, next_page)
    # book_objects = Book.objects.all()
    books = [{'name': b.name, 'author': b.author, 'pub_date': b.pub_date} for b in book_objects]
    # paginator = Paginator(books, 10)
    # page = paginator.get_page(page_date)
    # context = {'books': books, 'page': page}
    context = {'books': books, 'prev_page': prev_page, 'next_page': next_page}
    return render(request, template, context)