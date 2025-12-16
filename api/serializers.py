from rest_framework import serializers
from .models import Oqituvchi, TestStudent, OqituvchiTahrirlash, OqituvchiSMS, FirstTeacher, Guruh

class OqituvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oqituvchi
        fields = '__all__'


class TestStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestStudent
        fields = '__all__'


class OqituvchiTahrirlashSerializer(serializers.ModelSerializer):
    class Meta:
        model = OqituvchiTahrirlash
        fields = '__all__'


class OqituvchiSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = OqituvchiSMS
        fields = '__all__'


class GuruhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guruh
        fields = '__all__'


class FirstTeacherSerializer(serializers.ModelSerializer):
    guruhlar = GuruhSerializer(many=True, read_only=True)

    class Meta:
        model = FirstTeacher
        fields = '__all__'