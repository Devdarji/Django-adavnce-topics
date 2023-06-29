# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from sel_pre_related.db_queries import (
    books_list,
    book_list_selected_related,
    store_list,
    store_list_prefetch_related,
    course_list,
)


# Create your views here.
class HomeView(APIView):
    @staticmethod
    def get(request):

        # call books list -> without select_related
        books_list()

        # book_list_selected_related -> with select_related
        book_list_selected_related()

        # store list -> without prefetch related
        store_list()

        # store_list_prefetch_related -> with prefetch related
        store_list_prefetch_related()

        course_list()
        return Response(
            {"status": "success", "message": "Successfully Transferred", "payload": ""},
            status=status.HTTP_200_OK,
        )
