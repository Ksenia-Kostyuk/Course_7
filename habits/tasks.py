from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from users.models import User
from users.services import reminder_of_a_habit


@shared_task
def send_mail_habit(email):
    """Отправляет пользователю напоминание о выполнении привычки"""
    message = 'Вы не выполняли привычку более 7 дней'
    send_mail('Вы давно не выполняли привычку', 'Вы не выполняли привычку более 7 дней', EMAIL_HOST_USER, [email])
    user = User.objects.get(email=email)
    if user.tg_chat_id:
        reminder_of_a_habit(user.tg_chat_id, message)
