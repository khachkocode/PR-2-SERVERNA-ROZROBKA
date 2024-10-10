from django.db import models
from books.models import Book
from readers.models import Reader

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.reader.name} - {self.book.title}"
