from django.contrib.auth.models import User
from rest_framework import serializers

class SignUp(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
    )

    class Meta:
        model = User
        fields = ["username", "password"]

    def validate_username(self, value):
        if value in User.objects.values_list("username", flat=True):
            raise serializers.ValidationError("Username already taken")
        return value

    def create(self, validated_data):
        return User.objects.create_user(
        username=validated_data['username'],
        password=validated_data['password'],
    )

    def update(self, instance, validated_data):
        if "username" in validated_data:
            instance.username = validated_data["username"]
        if "password" in validated_data:
            instance.set_password(validated_data["password"])

        instance.save()
