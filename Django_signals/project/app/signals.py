import time
import threading
from django.db import transaction, IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def receiver(sender, instance, **kwargs):
    print("Signal received. Start heavy processing...")
    time.sleep(5)  # Simulate heavy processing
    print("Signal processed")

    print(f"Signal running in thread: {threading.current_thread().name}")

    print(f"Signal received, user: {instance.username}")
    instance.username = 'newusername'
    instance.save()
