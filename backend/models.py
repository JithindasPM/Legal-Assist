from django.db import models

# Create your models here.

class LegalDb(models.Model):
    LegalTypes = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.TextField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="legalimages", null=True, blank=True)
class CompanyDb(models.Model):
    Desc_cmpny = models.TextField(max_length=50, null=True, blank=True)
    Comp_Image = models.ImageField(upload_to="Company media", null=True, blank=True)
    ContactNo = models.TextField(max_length=10,null=True, blank=True)
    Address = models.TextField(max_length=50, null=True, blank=True)