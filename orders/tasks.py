from ESHOP3.celery import app
from django.core.mail import send_mail
from .models import Order


@app.task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ № {}'.format(order_id)
    message = 'Уважаемый {}, \n\nВаш заказ успешно размещен.' \
              'Номер заказа: {}'.format(order.first_name,
                                        order.id)
    mail_sent = send_mail(subject,
                          message,
                          'iorbit4557@gmail.com'
                          [order.email])

    return mail_sent
