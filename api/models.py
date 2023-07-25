# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models

from accounts.models import User


class Gear(models.Model):
    class Level(models.TextChoices):
        BASIC = ("BASIC", "初階")
        INTERMEDIATE = ("INTERMEDIATE", "中階")
        ADVANCED = ("ADVANCED", "進階")

    class Color(models.TextChoices):
        DARK = ("DARK", "暗色")
        BRIGHT = ("BRIGHT", "亮色")
        COLORFUL = ("COLORFUL", "彩色")

    class Type(models.IntegerChoices):  # Gear.Type.choices
        A = (0, "帽子/伏地挺身")
        B = (1, "手套/二頭彎舉")
        C = (2, "鞋子/深蹲")

    # primary_key = True in production
    token_id = models.PositiveIntegerField(unique=True, blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    level = models.CharField(choices=Level.choices, max_length=15, blank=True)
    type = models.IntegerField(choices=Type.choices, blank=True)
    loaded = models.BooleanField(default=False) #是否裝備
    color = models.CharField(choices=Color.choices, max_length=255, blank=True)
    work_max = models.IntegerField(blank=True, null=True)
    exp = models.FloatField(default=0, blank=True)
    lucky = models.FloatField(blank=True, null=True)
    coupon = models.CharField(max_length=255, blank=True, null=True)
    # status = models.IntegerField(blank=True, null=True) # use virtual property: is_exchangable, is_redeemed

    def __str__(self):
        return f"{self.user.username}_{self.pk}"

    @property
    def is_exchangable(self):
        return not self.is_redeemed and self.exp >= 0  # 待補滿級判斷邏輯

    @property
    def is_redeemed(self):
        return self.coupon != None

    class Meta:
        managed = True
        db_table = "gear"


class Exercise(models.Model):
    gear = models.ForeignKey(Gear, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accuracy = models.FloatField(default=0.0)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        managed = True
        db_table = "exercise"
        # unique_together = (("user", "timestamp"),) # use auto id

    def __str__(self):
        return f"{self.user.username}_{self.pk}"


class Thing(models.Model):
    class Level(models.TextChoices):
        BASIC = ("BASIC", "初級小物")
        INTERMEDIATE = ("INTERMEDIATE", "中級小物")
        HIGH_END = ("HIGH_END", "高級小物")

    level = models.CharField(choices=Level.choices, max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # directly record amount, easy to handle
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        managed = True
        db_table = "thing"
        unique_together = (("user", "level"),)

    def __str__(self):
        return f"{self.user.username}_{self.pk}"

class WeekTask(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="task"
    )
    week_start = models.DateField(auto_now=True)  # 记录每周任务开始日期
    count = models.PositiveIntegerField(default=0)  # 记录每周任务完成次数
    last_completed = models.DateField(null=True, blank=True)  # 记录用户上次完成任务的日期
    
    class Meta:
        managed = True


    def __str__(self):
        return f"{self.user.username}_{self.pk}"

