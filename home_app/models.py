from django.db import models

# Create your models here.
class Home(models.Model):
    owner_first_name = models.CharField(max_length=255, null=False)
    owner_last_name = models.CharField(max_length=255, null=False)
    address_line_1 = models.CharField(max_length=255, null=False)
    postcode = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.owner_first_name
        
    def owner_full_name(self):
        full_name =self.owner_first_name + self.owner_last_name
        return full_name
