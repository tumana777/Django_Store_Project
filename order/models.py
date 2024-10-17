from django.db import models

class UserCart(models.Model):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} cart"