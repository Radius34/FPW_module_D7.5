from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


def send_article_emails():
    pass
#  логика для отправки списка статей на почту подписчикам


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')
# Запустить задачу каждую пятницу в 18:00
    scheduler.add_job(send_article_emails, 'cron', day_of_week='fri', hour=18)

    register_events(scheduler)
    scheduler.start()