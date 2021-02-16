from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return self.user.username

    # we override 'save' method
    # we will make profile pictures smaller in order to make browser faster
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_img.path)

        if img.height > 250 or img.width > 250:
            new_size = (250, 250)
            img.thumbnail(new_size)
            img.save(self.profile_img.path)


