from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        default_related_name = "books"

    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "publisher_name": self.publisher.name,
        }

    def __str__(self) -> str:
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)

    class Meta:
        default_related_name = "stores"

    def __str__(self) -> str:
        return self.name
