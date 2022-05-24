
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetalView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),

]

