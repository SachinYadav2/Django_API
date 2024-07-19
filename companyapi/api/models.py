from django.db import models

# Create your models here.


# created the Compnay class

class Company(models.Model):
    compnay_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    locations = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100 , choices=(("IT" , "IT") 
                                                      , ("None IT" , "None IT") ,
                                                        ("Mobile Phome","Mobile Phones")
                                                        ))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Method Overide so that companmy ka name show
    def __str__(self) -> str:
        return self.name

# Employeee Model Created


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email  = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    possition = models.CharField(max_length=50 , choices=(
        ("Manager" , "manager"),
        ("SDE" , 'sde'),
        ("Pr" , 'pr'),
    ))
    company = models.ForeignKey(Company , on_delete=models.CASCADE)




