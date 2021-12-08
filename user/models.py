from django.db import models


class Login(models.Model):
    name = models.CharField(max_length=155)
    username = models.CharField(max_length=155)
    email = models.EmailField(max_length=155)
    password = models.CharField(max_length=155)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["id"]

