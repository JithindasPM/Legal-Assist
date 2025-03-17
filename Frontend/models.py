from django.db import models

class LawyerDb(models.Model):
    Name = models.TextField(max_length=25, null=True, blank=True)
    Qualification = models.TextField(max_length=25, null=True, blank=True)
    EmailID = models.EmailField(max_length=25, null=True, blank=True)
    Specialization = models.TextField(max_length=25, null=True, blank=True)
    Username = models.TextField(max_length=25, null=True, blank=True)
    Password = models.TextField(max_length=25, null=True, blank=True)
    payment = models.IntegerField(null=True, blank=True)
    Mob_No = models.IntegerField(null=True, blank=True)
    Appointment_time = models.TimeField(null=True, blank=True)
    Image = models.ImageField(upload_to="Lawyer_images", null=True, blank=True)
    is_approved = models.BooleanField(default=False)  # New field for approval status

    def __str__(self):
        return self.Name

class UserDb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    EmailId=models.EmailField(max_length=50,null=True,blank=True)
    Phn_No=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    password=models.CharField(max_length=50,null=True,blank=True)

class CustomerRequest(models.Model):
    user=models.ForeignKey(UserDb,on_delete=models.CASCADE)
    lawyer=models.ForeignKey(LawyerDb,on_delete=models.CASCADE)
    acces=models.BooleanField(default=False)

