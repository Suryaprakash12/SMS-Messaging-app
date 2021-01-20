from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
# Create your models here.
class Dialer(models.Model):
    name=models.CharField(max_length=100)
    phone=PhoneNumberField()
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.phone)

    def get_absolute_url(self):
        return reverse('message:send-message',kwargs={'pk':self.pk})

