from rest_framework.serializers import ModelSerializer

from api.models import Todo


class TodoSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = [
            'id',
            'text',
            'done'
        ]
