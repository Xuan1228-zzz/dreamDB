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

urlpatterns += [ #使用者背包
    path("GearBag/<int:user_id>/", views.GearBagView.as_view()),
    path("ThingBag/<int:user_id>/", views.ThingBagView.as_view()), 

]

urlpatterns += [ #特定user的運動紀錄
    path("MonthHistory/<int:user_id>/", views.ExerciseMonthView.as_view()), 
    path("WeekTask/<int:user_id>/", views.ExerciseWeekView.as_view()), 
    path('complete-weekly-task/<int:user_id>/', views.CompleteWeeklyTaskAPIView.as_view()),
    path("DayHistory/<int:user_id>/", views.ExerciseDayView.as_view()),
]


# .list(), .retrieve(), .create(), .update(), .partial_update(), .destroy()
