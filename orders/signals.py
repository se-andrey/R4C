from django.db.models.signals import Signal, post_save
from django.dispatch import receiver

from robots.models import Robot


robots_add_signal = Signal()

@receiver(post_save, sender=Robot)
def robots_ad_handler(sender, instance, created, **kwargs):
    print(1)
    if created:
        robots_add_signal.send(sender=instance.__class__, robot=instance)