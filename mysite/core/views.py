from re import U
import sqlite3
from unicodedata import name
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .forms import BookForm
from .models import Book


def Home(request):
    count= User.objects.count()
    return render(request,'home.html',{
        'count':count
    })


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    form = BookForm(request.POST, request.FILES)
    print(request.POST)
    if request.method == 'POST':
        newfile = Book(pdf = request.FILES['pdf'])
        # name =request.FILES['pdf']
        print(str(name))
        if form.is_valid():
            print(newfile.pdf.name)
            newfile.save()
            sqlupdate(newfile.pdf.name)
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

def sqlupdate(p):
# Connecting to sqlite
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    sq='UPDATE core_book SET title=\"'+str(p.split("/")[-1])+'\" WHERE pdf=\"'+str(p)+'\"'
    print(sq)
    cursor.execute(sq)
    conn.commit()
    conn.close()


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')



def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{
        'form':form
    })

def threed(request,na):

#     file1=Book()
#     file1.name = 'a.glb'
#     file1.pdf = 'a.glb'
#     file1.bool

#     file2=Book()
#     file2.name = 'P2_dmZt8Zg.glb'
#     file2.pdf = 'P2_dmZt8Zg.glb'
#     file2.bool

#     files = [file1,file2]
    print(na)
    return render(request,'threed.html',{
        'file1':na
    })

