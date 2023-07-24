from django.urls import path, include
from . import views

# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path("gears/", views.GearView.as_view({"get": "list", "post": "create"})),
    path("gears/<int:pk>", views.GearView.as_view({"get": "retrieve"})),
    path("things/", views.ThingView.as_view({"get": "list", "post": "create"})),
    path("things/<int:pk>", views.ThingView.as_view({"get": "retrieve"})),
    path("exercises/", views.ExerciseView.as_view({"get": "list", "post": "create"})),
    path("exercises/<int:pk>", views.ExerciseView.as_view({"get": "retrieve"})),
]

urlpatterns += [
    path("MonthHistory/<int:user_id>/", views.ExerciseMonthView.as_view()), #特定user的運動紀錄
    path("WeekTask/<int:user_id>/", views.ExerciseWeekView.as_view()), #特定user的運動紀錄
]

urlpatterns += [
    path("DayHistory/<int:user_id>/", views.ExerciseDayView.as_view()), #特定user的運動紀錄
]

urlpatterns += [
    # 其他 URL 配置...
    path('complete-weekly-task/<int:user_id>/', views.CompleteWeeklyTaskAPIView.as_view()),
]

# .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
