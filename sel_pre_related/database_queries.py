from sel_pre_related.debugger import query_debugger
from sel_pre_related import models


@query_debugger
def book_list():
    print("======================")
    print("without select related")
    print("======================")

    queryset = models.Book.objects.all()

    books = []

    for book in queryset:
        books.append(
            {
                "id": book.id,
                "name": book.name,
                "price": book.price,
                "publisher": book.publisher.name,
            }
        )

    return books


@query_debugger
def book_list_with_select_related():
    print("======================")
    print("with select related")
    print("======================")

    queryset = models.Book.objects.select_related("publisher")

    books = []

    for book in queryset:
        books.append(
            {
                "id": book.id,
                "name": book.name,
                "price": book.price,
                "publisher": book.publisher.name,
            }
        )

    return books


@query_debugger
def store_list():
    print("======================")
    print("without prefetch related")
    print("======================")

    queryset = models.Store.objects.all()  # 1

    stores = []

    for store in queryset:
        books = [obj.name for obj in store.books.all()]  # 10
        stores.append({"id": store.id, "name": store.name, "books": books})

    return books


@query_debugger
def store_list_prefetch_related():
    print("======================")
    print("with prefetch related")
    print("======================")

    queryset = models.Store.objects.prefetch_related("books")  # 1

    stores = []

    for store in queryset:
        books = [obj.name for obj in store.books.all()]  # 10
        stores.append({"id": store.id, "name": store.name, "books": books})

    return books
