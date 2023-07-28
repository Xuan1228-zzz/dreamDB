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
    path('gacha/', views.GachaAPIView.as_view(),),
]

urlpatterns += [ #使用者背包
    path("GearBag/", views.GearBagView.as_view()),
    path("ThingBag/", views.ThingBagView.as_view()), 

]

urlpatterns += [ #特定user的運動紀錄
    path("history/<int:year>/<int:month>/", views.ExerciseMonthView.as_view()), 
    path("task/", views.ExerciseWeekView.as_view()), 
    # path('complete-weekly-task/', views.CompleteWeeklyTaskAPIView.as_view()),
    path("history/<int:year>/<int:month>/<int:day>/", views.ExerciseDayView.as_view()),
]


# .list(), .retrieve(), .create(), .update(), .partial_update() , .destroy()
