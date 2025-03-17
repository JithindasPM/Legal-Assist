from legal_assistance_project import settings
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from backend.views import LegalDb,CompanyDb
from Frontend.models import LawyerDb, UserDb, CustomerRequest
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponse, HttpResponseNotAllowed, \
    HttpResponseServerError
from django.urls import reverse
import re
import razorpay
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from razorpay import Client as RazorpayClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
# from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
# from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
from PyPDF2 import PdfReader
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings


# Create your views here.
def homepage(request):
    law = LegalDb.objects.all()
    approved_lawyers = LawyerDb.objects.filter(is_approved=True)
    return render(request,"Home.html",{'law':law, 'approved_lawyers':approved_lawyers})

def aboutpage(req,aboutid):
    about = LegalDb.objects.get(id=aboutid)
    return render(req,"About.html",{'about':about})
def aboutus(request):
    return render(request, "Aboutus.html")
def lawyerdb(request):
    return render(request, "lawyerreg.html")
def save_lawyer(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        qal = request.POST.get('quali')
        ema = request.POST.get('email')
        spe = request.POST.get('spec')
        usn = request.POST.get('username')
        pwd = request.POST.get('password')
        py = request.POST.get('Amount')
        app = request.POST.get('apptime')
        no = request.POST.get('phnno')
        pic = request.FILES['image']
        if LawyerDb.objects.filter(EmailID=ema).exists():
            messages.error(request, "Email already exists")
            return HttpResponseRedirect(reverse('lawyerdb'))
        if LawyerDb.objects.filter(Username=usn).exists():
            messages.error(request, "Username already exists")
            return HttpResponseRedirect(reverse('lawyerdb'))
        if LawyerDb.objects.filter(Mob_No=no).exists():
            messages.error(request, "Mobile number already exists")
            return HttpResponseRedirect(reverse('lawyerdb'))
        if len(no) != 10:
            messages.error(request, "Mobile number must be 10 characters long")
            return HttpResponseRedirect(reverse('lawyerdb'))
        if len(pwd) < 6 or not re.search(r'[A-Z]', pwd) or not re.search(r'[!@#$%^&*()_+}{":?><,./;\'[\]]', pwd):
            messages.error(request, "Password must be greater than 5 characters and contain at least one capital letter and one special character")
            return HttpResponseRedirect(reverse('lawyerdb'))

        obj = LawyerDb(Name=nam,Qualification=qal,EmailID=ema,Specialization=spe,Username=usn,Password=pwd,payment=py, Mob_No=no,Appointment_time=app,Image=pic)


        obj.save()
        return redirect(lawyer_log)
def Userpage(request):
    return render(request, "User_Reg_log.html")
def saveuser(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        ph = req.POST.get('mobile')
        us = req.POST.get('username')
        pw = req.POST.get('password')

        # Check if email already exists
        if UserDb.objects.filter(EmailId=em).exists():
            messages.error(req, "Email already exists")
            return HttpResponseRedirect(reverse('Userpage'))

        # Check if username already exists
        if UserDb.objects.filter(username=us).exists():
            messages.error(req, "Username already exists")
            return HttpResponseRedirect(reverse('Userpage'))

        # Check if mobile number already exists
        if UserDb.objects.filter(Phn_No=ph).exists():
            messages.error(req, "Mobile number already exists")
            return HttpResponseRedirect(reverse('Userpage'))

        # Ensure mobile number is 10 characters long
        if len(ph) != 10:
            messages.error(req, "Mobile number must be 10 characters long")
            return HttpResponseRedirect(reverse('Userpage'))

        # Password criteria: greater than 5 characters, contains a capital letter, and a special character
        if len(pw) < 6 or not re.search(r'[A-Z]', pw) or not re.search(r'[!@#$%^&*()_+}{":?><,./;\'[\]]', pw):
            messages.error(req, "Password must be greater than 5 characters and contain at least one capital letter and one special character")
            return HttpResponseRedirect(reverse('Userpage'))

        # Create and save user object with plain text password
        obj = UserDb(Name=na, EmailId=em, Phn_No=ph, username=us, password=pw)
        obj.save()
        return redirect(Userpage)


def userlogin(request):
    if request.method == "POST":
        una = request.POST.get('username')
        psd = request.POST.get('password')
        user = UserDb.objects.filter(username=una, password=psd).first()
        if user:
            request.session['id'] = user.id  # Adding user ID to the session
            request.session['username'] = una
            request.session['password'] = psd
            messages.success(request, "User logged in successfully")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid username or password")
            return redirect(userlogin)
    else:
        return redirect(userlogin)

def lawyer_log(request):
    return render(request, "lawyer_log.html")

def lawyerlogin(request):
    if request.method == "POST":
        urn = request.POST.get('user_name')
        ped = request.POST.get('pass_word')

        # Check if a lawyer with the given username and password exists and is approved
        approved_lawyer = LawyerDb.objects.filter(Username=urn, Password=ped, is_approved=True).first()

        if approved_lawyer:
            # Set session variables if needed
            request.session['Username'] = urn
            request.session['Password'] = ped
            request.session['lawyer_id'] = approved_lawyer.id 
            print(f"Logged in lawyer ID: {approved_lawyer.id}")

            messages.success(request, "Lawyer logged in successfully")
            return redirect(homepage)
        else:
            messages.error(request, "Invalid Username or Password or Lawyer is not approved")
            return redirect(lawyer_log)
    else:
        return redirect(lawyer_log)
    
def lawyer_logout(request):
    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Lawyer logged Out Successfully")
    return redirect(homepage)
    

def user_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "User logged Out Successfully")
    return redirect(homepage)


import razorpay
from django.shortcuts import render, get_object_or_404
from .models import LawyerDb

from Frontend.models import Booking_Model

def payment(request, lawyers_id):
    lawyer = get_object_or_404(LawyerDb, id=lawyers_id)
    payy = lawyer.payment
    amount = int(payy * 100)  # Convert to paisa for Razorpay
    payy_str = str(amount)
    total = int(payy_str) / 100

    user_id = request.session.get('id')
    if not user_id:
        messages.error(request, "User not logged in.")
        return redirect('userlogin')

    user = get_object_or_404(UserDb, id=user_id)

    if request.method == "POST":
        booking_date = request.POST.get('booking_date')
        payment_id = request.POST.get('payment_id')

        if booking_date and payment_id:
            Booking_Model.objects.create(
                user=user,
                Lawyer=lawyer,
                amount=total,
                booking_date=booking_date
            )
            messages.success(request, "Booking and payment initiated successfully.")
            return JsonResponse({'status': 'success'})

    return render(request, "payment.html", {'payy_str': payy_str, 'lawyer': lawyer})





def searchBar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        vak = None  # Initialize vak to None

        if query:
            # Filter by 'Qualification' and only include approved lawyers
            print("Search query:", query)
            vak = LawyerDb.objects.filter(Q(Specialization__icontains=query), is_approved=True)
            print("Queryset:", vak)
        else:
            print("No search query provided")

        return render(request, "Lawyer_Search_result.html", {'vak': vak})



def aproval(request, pk):
    user = request.user
    lawyer_id = pk
    # Check if a request already exists for the user and lawyer
    existing_request = CustomerRequest.objects.filter(user=user, lawyer_id=lawyer_id).exists()
    if not existing_request:
        CustomerRequest.objects.create(user=user, lawyer_id=lawyer_id)
    return redirect('payment')  # Redirect to payment page after request approval

# def lawyer_sub(request):
#     return render(request, "Subscription.html")

# def payment_law(request):
#     if request.method=="POST":
#         amount=50000
#         order_currency='INR'
#         client = razorpay.Client(auth=('rzp_test_IzIBFTmzd3zzKk','mMvIdZd7a4EU1pMd9tSQEbE0'))
#         payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
#     return render(request,"pay.html")

def thanks_page(request):
    return render(request, "thanks.html")


import groq
import re

client = groq.Client(api_key="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")


def get_groq_response(user_input):
    """
    Communicate with the GROQ chatbot to get a response based on user input.
    This version focuses on providing accurate and clear information.
    """
    system_prompt = {
        "role": "system",
        "content": ("You are a helpful assistant. Provide concise, accurate, and relevant legal information. "
                    "Focus on Indian law and legal practices, but avoid repeating the word 'India' unnecessarily. "
                    "Answer directly and to the point, only mentioning India when it's absolutely necessary.")
    }

    chat_history = [system_prompt]

    # Append user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    # Get response from GROQ API
    chat_completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=100,
        temperature=0.5  # Reduced temperature for more factual consistency
    )

    response = chat_completion.choices[0].message.content

    # Format response (convert *bold* to <b>bold</b>)
    response = re.sub(r'\\(.?)\\*', r'<b>\1</b>', response)

    return response


from Frontend.forms import Groq_Chat_Form
from django.views.generic import View
    
class Groq_View(View):
    def get(self, request, *args, **kwargs):
        form = Groq_Chat_Form()
        # Start with fresh chat history
        request.session['chat_history'] = []
        return render(request, 'chat_boat.html', {'form': form, 'chat_history': []})
    
    def post(self, request, *args, **kwargs):
        form = Groq_Chat_Form(request.POST)
        user_input = request.POST.get('text')

        if not user_input:
            message = 'Please enter a message'
            return render(request, 'chat.html', {
                'error': message, 
                'form': form, 
                'chat_history': request.session.get('chat_history', [])
            })

        # Get response from Groq
        chatbot_response = get_groq_response(user_input)
        
        # Get existing chat history or initialize empty list
        chat_history = request.session.get('chat_history', [])
        
        # Add new messages to history
        chat_history.append({
            'user': user_input,
            'bot': chatbot_response
        })
        
        # Update session
        request.session['chat_history'] = chat_history
        request.session.modified = True
        
        form = Groq_Chat_Form()
        return render(request, 'chat_boat.html', {
            'form': form, 
            'chat_history': chat_history
        })
        

# def user_bookings(request):
#     # Retrieve user ID from session
#     user_id = request.session.get('id')
    
#     if not user_id:
#         messages.error(request, "You must be logged in to view bookings.")
#         return redirect('userlogin')
    
#     user = get_object_or_404(UserDb, id=user_id)

#     bookings = Booking_Model.objects.filter(user=user).order_by('-created_date')

#     return render(request, "user_bookings.html", {'bookings': bookings})

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def user_bookings(request):
    # Retrieve user ID from session
    user_id = request.session.get('id')
    
    if not user_id:
        messages.error(request, "You must be logged in to view bookings.")
        return redirect('userlogin')
    
    user = get_object_or_404(UserDb, id=user_id)

    bookings_list = Booking_Model.objects.filter(user=user).order_by('-created_date')
    
    # Pagination: 5 bookings per page
    paginator = Paginator(bookings_list, 5)  
    page = request.GET.get('page')
    
    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        bookings = paginator.page(1)
    except EmptyPage:
        bookings = paginator.page(paginator.num_pages)

    return render(request, "user_bookings.html", {'bookings': bookings})

    
def lawyer_bookings(request):
    
    lawyer_id = request.session.get('lawyer_id')
    print(lawyer_id)

    if not lawyer_id:
        messages.error(request, "You must be logged in to view bookings.")
        return redirect('lawyer_log')

    lawyer = get_object_or_404(LawyerDb, id=lawyer_id)

    bookings_list = Booking_Model.objects.filter(Lawyer=lawyer).order_by('-created_date')

    print(f"Total bookings found: {bookings_list.count()}")  # Debugging

    paginator = Paginator(bookings_list, 5)
    page = request.GET.get('page')

    try:
        bookings = paginator.page(page)
    except PageNotAnInteger:
        bookings = paginator.page(1)
    except EmptyPage:
        bookings = paginator.page(paginator.num_pages)

    return render(request, "lawyer_booking.html", {'bookings': bookings})

