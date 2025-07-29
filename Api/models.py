from django.db import models # type: ignore

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100,choices=(
                           ('IT','IT'),
                           ('Non IT','Non IT'),
                           ('Product-Based','Product-Based')
                           ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + '--' + self.location
    
class Empolyee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(choices=(('Manager','manager'),
        ('Software Developer','sd'),
        ('Project Leader','pl'))
        )
    # This will basically help us to create the 1-Many relationship between company and employee
    company = models.ForeignKey(Company,on_delete=models.CASCADE)