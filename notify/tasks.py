# from api.models import Exercise
# from datetime import timedelta
# from celery import shared_task
# from django.utils import timezone
# from accounts.models import User

# @shared_task
# def reminder():
#     now = timezone.now()
#     time_up = now - timedelta(seconds=10)

#     records = Exercise.objects.filter(exercise_time__gte=time_up)