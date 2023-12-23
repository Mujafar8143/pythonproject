from django.db import models

# Create your models here.
class Employee(models.Model):
    #id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    number=models.IntegerField()
    gender=models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.name








