from django.urls import path
from django_transaction import views as django_transaction_views

urlpatterns = [
    path("", django_transaction_views.TransferView.as_view(), name="transfer-view"),
    path("course/", django_transaction_views.CourseView.as_view(), name="course-view"),
]
