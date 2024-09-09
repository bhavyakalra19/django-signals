from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Product

@receiver(post_save, sender=Product)
def example_reciever(sender, instance, created, **kwargs):
    print("hello")
    print(instance)
    print(created)