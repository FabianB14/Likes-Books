from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import re
import bcrypt
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.contrib import messages 
from ..belt_users.models import LogUsers, Book
from ..belt_users.views import profile

def show_add_books(request):
    return render(request, 'books_add/add_books.html')
def add_books(request):
    response = ''
    response = Book.objects.add_book(request.POST, request.session['user_id'])
    
    book_info = {
        'Book': Book.objects.all(),
        'uploader_title': Book.objects.filter(uploader__id =request.session['user_id']) 
    }
    
    return render(request,'belt_users/index3.html', book_info)



# Create your views here.
