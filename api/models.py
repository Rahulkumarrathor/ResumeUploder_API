from django.db import models

# Create your models here.
STATE_CHOICE = ((
    ('Bihar', 'Bihar'),
    ('Jharkhand', 'Jharkhand'),
    ('west Bengal', 'west Bengal'),
                ))
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='pimage', blank=True)
    pfile = models.FileField(upload_to='pfile', blank=True)

    def __str__(self):
        return self.name