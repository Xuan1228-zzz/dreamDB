from django.contrib import admin
# Register your models here.
# from .models import UserInfo
# admin.site.register(UserInfo)

from .models import Eq
admin.site.register(Eq)

from .models import Exercise
admin.site.register(Exercise)

from .models import Thing
admin.site.register(Thing)

from .models import User
admin.site.register(User)

