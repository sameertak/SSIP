from rest_framework import serializers
from .models import responseModel

class FeedbackSerializers(serializers.ModelSerializer):
    res1 = serializers.CharField(max_length=50)
    res2 = serializers.CharField(max_length=50)
    res3 = serializers.CharField(max_length=300)
    res4 = serializers.CharField(max_length=1)

    class Meta:
        model = responseModel
        fields = ('__all__')