import random

from django.core.management.base import BaseCommand
from sel_pre_related import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Publisher.objects.all().delete()
        models.Book.objects.all().delete()
        models.Store.objects.all().delete()

        # create a 5 publishers
        publishers = [
            models.Publisher(name=f"Publisher{index}") for index in range(1, 6)
        ]
        models.Publisher.objects.bulk_create(publishers)

        # create a 20 books for every publishers
        counter = 0
        books = []

        for publisher in models.Publisher.objects.all():
            for i in range(20):
                counter += 1
                books.append(
                    models.Book(
                        name=f"Book{counter}",
                        price=random.randint(50, 300),
                        publisher=publisher,
                    )
                )

        models.Book.objects.bulk_create(books)

        # create 10 stores and insert 10 books in every store
        books = list(models.Book.objects.all())

        for i in range(10):
            temp_book = [books.pop() for i in range(10)]
            store = models.Store.objects.create(name=f"Store{i+1}")
            store.books.set(temp_book)
            store.save()
