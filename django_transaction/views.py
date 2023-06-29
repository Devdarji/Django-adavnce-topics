from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.db import transaction
from django.http import JsonResponse
from django.core.cache import cache

from django_transaction import models as django_transaction_models

"""
    ACID
     - Atomicity
     - Consistency
     - Isolation
     - Durability
"""


# Create your views here.
class TransferView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        request_data = request.data

        amount = Decimal(request_data.get("amount"))
        receiving_user_id = request_data.get("receiving_user_id")

        with transaction.atomic():
            # initiator_account = django_transaction_models.UserAccount.objects.select_for_update(nowait=True).filter(
            #     user=request.user
            # ).last()

            initiator_account = django_transaction_models.UserAccount.objects.filter(
                user=request.user
            ).last()

            if initiator_account.balance < amount:
                return Response(
                    {
                        "status": "Error",
                        "message": "You do not have enough funds.",
                        "payload": "",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # transfer_instance = django_transaction_models.Transfer.objects.create(
            #     initiated_by=request.user, transfer_to=receiving_user_id, amount=amount
            # )

            django_transaction_models.Transfer.objects.create(
                initiated_by=request.user, transfer_to=receiving_user_id, amount=amount
            )

            initiator_account.balance = initiator_account.balance - amount
            receiving_user_account = django_transaction_models.UserAccount.objects.filter(
                user_id=receiving_user_id
            ).last()

            receiving_user_account.balance = receiving_user_account.balance + amount

            initiator_account.save(update_fields=["balance"])
            receiving_user_account.save(update_fields=["balance"])

            return Response(
                {
                    "status": "success",
                    "message": "Successfully Transferred",
                    "payload": "",
                },
                status=status.HTTP_200_OK,
            )


class CourseView(APIView):
    @staticmethod
    def get(request):
        payload = []
        if cache.get("courses"):
            payload = cache.get("courses")

            print(cache.ttl("courses"))
            db = "redis"
        else:
            instances = django_transaction_models.Course.objects.all()
            payload = [data.course_name for data in instances]
            cache.set("courses", payload, 25)
            db = "sqlite"

        return JsonResponse({"status": 200, "db": db, "data": payload})
