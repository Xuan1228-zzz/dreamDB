from django.contrib import admin
from .models import Thing, Gear, Exercise, WeekTask


# Register your models here.
class GearInline(admin.StackedInline):  # admin.TabularInline
    model = Gear
    extra = 1


class GearAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "token_id",
        "user",
        "level",
        "type",
        "loaded",
        "color",
        "work_max",
        "exp",
        "lucky",
        "coupon",
    ]


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["user", "gear", "timestamp", "count", "accuracy"]
    

class ThingAdmin(admin.ModelAdmin):
    list_display = ["user", "level", "amount"]


class WeekTaskAdmin(admin.ModelAdmin):
    list_display = ["user", "week_start", "count","last_completed"]


admin.site.register(Gear, GearAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Thing, ThingAdmin)
admin.site.register(WeekTask, WeekTaskAdmin)