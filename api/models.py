from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    # slug = models.SlugField(default="", null=False)

    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"
