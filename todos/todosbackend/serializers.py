from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=20)
    body = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)
    """

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.title)

        instance.save()
        return instance
    """

    class Meta:
        model = Todo
        fields = ('id', 'title', 'body', 'isDone')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
