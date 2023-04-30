from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер . {order_id}'
    message = f'Уважаемый (ая) {order.first_name}, \n\n' \
              f'Ваш заказ получен и мы приступаем к сборке '  \
              f'Номер Вашего заказа {order_id}'
    mail_sent = send_mail(subject,message,'shop@hogart.ru', [order.email])
    return mail_sent