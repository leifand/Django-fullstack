from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.all()
    books_data = { 'books' : books }
    return render(request, 'fullbooks/index.html', books_data)

# enter user data for new book into db
def add_book(request):
    if request.method == 'POST':
        name = request.POST['author']
        author = Author.objects.create(name=name)
        book = Book.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            author = author
        )
    return redirect('/')
