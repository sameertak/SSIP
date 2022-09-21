from rest_framework import serializers
from .models import responseModel

class FeedbackSerializers(serializers.ModelSerializer):
    res1 = serializers.CharField(max_length=1)
    res2 = serializers.CharField(max_length=1)
    res3 = serializers.CharField(max_length=200)

    class Meta:
        model = responseModel
        fields = ('__all__')