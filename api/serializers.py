from .models import Thing, Gear, Exercise
from rest_framework import serializers
from datetime import datetime, timedelta
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied, ValidationError
from rest_framework.response import Response


class ThingSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Thing
        fields = "__all__"


class GearSerializers(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    exp = serializers.FloatField(read_only=True)

    class Meta:
        model = Gear
        fields = "__all__"



class ExerciseSerializers(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.username")
    # user = serializers.SerializerMethodField()
    # def get_user(self, obj):
    #     return {"id": obj.user.id, "username": obj.user.username}
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # gear = serializers.SerializerMethodField(source="gear.type")
    thing_level = serializers.CharField(write_only=True, required=False)  # Add the thing_level field

    
    class Meta:
        model = Exercise
        fields = ['gear', 'timestamp', 'user', 'accuracy', 'count', 'thing_level']

    def create(self, validated_data):
            thing_level = validated_data.pop("thing_level", None)  # Remove thing_level from validated_data

            instance = super().create(validated_data)

            if thing_level:
                gear = instance.gear
                if gear.user != instance.user:
                    raise serializers.ValidationError("You are not allowed to modify this gear.")

                # Get the related Thing object (if any) for the current user and the specified thing_level
                thing = Thing.objects.filter(user=instance.user, level=thing_level).first() #BASIC, INTERMEDIATE, HIGH_END

                if thing:
                    # Check the level of the Thing and set the corresponding weight
                    if thing.level == Thing.Level.BASIC:
                        weight = 1.5
                        thing.amount -= 1
                    elif thing.level == Thing.Level.INTERMEDIATE:
                        weight = 2
                        thing.amount -= 1
                    else:
                        weight = 2.5
                        thing.amount -= 1
                    thing.save()
                else:
                    weight = 1

                today = datetime.now().date()
                today_last_count = Exercise.objects.filter(user=instance.user, timestamp__date=today).count()
                today_now_count = instance.count

                work_max = gear.work_max

                if today_last_count + today_now_count > work_max:
                    raise serializers.ValidationError({'message': 'You have already reached the maximum experience points for today.'})

                gear.exp += today_now_count * weight * instance.accuracy
                gear.save()

            return instance

