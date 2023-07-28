# from django.shortcuts import render
import random
from accounts.models import User
from .models import Thing, Gear, Exercise, WeekTask
from datetime import datetime, timedelta
from django.db.models import Sum,Q
from accounts.permissions import IsUserOrAdmin
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    GearSerializers,
    ThingSerializers,
    ExerciseSerializers,
)


class ThingView(ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ThingBagView(APIView): #查看使用者背包，可查看現有的小物
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        thing = Thing.objects.filter(user=request.user).order_by("level")
        serializer = GearSerializers(instance=thing, many=True)

        return Response(serializer.data)

class GachaAPIView(APIView):

    permission_classes = [IsAuthenticated]  

    def post(self, request):

        # 設定各等級小物的機率值
        level_probabilities = {
            "BASIC": 0.6,
            "INTERMEDIATE": 0.3,
            "HIGH_END": 0.1,
        }

         # 根據機率隨機獲取一個等級
        level_choices = list(level_probabilities.keys())
        level_probabilities_values = list(level_probabilities.values())
        random_level = random.choices(level_choices, weights=level_probabilities_values)[0]
        print(random_level)
        # 檢查是否已經有同一等級的thing存在
        existing_thing = Thing.objects.filter(user=request.user, level=random_level).first()

        if existing_thing:
            # 如果已存在，將amount加一
            existing_thing.amount += 1
            existing_thing.save()
            new_thing = existing_thing
        else:
            # 否則創建新的thing
            new_thing = Thing.objects.create(user=request.user, level=random_level)
            new_thing.amount = 1
            new_thing.save()

        # 返回結果
        response_data = {
            "message": "You got a new thing!",
            "thing_id": new_thing.pk,
            "level": [new_thing.level, new_thing.get_level_display()],
            "amount": new_thing.amount,
        }
        return Response(response_data)

class GearView(ModelViewSet):
    queryset = Gear.objects.all()
    serializer_class = GearSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GearBagView(APIView): #查看使用者背包，可查看現有的NFT
    
    permission_classes = [IsAuthenticated]

    def get(self, request):
        gear = Gear.objects.filter(user=request.user).order_by("type")
        serializer = GearSerializers(instance=gear, many=True)

        return Response(serializer.data)

class ExerciseView(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializers
    permission_classes = [IsAuthenticated]
    
    # def perform_create(self, serializer):  
    #     data = serializer.validated_data
    #     gear = data.get("gear")
    #     accuracy = data.get("accuracy")  # or from server

    #     if gear.user != self.request.user:
    #         raise PermissionDenied("You are not allowed to modify this gear.")

    #     # 之後修改加權方式
    #     gear.exp += accuracy  # calculate exp with exercise...
    #     gear.save()

    #     serializer.save(user=self.request.user)

    #     # return Response(serializer.data, status=201) # customize response
    def perform_create(self, serializer):  
        data = serializer.validated_data
        gear = data.get("gear")
        # accuracy = data.get("accuracy")
        # count = data.get("count")

        if gear.user != self.request.user:
            raise PermissionDenied("You are not allowed to modify this gear.")

        thing_level = self.request.data.get("thing_level")  # Get the thing_level from the request data
        serializer.save(user=self.request.user, thing_level=thing_level)  # Save the instance with thing_level


class ExerciseMonthView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month): #抓取特定user以及當前月份完成運動的紀錄

        exercises =  (Exercise.objects.filter(
                    user = request.user,
                    timestamp__year=year,
                    timestamp__month=month,)
                    .dates("timestamp", "day", )
                    # .values_list("timestamp__day", flat=True)
                    )
    
        print(exercises)

        return Response({
            "days":list(exercises)
        })
    
class ExerciseWeekView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request): #抓取特定user以及當前月份完成運動的紀錄
        # date = datetime.today().date()
        # task = request.user.task
        task = User.objects.get(pk=request.user.pk).task

        start = task.week_start
        count = task.count
        # end = start + timedelta(days=7)
        # exercise_days = Exercise.objects.filter(timestamp__range=(start, end))
        days = [{"date":start + timedelta(i), "done":i < count} for i in range(7)]

    
        print(days)

        return Response(days)
    
    def post(self, request):
        today = datetime.now().date()

        # 獲取使用者當天的所有運動紀 錄
        if Exercise.objects.filter(user=request.user, timestamp__date=today).exists():
            return Response({'message': 'You have already completed the task for today.'})

        task = WeekTask.objects.get(user=request.user)
        delta = today - task.week_start
        # 檢查今天是否已经完成任务，避免重複計算
        # res = None
        if delta == timedelta(days=task.count):
            task.count += 1
            if task.count >= 7:
                task.count = 0
                res = "恭喜"
            else:
                res = "++"
        elif delta == timedelta(days=task.count - 1):
            return Response({'message': 'You have already completed the task for today.'})
        else:
            task.week_start = today
            task.count = 1
            res = "restart"
     
        task.save()# 保存更新後的 WeekTask 
        
        return Response({'message': res, "count":task.count, "start":task.week_start})  

class ExerciseDayView(APIView): #使用者每日運動種類與次數 目前是直接加總
    permission_classes = [IsAuthenticated]

    def get(self, request, year, month, day):

        type_filter = Q(gear__type=0) | Q(gear__type=1) | Q(gear__type=2)
        
        exercises = Exercise.objects.filter(
            user = request.user,
            timestamp__year=year,
            timestamp__month=month,
            timestamp__day=day
        ).filter(
            type_filter
        ).values('gear__type').annotate(
            type_total_count=Sum('count')
        )
        print(exercises)
        # 使用列表推导式将每个gear类型和对应的count字段组合成字典
        result_data = {item["gear__type"]:{"count": item["type_total_count"]} for item in  exercises}
        result = [{"type":type[1], "count":0} for type in Gear.Type.choices]
        for k,v in result_data.items():
            result[k]["count"] = v["count"]
        
        return Response(result)
    
     
    
class CompleteWeeklyTaskAPIView(APIView): 
#現在的寫法為寫入運動資料前要先call這個API，不然會顯示already completed --> 有待優化
    permission_classes = [IsAuthenticated]

    def post(self, request):
        today = datetime.now().date()

        # 獲取使用者當天的所有運動紀 錄
        if Exercise.objects.filter(user=request.user, timestamp__date=today).exists():
            return Response({'message': 'You have already completed the task for today.'})

        task = WeekTask.objects.get(user=request.user)
        # 檢查今天是否已经完成任务，避免重複計算

        if today - task.week_start == timedelta(days=task.count):
            task.count += 1
            if task.count >= 7:
                task.count = 0
                res = {'message': 'Congratulations!'}
        else:
            task.week_start = today
            task.count = 1
            res = {'message': 'Week-Task completed for today.'}
     
        task.save()# 保存更新後的 WeekTask 
        
        return Response(res)       