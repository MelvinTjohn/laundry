# Generated by Django 5.0.4 on 2024-07-03 09:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adminaddservices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('s_img', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
                ('categories', models.CharField(choices=[('Normal wash', 'Normal wash'), ('Normal wash+Iron', 'Normal wash+Iron'), ('Premium wash', 'premium wash')], default='Normal wash', max_length=100)),
                ('pieces', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='d_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=10)),
                ('l_name', models.CharField(max_length=15)),
                ('d_email', models.EmailField(max_length=254)),
                ('d_adrs', models.CharField(max_length=50)),
                ('d_phno', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=15)),
                ('d_photo', models.FileField(upload_to='')),
                ('d_lcnc', models.FileField(upload_to='')),
                ('biodata', models.FileField(upload_to='')),
                ('d_username', models.CharField(max_length=10, unique=True)),
                ('d_password', models.CharField(max_length=10)),
                ('d_pncd', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=15)),
                ('f_email', models.EmailField(max_length=254)),
                ('f_num', models.IntegerField()),
                ('f_feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='u_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('u_adrs', models.CharField(max_length=255)),
                ('pncd', models.CharField(max_length=6)),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('phonenumber', models.CharField(max_length=15)),
                ('u_img', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LAUND.u_register')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(default=datetime.datetime.today, null=True)),
                ('u_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('s_name', models.CharField(max_length=200)),
                ('s_price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('b_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('add_details', models.CharField(max_length=200)),
                ('total_price', models.IntegerField()),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Finished', 'Finished'), ('pending', 'pending'), ('Cancelled', 'Cancelled')], default='pending', max_length=150, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAUND.adminaddservices')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAUND.u_register')),
            ],
        ),
        migrations.CreateModel(
            name='booked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_name', models.CharField(max_length=500, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('number', models.IntegerField(null=True)),
                ('pin_code', models.IntegerField(null=True)),
                ('date', models.DateField(default=datetime.datetime.today, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('s_name', models.CharField(max_length=200, null=True)),
                ('s_price', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAUND.u_register')),
            ],
        ),
        migrations.CreateModel(
            name='u_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=200)),
                ('radio_c', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('s_name', models.CharField(max_length=200, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAUND.adminaddservices')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='LAUND.u_register')),
            ],
        ),
    ]
