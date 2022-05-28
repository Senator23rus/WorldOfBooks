from django.shortcuts import render
from django.http import *
from .models import Book, Author, BookInstance, Genre
from .forms import AuthorsForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin




def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html', context={'num_books': num_books,
                                                  'num_instances': num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors,
                                                  'num_visits': num_visits,
                                                  })

class BookListView(generic.ListView):
    model = Book
    paginate_by = 3

class BookDetalView(generic.DetailView):
    model = Book
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')

def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html",
                  {"form": authorsform, "author": author})