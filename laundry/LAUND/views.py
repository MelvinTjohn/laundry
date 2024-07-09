from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponse
from .models import *
from collections import defaultdict
from django.template import loader
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.db import IntegrityError
from .forms import *
import datetime
import re

# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
import os

def loginindex(request):
    return render(request,'loginindex.html')
def index(re):
    return render(re,'index.html')
def home(re):
    return render(re,'index.html')
def services(re):
    return render(re,'services.html')
def about(re):
    data = Feedback.objects.all()
    return render(re, 'about.html', {'d': data})
def contact(re):
    return render(re,'contact.html')
def admin(re):
    return render(re,'admin.html')
def employee(re):
    return render(re,'employee.html')
def adminviewuser(re):
    if 'aid' in re.session:
        data=u_register.objects.all()
        return render(re,'adminviewuser.html',{'d':data})
    return redirect(admin)
def adminviewemployee(re):
    if 'aid' in re.session:
        data=d_register.objects.all()
        return render(re,'adminviewemployee.html',{'d':data})
    return redirect(admin)
# def adminaddservicess(re):
#     return render(re,'adminaddservices.html')
def adminviewwork(re):
    if 'aid' in re.session:
        data=Booking.objects.all()
        return render(re,'adminviewwork.html',{'d':data})
    return render(admin)
def statusup(re, wal):
    if re.method == "POST":
        st = Booking.objects.get(booking_id=wal)
        st.status = re.POST.get('status')
        st.save()
    return redirect(adminviewwork)

def adminviewservices(re):
    if 'aid' in re.session:
        data=adminaddservices.objects.all()
        return render(re,'adminviewservices.html',{'d':data})
    return redirect(admin)
def adminaddemployee(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        e_email = request.POST['e_mail']
        e_phno = request.POST['ph_no']
        location = request.POST['loc']
        e_img = request.FILES['e_img']
        e_bio = request.FILES['e_bio']
        e_licence = request.FILES['e_lic']
        e_usname = request.POST['us_name']
        e_password = request.POST['pass']
        e_pncd = request.POST['e_pincode']
        uadrs = request.POST['e_adrs']
        try:
            d = d_register.objects.get(d_username=e_usname)
            if d is not None:
                messages.error(request, 'username Already Exists')
        except Exception:
            d = d_register.objects.create(f_name=f_name,d_email=e_email, d_adrs=uadrs, d_pncd=e_pncd,
                                          d_phno=e_phno, d_username=e_usname, location=location, d_photo=e_img,
                                          biodata=e_bio, d_lcnc=e_licence, d_password=e_password)
            d.save()
            messages.success(request, 'Employee added successfully')
            return redirect(adminaddemployee)
    return render(request, 'adminaddemployee.html')
def adminviewcustomerreview(re):
    if 'aid' in re.session:
        data=Feedback.objects.all()
        return render(re,'adminviewcustomerreview.html',{'d':data})
    return redirect(admin)
def employeeviewuser(re):
    return render(re,'employeeviewuser.html')
def employeevieworder(re):
    return render(re,'employeevieworder.html')
def user(re):
    return render(re,'user.html')
def userhome(re):
    return render(re,'user.html')
def userabout(re):
    return render(re,'userabout.html')
def userservices(re):
    if 'aid' in re.session:
        data=adminaddservices.objects.all()
        return render(re,'userservices.html',{'d':data})
    return redirect(user)
def usercontact(re):
    return render(re,'usercontact.html')
def userprofile(re):
    return render(re,'userprofile.html')
def logout(re):
    return render(re,'logout.html')
def indexbook(re):
    return render(re,'indexbook.html')

def u_reg(request):
        if request.method == 'POST':
            uname = request.POST['uname']
            email = request.POST['email']
            uadrs = request.POST['adrs']
            pncd = request.POST['pincode']
            uphno = request.POST['nmbr']
            usname = request.POST['usname']
            pwd = request.POST['password']
            u_img = request.POST['dimg']

            if len(pwd) < 8:
                messages.error(request, "Password must be at least 8 characters long")
                return render(request, 'loginindex.html')

            special_char_pattern = r'[!@#$%^&*()_+=\-[\]{};:\'"\\|,.<>/?]'
            alph_pattern = r'[A-Za-z]'
            number_pattern = r'[0-9]'

            if not re.search(special_char_pattern, pwd):
                messages.error(request, "Password must contain at least one special character")
                return render(request, 'loginindex.html')

            if not re.search(alph_pattern, pwd):
                messages.error(request, "Password must contain at least one uppercase letter")
                return render(request, 'loginindex.html')

            if not re.search(number_pattern, pwd):
                messages.error(request, "Password must contain at least one number")
                return render(request, 'loginindex.html')
            try:
                u = u_register.objects.get(username=usname)
                if u is not None:
                    messages.error(request, 'username Already Exists')
                    return render(request,'loginindex.html')
            except u_register.DoesNotExist:
                try:
                    u = u_register.objects.create(u_name=uname, email=email, u_adrs=uadrs, pncd=pncd, phonenumber=uphno,
                                                  username=usname, password=pwd, u_img=u_img)
                    u.save()
                    messages.success(request, 'Your profile details added successfully')
                except IntegrityError:
                    messages.error(request, 'Email already exists')
                    return render(request, 'loginindex.html')

            return render(request, 'loginindex.html')

        #     except Exception:
        #         u = u_register.objects.create(u_name=uname, email=email, u_adrs=uadrs, pncd=pncd, phonenumber=uphno,
        #                                       username=usname, password=pwd, u_img=u_img)
        #         u.save()
        #         messages.success(request, 'your profile Details added successfully')
        # return render(request, 'loginindex.html')
def login(re):
    if re.method=='POST':
        username=re.POST['usname']
        password=re.POST['password']
        try:
            data=u_register.objects.get(username=username)
            if username==data.username and password==data.password:
                re.session['uid']=username
                return redirect(user)

            else:
                messages.error(re,'Invalid Username or Password')
        except:
            try:
                data = d_register.objects.get(d_username=username)
                if username == data.d_username and password == data.d_password:
                    re.session['did'] = username
                    return redirect(employee)
                else:
                    messages.error(re,'Invalid Username or Password')
            except Exception:
                if username == 'admin' and password == 'admin':
                    re.session['aid'] = username
                    return redirect(admin)
                else:
                    messages.error(re,'Invalid Username or Password')
                return render(re,'dlogin.html')

    return render(re, 'loginindex.html')
def dlogin(re):
    return render(re,'dlogin.html')
def delboy_reg(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        d_email=request.POST['d_email']
        d_adrs=request.POST['d_adrs']
        d_phno=request.POST['d_nmbr']
        location=request.POST['location']
        d_img=request.FILES['dimg']
        d_bio=request.FILES['d_bio']
        d_licence=request.FILES['d_lcnce']
        d_usname=request.POST['d_usname']
        d_password=request.POST['d_password']
        d_pncd=request.POST['d_pincode']
        try:
            d=d_register.objects.get(d_username=d_usname)
            if d is not None:
                messages.error(request,'username Already Exists')
        except Exception:
            d=d_register.objects.create(f_name=fname,l_name=lname,d_email=d_email,d_adrs=d_adrs,d_pncd=d_pncd,d_phno=d_phno,d_username= d_usname,location=location,d_photo=d_img,biodata=d_bio,d_lcnc=d_licence,d_password=d_password)
            d.save()
            messages.success(request,'profile details added successfully')
    return render(request,'dlogin.html')
def addservices(re):
    if re.method == 'POST':
        s_name = re.POST['s_name']
        price = re.POST['price']
        description = re.POST['description']
        catogaries = re.POST['category']
        s_img = re.FILES['s_img']
        upload = adminaddservices.objects.create(s_img=s_img, price=price, s_name=s_name, description=description,
                                                     categories=catogaries)
        upload.save()
        messages.success(re, 'Added Successfully')
    return render(re, 'adminaddservices.html')
def edit(re,id):
    if'aid' in re.session:
        data = adminaddservices.objects.get(pk=id)
        return render(re, 'edit.html', {'d': data})
def updating(re, id):
    if 'aid' in re.session:
        if re.method == 'POST':
            s_name = re.POST['cs_name']
            price = re.POST['c_price']
            description = re.POST['cdescription']
            # catogaries = re.POST['ccategory']
            # s_img = re.FILES['cs_img']
            adminaddservices.objects.filter(pk=id).update(s_name=s_name, description=description, price=price)
            return redirect(adminviewservices)
        return render(re, 'edit.html')
def delete(re, id):
    if 'aid' in re.session:
        data = adminaddservices.objects.get(pk=id)
        data.delete()
        messages.success(re, 'Services Deleted')
        return redirect(adminviewservices)
def user_feedback(re):
    if 'uid' in re.session:
        if re.method == 'POST':
            name = re.POST['Name']
            fmail = re.POST['email']
            phone = re.POST['phno']
            msg = re.POST['Message']
            feedback=Feedback.objects.create(f_name=name,f_email=fmail,f_num=phone,f_feedback=msg)
            feedback.save()
            messages.success(re,'...Feedback Submitted Successfully...','THANK YOU FOR YOUR FEEDBACK')
        return render(re, 'usercontact.html')
    return redirect(user)
def fdelete(re,id):
    if 'aid' in re.session:
        data = Feedback.objects.get(pk=id)
        data.delete()
        messages.success(re, 'Services Deleted')
        return redirect(adminviewcustomerreview)
def usr_profile(re):
    if 'uid' in re.session:
        u = u_register.objects.get(username=re.session['uid'])
        return render(re,'userprofile.html',{'d':u})
    return redirect(userhome)

def pro_edit(re,id):
    if 'uid' in re.session:
        u = u_register.objects.get(pk=id)
        if re.method == 'POST':
            u.u_name = re.POST['name']
            u.email = re.POST['email']
            u.u_phno = re.POST['nmbr']
            u.u_address = re.POST['adrss']
            # u.u_district = re.POST['udistrict']
            # u.u_city = re.POST['ucity']
            u.u_pincode  = re.POST['upincode']
            try:
                u.u_img = re.FILES['user_img']
                import os
                os.remove()
                u.save()
            except:
                u.save()
                return redirect(update_profile,id)
        return render(re,'userprofile.html',{'d':u})


def update_profile(re,id):
    if 'uid' in re.session:
        if re.method == 'POST':
            form=UserProfileForm(re.POST,re.FILES)
            if form.is_valid():
                a = form.cleaned_data['name']
                b = form.cleaned_data['email']
                c = form.cleaned_data['nmbr']
                d = form.cleaned_data['adrss']
                g = form.cleaned_data['user_img']
                h= form.cleaned_data['upincode']
                u_register.objects.filter(pk=id).update(u_name=a,email=b,phonenumber=c,u_adrs=d,u_img=g,pncd=h)
                messages.success(re,'...Profile Updated Successfully...')
                return redirect(usr_profile)
            data = u_register.objects.all()
            return render(re,'userprofile.html',{'d':data})
            form=UserProfileForm()
            return render(re,'userprofile.html',{'form':form})
        return redirect(usr_profile)
def vedelete(re,id):
    if 'aid' in re.session:
        data =d_register.objects.get(pk=id)
        data.delete()
        messages.success(re, 'Services Deleted')
        return redirect(adminviewemployee)
# def bookingservice(re):
#     return render(re,'bookingservice.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = u_register.objects.get(email=email)
        except:
            messages.info(request,"Email id not registered")
            return redirect(forgot_password)
        # Generate and save a unique token
        token = get_random_string(length=4)
        PasswordReset.objects.create(user=user, token=token)

        # Send email with reset link
        reset_link = f'http://127.0.0.1:8000/reset/{token}'
        try:
            send_mail('Reset Your Password', f'Click the link to reset your password: {reset_link}','settings.EMAIL_HOST_USER', [email],fail_silently=False)
            # return render(request, 'emailsent.html')
        except:
            messages.info(request,"Network connection failed")
            return redirect(forgot_password)

    return render(request, 'frgt.html')
def reset_password(request, token):
    # Verify token and reset the password
    print(token)
    password_reset = PasswordReset.objects.get(token=token)
    # usr = User.objects.get(id=password_reset.user_id)
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        repeat_password = request.POST.get('cpassword')
        if repeat_password == new_password:
            password_reset.user.password=new_password
            password_reset.user.save()
            # password_reset.delete()
            return redirect(login)
    return render(request, 'rest-pass.html',{'token':token})

def book(re,id):
    if 'uid' in re.session:
        u = u_register.objects.get(username=re.session['uid'])
        s=adminaddservices.objects.get(pk=id)
        return render(re, 'bookingservice.html', {'user': u, 'd': s})
    return redirect(userhome)


def single_razor(request,id):
    # Fetch the service and user objects or return a 404 error if not found
    service = get_object_or_404(adminaddservices, pk=id)
    s=request.session.get('uid')
    user = get_object_or_404(u_register, username=s)



    if request.method == "POST":
        # Retrieve form data from the POST request
        name = user.u_name
        address = user.u_adrs
        email = user.email
        number = user.phonenumber
        pin_code = user.pncd
        s_name = request.POST.get('s_name')
        s_price = request.POST.get('price')
        date = request.POST.get('booking_date')
        total_amount = request.POST.get('total')
        details = request.POST.get('add_details')
        description = request.POST.get('description')

        # Create a new booking instance
        booking = Booking.objects.create(
            service=service,
            customer=user,
            u_email=email,
            pincode=pin_code,
            s_name=s_name,
            s_price=s_price,
            date=date,
            total_price=total_amount,
            add_details=details,
            description=description,
            b_name=name,
            address=address,
            number=number
        )

        # Save the booking instance to the database
        booking.save()

        # Add a success message
        # messages.success(request, 'Booking request sent')

        # Redirect to the user view order page
        return redirect(uservieworder)

    # Redirect to the user services page if the request method is not POST
    return redirect(userservices)


def uservieworder(re):
    if 'uid' in re.session:
        u = Booking.objects.all()
        return render(re, 'uservieworder.html', {'d': u})
    return render(re,'uservieworder.html')


def send_review_form(re,id):
    if 'uid' in re.session:
        u = u_register.objects.get(username=re.session['uid'])
        s = Booking.objects.get(pk=id)
        return render(re, 'send_reviews.html', {'user': u,'s': s})
def send_reviews(re,id):
    if 'uid' in re.session:
        u = get_object_or_404(Booking, pk=id)  # Get a single service based on the provided ID
        s=adminaddservices.objects.all()
        if re.method == 'POST':
            email = re.POST['email']
            Message = re.POST['Message']
            radio_c = re.POST['select5']
            user_name = re.POST['Name']
            s.s_name = re.POST.get('s_name')
            number = re.POST.get('number')
            data = u_review(s_name=s.s_name, email=email, radio_c=radio_c, Message=Message, user_name=user_name)
            data.save()
            return redirect(show_reviews)  # Use the name of the view
    return render(re, 'send_reviews.html')
    # return render(re, 'send_reviews.html')
    # return render(re, 'send_reviews.html', {'s)
def show_reviews(re):
    Very_Bad = 0
    Bad = 0
    Very_Good = 0
    Good = 0
    Excellent = 0
    l = []

    # Retrieve all items from u_review model
    items = u_review.objects.all()

    # Count occurrences of each rating category
    for i in items:
        if i.radio_c == 'Very Bad':
            Very_Bad += 1
        elif i.radio_c == 'Bad':
            Bad += 1
        elif i.radio_c == 'Very Good':
            Very_Good += 1
        elif i.radio_c == 'Good':
            Good += 1
        elif i.radio_c == 'Excellent':
            Excellent += 1
    for i in items:
        l.append(i.radio_c)

    d = u_review.objects.all()
    return render(re,'show_reviews.html',{'user1':d,
        'Vb': Very_Bad,
        'Bd': Bad,
        'Vg': Very_Good,
        'Gd': Good,
        'Ex': Excellent,})

def payment(request,s_price,pk):
    if 'uid' in request.session:
        u = u_register.objects.get(username=request.session['uid'])
        s = Booking.objects.filter(b_name=u)
        f=adminaddservices.objects.all()
        t=s_price*100


        return render(request, "payment.html", {'amount':t,'pk':pk})
    return render(request, "payment.html")

def u_booking(re):
    data = Booking.objects.all()
    return render(re, 'bookingservice.html', {'d': data})


def u_bookreq_cancel(re,id):
    if 'uid' in re.session:
        data = Booking.objects.get(pk=id)
        data.delete()
    return redirect(uservieworder)



def razor(re):
    return render(re, "payment.html")

def razorpaycheck(request, s_price):
    if 'uid' in request.session:
        u = u_register.objects.get(user_name=request.session['uid'])
        s = Booking.objects.filter(name=u)
        t = s_price * 100
        return render(request, "payment.html", {'amount': t})

    return redirect(razor)

def success(re,id):
    if 'uid' in re.session:
        data = Booking.objects.get(pk=id)
        a = booked.objects.create(booked_name=data.b_name,
                                            # booked_id=data.booking_id,
                                            email=data.u_email,
                                            address=data.address,
                                            number=data.number,
                                            s_name=data.s_name,
                                            s_price=data.s_price,
                                            # customer=data,
                                            pin_code=data.pincode,
                                            date=data.date)
        a.save()
        # v=booked.objects.all()
        return render(re,'success.html')
def bookingdetails(re):
    if 'uid' in re.session:
        v=booked.objects.all()
        return render(re, 'bookingdetails.html', {'c': v})
    return render(re, 'bookingdetails.html')
def adminpaymentdetails(re):
    if 'uid' in re.session:
        v=booked.objects.all()
        return render(re, 'adminviewpaymentdetails.html', {'c': v})
    return render(re, 'adminviewpaymentdetails.html')