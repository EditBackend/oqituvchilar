from django.db import models

# Create your models here.

class Oqituvchi(models.Model):
    ismi = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    guruhlar_soni = models.IntegerField()
    oqituvchilar_miqdori = models.IntegerField()

    def __str__(self):
        return self.ismi


class TestStudent(models.Model):
    ismi = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    guruhlar_soni = models.IntegerField()

    def __str__(self):
        return self.ismi


class OqituvchiTahrirlash(models.Model):
    JINSI_TANLOV = [
        ('erkak', 'Erkak'),
        ('ayol', 'Ayol'),
    ]

    ismi = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    tugilgan_sana = models.DateField()
    jinsi = models.CharField(max_length=10, choices=JINSI_TANLOV)
    foto = models.ImageField(upload_to='oqituvchilar/', null=True, blank=True)
    parol = models.CharField(max_length=128)

    def __str__(self):
        return self.ismi


class OqituvchiSMS(models.Model):
    oqituvchi = models.ForeignKey('Oqituvchi', on_delete=models.CASCADE, related_name='smslar')
    sms_matni = models.TextField()  # cheksiz yozish imkoniyati

    def __str__(self):
        return f"{self.oqituvchi.ismi} ga SMS"


class FirstTeacher(models.Model):
    telefon = models.CharField(max_length=13)
    rollari = models.CharField(max_length=100)
    filliallari = models.CharField(max_length=100)

    def __str__(self):
        return self.telefon


class Guruh(models.Model):
    first_teacher = models.ForeignKey(FirstTeacher, on_delete=models.CASCADE, related_name='guruhlar')
    qaysi_kursligi = models.CharField(max_length=100)
    boshlash_sanasi = models.DateField()
    tugash_sanasi = models.DateField()
    toq_kunlar = models.CharField(max_length=50)

    def __str__(self):
        return self.qaysi_kursligi