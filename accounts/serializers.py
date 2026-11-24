from rest_framework import serializers

from accounts.models import User,TutorProfile

class TutorSerializer(serializers.ModelSerializer):

    class Meta :

        model= User
        fields=["id","username","email","password","phone","role"]
        read_only_fields=["id","role"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data,role='tutor')


class TutorProfileSerializer(serializers.ModelSerializer):

    class Meta :
        model= TutorProfile
        fields='__all__'
        read_only_fields= ["id","user","created_at","updated_at"]