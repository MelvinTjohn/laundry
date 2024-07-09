from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
class u_register(models.Model):
    u_name=models.CharField(max_length=15)
    email=models.EmailField(max_length=200,unique=True)
    u_adrs=models.CharField(max_length=255)
    pncd=models.CharField(max_length=6)
    username=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=15)
    phonenumber=models.CharField(max_length=15)
    u_img = models.FileField()

class d_register(models.Model):
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=15)
    d_email = models.EmailField()
    d_adrs = models.CharField(max_length=50)
    d_phno = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    d_photo = models.FileField()
    d_lcnc = models.FileField()
    biodata = models.FileField()
    d_username = models.CharField(max_length=10,unique=True)
    d_password = models.CharField(max_length=10)
    d_pncd=models.CharField(max_length=6)
class adminaddservices(models.Model):
    categorychoices=(
        ('Normal wash','Normal wash'),
        ('Normal wash+Iron','Normal wash+Iron'),
        ('Premium wash','premium wash'),
    )
    s_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    s_img=models.FileField()
    price=models.IntegerField()
    categories=models.CharField(max_length=100,default='Normal wash',choices=categorychoices)
    pieces = models.IntegerField(default=1)
    def __str__(self):
        return self.s_name





class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True,unique=True)
    customer = models.ForeignKey(u_register, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(adminaddservices, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.datetime.today, null=True)
    u_email = models.EmailField(null=True, blank=True)  # Allowing null and blank values
    pincode = models.CharField(max_length=6, null=True)  # Allowing null and blank values
    s_name = models.CharField(max_length=200)
    s_price = models.IntegerField()
    description = models.CharField(max_length=200)
    b_name = models.CharField(max_length=100, null=True, blank=True)  # Allowing null and blank values
    address = models.CharField(max_length=200, null=True, blank=True)  # Allowing null and blank values
    number = models.CharField(max_length=10, null=True, blank=True)  # Allowing null and blank values
    add_details = models.CharField(max_length=200)
    total_price = models.IntegerField()
    orderstatus = (
        ('Accepted', 'Accepted'),
        ('Finished', 'Finished'),
        ('pending', 'pending'),
        ('Cancelled', 'Cancelled')
    )
    status = models.CharField(max_length=150, choices=orderstatus, default='pending', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class Feedback(models.Model):
    f_name=models.CharField(max_length=15)
    f_email=models.EmailField()
    f_num=models.IntegerField()
    f_feedback=models.CharField(max_length=500)

class PasswordReset(models.Model):
    user=models.ForeignKey(u_register,on_delete=models.CASCADE)
    #security
    token=models.CharField(max_length=4)
class u_review(models.Model):
    user = models.ForeignKey(u_register, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(adminaddservices, on_delete=models.CASCADE, null=True)
    Message= models.CharField(max_length=200)
    radio_c=models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    user_name = models.CharField(max_length=200,null=True)
    s_name = models.CharField(max_length=200,null=True)
    number = models.CharField(max_length=10, null=True, blank=True)

class booked(models.Model):
    # booked_id = models.IntegerField()
    customer = models.ForeignKey(u_register, on_delete=models.CASCADE, null=True)
    booked_name= models.CharField(max_length=500,null=True)
    email = models.EmailField(max_length=200,null=True)
    address = models.CharField(max_length=500,null=True)
    number = models.IntegerField(null=True)
    pin_code = models.IntegerField(null=True)
    date = models.DateField(default=datetime.datetime.today, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    s_name = models.CharField(max_length=200, null=True)
    s_price = models.IntegerField(null=True)


