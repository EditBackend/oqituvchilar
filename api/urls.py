from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OqituvchiViewSet, TestStudentViewSet, OqituvchiTahrirlashViewSet,OqituvchiSMSViewSet,FirstTeacherViewSet,GuruhViewSet,test_api


router = DefaultRouter()
router.register('oqituvchilar', OqituvchiViewSet)
router.register('test-studentlar', TestStudentViewSet)
router.register('oqituvchi-taxrirlash', OqituvchiTahrirlashViewSet)
router.register('oqituvchi-sms', OqituvchiSMSViewSet)
router.register('first-teacher', FirstTeacherViewSet)
router.register('guruh', GuruhViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('test/', test_api),
]
