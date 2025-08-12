from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    query = request.GET.get('q', '').strip()
    if query:
        books = Book.objects.filter(title__icontains=query)  # safe ORM filtering
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'query': query})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Implement your form validation and save logic here
        # For example:
        # form = BookForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, "Book created successfully.")
        #     return redirect('bookshelf:book_list')
        pass
    else:
        # form = BookForm()
        pass
    return render(request, 'bookshelf/create_book.html')  # Replace with your actual template

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Implement your form validation and update logic here
        # form = BookForm(request.POST, instance=book)
        # if form.is_valid():
        #     form.save()
        #     messages.success(request, "Book updated successfully.")
        #     return redirect('bookshelf:book_list')
        pass
    else:
        # form = BookForm(instance=book)
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})  # Replace with your actual template

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, "Book deleted successfully.")
    return redirect('bookshelf:book_list')
