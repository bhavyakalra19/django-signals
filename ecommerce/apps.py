from django.apps import AppConfig
from django.db.models.signals import post_save

def example_reciever(sender, **kwargs):
    print("Message is recieved from sender")


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'
    
    def ready(self) -> None:
        import ecommerce.signals
    