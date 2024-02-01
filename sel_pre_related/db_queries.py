from sel_pre_related.debugger import query_debugger
from sel_pre_related import models

from django_transaction import models as tr_models


@query_debugger
def books_list():
    print("==================================================================")
    print("Without select related")
    print("==================================================================")
    queryset = models.Book.objects.filter()

    # books = [obj.name for obj in queryset]
    books = []

    # print(books)

    for book in queryset:
        books.append(
            {"id": book.id, "name": book.name, "publisher": book.publisher.name}
        )

    return books


@query_debugger
def book_list_selected_related():
    print("==================================================================")
    print("Select related")
    print("==================================================================")
    queryset = models.Book.objects.select_related("publisher")

    books = [obj.get_details() for obj in queryset]

    # print(books)

    # for book in queryset:
    #     books.append(
    #         {"id": book.id, "name": book.name, "publisher": book.publisher.name}
    #     )

    return books


@query_debugger
def store_list():
    print("==================================================================")
    print("Without prefetch related")
    print("==================================================================")

    queryset = models.Store.objects.all()

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({"id": store.id, "name": store.name, "books": books})

    return stores


@query_debugger
def store_list_prefetch_related():
    print("==================================================================")
    print("Prefetch related")
    print("==================================================================")

    queryset = models.Store.objects.prefetch_related("books")

    stores = []

    for store in queryset:
        books = [book.name for book in store.books.all()]
        stores.append({"id": store.id, "name": store.name, "books": books})

    return stores


@query_debugger
def course_list():
    print("==================================================================")
    print("Select related")
    print("==================================================================")
    # name = "%ankit%g%goswami%"
    # new_name = name.replace("%", " ").strip()
    # print(new_name)
    # instance = models.Book.objects.filter(name__icontains=new_name)

    # print("===================> ", instance)
    queryset = tr_models.Course.objects.all()

    courses = []

    for course in queryset:
        courses.append({"name": course.course_name})

    return courses


@query_debugger
def transfer_select_related():
    # "initiated_by", "transfer_to"
    queryset = tr_models.Transfer.objects.select_related()

    transfers = []

    for transfer in queryset:
        transfers.append(
            {
                "id": transfer.id,
                "amount": transfer.amount,
                "created_at": transfer.created_at,
                "initiated_by": transfer.initiated_by.username,
                "transfer_to": transfer.transfer_to.username,
            }
        )

    print(transfers)
    return transfers
