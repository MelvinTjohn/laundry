from django import forms
from.models import*


class UserProfileForm(forms.Form):
    u_name = models.CharField(max_length=20)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    u_img = models.FileField()
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    u_adrs = models.CharField(max_length=100)
    u_pncd = models.IntegerField()
