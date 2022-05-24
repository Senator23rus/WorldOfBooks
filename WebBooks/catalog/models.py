from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Input genre of the book", verbose_name="Genre book")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Input language of the book", verbose_name="Book language")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Input name author", verbose_name="Author name")
    last_name = models.CharField(max_length=100, help_text="Input family name author",
                                 verbose_name="Author family name")
    date_of_birth = models.DateField(help_text="Input date of birth", verbose_name="Birth date", null=True, blank=True)
    date_of_death = models.DateField(help_text="Input date of death", verbose_name="Death date", null=True, blank=True)

    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Input title of the book", verbose_name="Name of book")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text=" Choose genre of the book",
                              verbose_name="Genre of book", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text=" Choose language of the book",
                                 verbose_name="Language of book", null=True)
    author = models.ManyToManyField('Author', help_text=" Choose author of the book", verbose_name="Author of book")
    summary = models.TextField(max_length=1000, help_text="Input summary of the book",
                               verbose_name="Short text of the book")
    isbn = models.CharField(max_length=13, help_text="Only 13 symbols", verbose_name="ISBN of the book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Authors'


class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Input status of book", verbose_name="Status exemplar of book")

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_num = models.CharField(max_length=20, null=True, help_text="Input inentary number",
                               verbose_name="Inventary humber")
    inprint = models.CharField(max_length=200, help_text="Input publishing and year", verbose_name="Publishing")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, help_text="Change status exemplar",
                               verbose_name="Status exemplar")
    due_back = models.DateField(null=True, blank=True, help_text="Input end of status", verbose_name="Date of status")

    def __str__(self):
        return '%s %s %s' % (self.inv_num, self.book, self.status)
