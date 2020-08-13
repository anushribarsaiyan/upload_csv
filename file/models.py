from django.db import models

# Create your models here.
class Contract(models.Model):
    first_name=models.CharField(max_length=3)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    id_address=models.GenericIPAddressField(null=True)
    message=models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

