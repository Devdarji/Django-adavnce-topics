from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    balance = models.DecimalField(max_digits=32, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transfer(models.Model):
    initiated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="initiated_transfers"
    )
    transfer_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_transfers"
    )
    amount = models.DecimalField(max_digits=32, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    course_name = models.CharField(max_length=100)
