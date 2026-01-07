from django.contrib import admin
from .models import Oqituvchi, TestStudent, OqituvchiTahrirlash, OqituvchiSMS,FirstTeacher, Guruh
from .serializers import FirstTeacherSerializer

admin.site.register(Oqituvchi)
admin.site.register(TestStudent)
admin.site.register(OqituvchiTahrirlash)
admin.site.register(OqituvchiSMS)
admin.site.register(FirstTeacher)
admin.site.register(Guruh)
