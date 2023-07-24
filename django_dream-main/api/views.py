# from django.shortcuts import render
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


class GearView(ModelViewSet):
    queryset = Gear.objects.all()
    serializer_class = GearSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseView(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):  #
        data = serializer.validated_data
        gear = data.get("gear")
        accuracy = data.get("accuracy")  # or from server

        if gear.user != self.request.user:
            raise PermissionDenied("You are not allowed to modify this gear.")

        # 之後修改加權方式
        gear.exp += accuracy  # calculate exp with exercise...
        gear.save()

        serializer.save(user=self.request.user)

        # return Response(serializer.data, status=201) # customize response

class ExerciseMonthView(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id): #抓取特定user以及當前月份完成運動的紀錄
        year = int(request.GET.get("year"))
        month = int(request.GET.get("month"))
        exercises =  (Exercise.objects.filter(
                    user_id=user_id,
                    timestamp__year=year,
                    timestamp__month=month,)
                    .dates("timestamp", "day")
                    .values_list("timestamp__day", flat=True)
                    )
    
        print(exercises)

        return Response({
            "year":year,
            "month":month,
            "days":list(exercises)
            # "current_month_records":serializer.data,
            # "type":serializer1.data,
        })

class ExerciseDayView(APIView): #使用者每日運動種類與次數 目前是直接加總
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        year = int(request.GET.get("year"))
        month = int(request.GET.get("month"))
        day = int(request.GET.get("day"))
        type_filter = Q(gear__type=0) | Q(gear__type=1) | Q(gear__type=2)
        
        exercises = Exercise.objects.filter(
            user_id=user_id,
            timestamp__year=year,
            timestamp__month=month,
            timestamp__day=day
        ).filter(
            type_filter
        ).values('gear__type').annotate(
            type_total_count=Sum('count')
        )
        # 使用列表推导式将每个gear类型和对应的count字段组合成字典
        result_data = [{"gear_type": item["gear__type"], "count": item["type_total_count"]} for item in exercises]
        
        print(result_data)

        return Response(result_data)
    
class CompleteWeeklyTaskAPIView(APIView): 
#現在的寫法為寫入運動資料前要先call這個API，不然會顯示already completed --> 有待優化
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        today = datetime.now().date()

        # 獲取使用者當天的所有運動紀錄
        exercises = Exercise.objects.filter(user_id=user_id, timestamp__date=today)

        this_week_task, created = WeekTask.objects.get_or_create(user_id=user_id, week_start_date=today - timedelta(days=today.weekday()))
        # 檢查今天是否已经完成任务，避免重複計算
        if exercises.exists():
            return Response({'message': 'You have already completed the task for today.'})

        # 檢查是否創建了新的 WeekTask
        if created:
            # 如果新創建了 WeekTask ，設置 task_count 為 1
            this_week_task.task_count = 1
        else:
            # 如果獲取到了已存在的 WeekTask，將 task_count 加 1
            this_week_task.task_count += 1

        # 更新上次完成日期為今天
        this_week_task.last_completed_date = today

        if this_week_task.task_count > 7:
            this_week_task.task_count = 1
            this_week_task.week_start_date = today #更新每周任務開始日期
            this_week_task.save()# 保存更新後的 WeekTask 
        else:
            this_week_task.save()# 保存更新後的 WeekTask 
        

        # 檢查是否完成了每周任务
        if this_week_task.task_count >= 7:
            # 给予獎勵-->待更新，獎勵為何?
            return Response({'message': 'Congratulations!'})        
        else:
            return Response({'message': 'Week-Task completed for today.'})

# class ExerciseWeekView(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         today = datetime.now().date()

#         # 获取用户过去七天的所有运动记录
#         seven_days_ago = today - timedelta(days=7)
#         exercises = Exercise.objects.filter(
#             user=user,
#             timestamp__date__gte=seven_days_ago, 
#             timestamp__date__lte=today
#             )

#         # 检查是否连续七天完成任务
#         if exercises.count() >= 7:
#             # 给予奖励（根据具体需求实现）
#             return Response({'message': 'Congratulations! You have completed the weekly task for seven consecutive days and earned a reward.'})
#         else:
#             return Response({'message': 'Task completed for today.'})