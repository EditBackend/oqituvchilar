from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Oqituvchi, TestStudent, OqituvchiTahrirlash, OqituvchiSMS, Guruh, FirstTeacher
from .serializers import OqituvchiSerializer, TestStudentSerializer, OqituvchiTahrirlashSerializer, OqituvchiSMSSerializer, GuruhSerializer,FirstTeacherSerializer


@api_view(['GET'])
def test_api(request):
    return Response({"msg": "Swagger ishlayapti"})

class OqituvchiViewSet(ModelViewSet):
    queryset = Oqituvchi.objects.all()
    serializer_class = OqituvchiSerializer


class TestStudentViewSet(ModelViewSet):
    queryset = TestStudent.objects.all()
    serializer_class = TestStudentSerializer


class OqituvchiTahrirlashViewSet(ModelViewSet):
    queryset = OqituvchiTahrirlash.objects.all()
    serializer_class = OqituvchiTahrirlashSerializer


class OqituvchiSMSViewSet(ModelViewSet):
    queryset = OqituvchiSMS.objects.all()
    serializer_class = OqituvchiSMSSerializer


class FirstTeacherViewSet(ModelViewSet):
    queryset = FirstTeacher.objects.all()
    serializer_class = FirstTeacherSerializer


class GuruhViewSet(ModelViewSet):
    queryset = Guruh.objects.all()
    serializer_class = GuruhSerializer