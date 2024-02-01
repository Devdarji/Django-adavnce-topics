from django.db.models.signals import post_save
from django.dispatch import receiver
from sel_pre_related import models as sel_pre_related_models


@receiver(post_save, sender=sel_pre_related_models.Publisher)
def publisher_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"A new record created : {instance}")
    else:
        print(f"Record Updated: {instance}")


post_save.connect(publisher_post_save, sender=sel_pre_related_models.Publisher)
