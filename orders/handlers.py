import os

from django.dispatch import receiver
from django.core.mail import send_mail
from dotenv import load_dotenv

from orders.models import Order
from orders.signals import robots_add_signal


load_dotenv()
FROM_EMAIL = os.getenv('FROM_EMAIL')


@receiver(robots_add_signal)
def check_customer(sender, robot, **kwargs):

    matching_orders = Order.objects.filter(robot_serial=robot.serial)

    for order in matching_orders:

        customer_email = order.customer.email
        subject = f'Робот доступен {robot.serial}'
        message = f'Добрый день!\nНедавно вы интересовались нашим роботом модели {robot.model}, ' \
                  f'версии {robot.version}. Этот робот теперь в наличии.\n' \
                  f'Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'

        send_mail(subject, message, FROM_EMAIL, [customer_email])
