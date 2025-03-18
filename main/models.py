from django.db import models

class Therapist(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=150)
    message = models.TextField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.specialization}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message de {self.name} ({self.email})"


class Questionnaire(models.Model):
    q1 = models.CharField(max_length=400)
    q2 = models.CharField(max_length=500)
    q3 = models.CharField(max_length=500)
    q4 = models.CharField(max_length=500)
    q5 = models.TextField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.CharField(max_length=555)
    q9 = models.CharField(max_length=500)

    def __str__(self):
        return f"Questionnaire #{self.id}"
