from django.shortcuts import render, redirect
from backend.models import LegalDb, CompanyDb
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ValidationError
from Frontend.views import LawyerDb
from django.utils.dateparse import parse_time

# Create your views here.

def index_page(request):
    return render(request,"index.html")

def add_legal_ent(request):
    return render(request,"add_legal_entities.html")

def save_legal_ent(request):
    if request.method == "POST":
        legal_typ = request.POST.get('legal_types')
        price = request.POST.get('price')
        description = request.POST.get('Description')

        try:
            img = request.FILES['image']
            # Validate file size, type, etc. if needed
        except KeyError:
            # Handle the case where no image is provided
            messages.error(request, "No image provided")
            return redirect(add_legal_ent)

        try:
            obj = LegalDb.objects.create(
                LegalTypes=legal_typ,
                Price=price,
                Description=description,
                Image=img
            )
            messages.success(request, "Legal entity added successfully")
            return redirect(add_legal_ent)
        except ValidationError as e:
            # Handle validation errors
            messages.error(request, f"Validation error: {e}")
            return redirect(add_legal_ent)
        except Exception as e:
            # Handle other unexpected errors
            messages.error(request, f"An error occurred: {e}")
            return redirect(add_legal_ent)

def display_legal_ent(request):
    legal = LegalDb.objects.all()
    return render(request, "display_legal_details.html",{'legal':legal})
def edit_legal(request,legalid):
    data = LegalDb.objects.get(id=legalid)
    return render(request,"Edit_legal.html",{'data':data})
def update_legal(request, updateid):
    if request.method == "POST":
        lg_typ = request.POST.get('legal_types')
        prc = request.POST.get('price')
        des = request.POST.get('Description')

        try:
            pic = request.FILES['image']
            fs = FileSystemStorage()
            doc = fs.save(pic.name, pic)
        except MultiValueDictKeyError:
            doc = LegalDb.objects.get(id=updateid).Image
        except ValidationError as e:
            messages.error(request, f"Validation error: {e}")
            return redirect(display_legal_ent)
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect(display_legal_ent)

        try:
            LegalDb.objects.filter(id=updateid).update(
                LegalTypes=lg_typ,
                Price=prc,
                Description=des,
                Image=doc
            )
            messages.success(request, "Edited Legal Details Successfully")
            return redirect(display_legal_ent)
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect(display_legal_ent)

def de_l_legal(request,delid):
    var = LegalDb.objects.filter(id=delid)
    var.delete()
    messages.error(request,"legal details deleted Successfully")
    return redirect(display_legal_ent)
def admin_log_page(request):
    return render(request, "Admin_login.html")
def adminlogin(request):
    if request.method == "POST":
        usn = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if User.objects.filter(username__contains=usn).exists():
            x = authenticate(username=usn,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=usn
                request.session['password']=pwd
                messages.success(request,"Admin Logged Successfully")
                return redirect(index_page)
            else:
                messages.success(request, "Error username or password")
                return redirect(admin_log_page)
        else:
            return redirect(admin_log_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Admin logged Out Successfully")
    return redirect('homepage')

def add_comp_det(request):
    return render(request,"add_company_det.html")

def save_comp_det(request):
    if request.method == "POST":
        desc = request.POST.get('description')
        img = request.FILES['comp_img']
        con = request.POST.get('telephone_number')
        addr = request.POST.get('Address')
        obj = CompanyDb(Desc_cmpny=desc, Comp_Image=img, ContactNo=con, Address=addr)
        obj.save()
        messages.success(request,"Company Details added successfully")
        return redirect(add_comp_det)

def disp_comp_det(request):
    comp = CompanyDb.objects.all()
    return render(request,"Display_Company_Details.html",{'comp':comp})

def edit_comp(request,compid):
    info = CompanyDb.objects.get(id=compid)
    return render(request, "Edit_comp_det.html", {'info':info})

def update_comp(request,upid):
    if request.method=="POST":
        des = request.POST.get("description")
        cn = request.POST.get("telephone_number")
        add = request.POST.get("Address")
        try:
            im= request.FILES['comp_img']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = CompanyDb.objects.get(id=upid).Comp_Image
        CompanyDb.objects.filter(id=upid).update(Desc_cmpny=des,Comp_Image=file,ContactNo=cn,Address=add)
        messages.success(request, "Company Details Edited Successfully")
        return redirect(disp_comp_det)

def delete_comp(request,cncid):
    can = CompanyDb.objects.get(id=cncid)
    can.delete()
    messages.error(request,"Company Details Deleted Successfully")
    return redirect(disp_comp_det)
def display_lawyer(request):
    law = LawyerDb.objects.all()
    return render(request, "lawyerdisplay.html",{'law':law})

def edit_lawyer(request,lawyerid):
    lawyer = LawyerDb.objects.get(id=lawyerid)
    return render(request, "editlawyer.html",{'lawyer':lawyer})


# def update_lawyer(request, updid):
#     if request.method == "POST":
#         Nam = request.POST.get('name')
#         ql = request.POST.get('Qualification')
#         ema = request.POST.get('EmailID')
#         spc = request.POST.get('Specialization')
#         us = request.POST.get('Username')
#         ap = request.POST.get('Appointment_Time')
#         nm = request.POST.get('Mob_num')
#         py = request.POST.get('pay')

#         # Retrieve the value of approval status
#         is_approved = request.POST.get(
#             'approval') == 'approve'  # Assuming the form has 'approval' field with values 'approve' or 'reject'

#         try:
#             imo = request.FILES['image']
#             fs = FileSystemStorage()
#             file = fs.save(imo.name, imo)
#         except MultiValueDictKeyError:
#             file = LawyerDb.objects.get(id=updid).Image

#         # Check if Appointment time is provided, if not retain the existing value
#         existing_ap = LawyerDb.objects.get(id=updid).Appointment_time
#         if ap is None:
#             ap = existing_ap

#         # Update LawyerDb object with new values
#         LawyerDb.objects.filter(id=updid).update(
#             Name=Nam,
#             Qualification=ql,
#             EmailID=ema,
#             Specialization=spc,
#             Username=us,
#             Appointment_time=ap,
#             is_approved=is_approved,  # Assign the boolean value here
#             Image=file,
#             payment=py,
#             Mob_No=nm
#         )

#         messages.success(request, "Lawyer Details Edited Successfully")
#         return redirect(display_lawyer)

from django.core.exceptions import ValidationError

def update_lawyer(request, updid):
    if request.method == "POST":
        Nam = request.POST.get('name')
        ql = request.POST.get('Qualification')
        ema = request.POST.get('EmailID')
        spc = request.POST.get('Specialization')
        us = request.POST.get('Username')
        ap = request.POST.get('Appointment_Time')
        nm = request.POST.get('Mob_num')
        py = request.POST.get('pay')

        # Approval status
        is_approved = request.POST.get('approval') == 'approve'

        # Handle image upload
        try:
            imo = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(imo.name, imo)
        except MultiValueDictKeyError:
            file = LawyerDb.objects.get(id=updid).Image

        # Handle Appointment Time correctly
        if not ap:
            # Retain existing time if no new time provided
            ap = LawyerDb.objects.get(id=updid).Appointment_time
        else:
            try:
                # Ensure time format is valid (HH:MM)
                from datetime import time
                hours, minutes = map(int, ap.split(":"))
                ap = time(hours, minutes)
            except (ValueError, TypeError):
                messages.error(request, "Invalid appointment time format. Use HH:MM format.")
                return redirect(display_lawyer)

        # Update LawyerDb object
        LawyerDb.objects.filter(id=updid).update(
            Name=Nam,
            Qualification=ql,
            EmailID=ema,
            Specialization=spc,
            Username=us,
            Appointment_time=ap,
            is_approved=is_approved,
            Image=file,
            payment=py,
            Mob_No=nm
        )

        messages.success(request, "Lawyer Details Edited Successfully")
        return redirect(display_lawyer)



def remove_lawyer(request,removeid):
    ca = LawyerDb.objects.get(id=removeid)
    ca.delete()
    messages.error(request, "Company Details Deleted Successfully")
    return redirect(display_lawyer)



