from django.urls import path
from Frontend import views
from Frontend.views import Groq_View

from .views import send_otp, verify_otp, reset_password
from .views import send_otp, verify_otp, reset_password, request_otp_page, verify_otp_page, reset_password_page


urlpatterns=[
    path('homepage/',views.homepage,name="homepage"),
    path('aboutpage/<int:aboutid>/',views.aboutpage,name="aboutpage"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('lawyerdb/',views.lawyerdb,name="lawyerdb"),
    path('save_lawyer/',views.save_lawyer,name="save_lawyer"),
    path('Userpage/',views.Userpage,name="Userpage"),
    path('saveuser/',views.saveuser,name="saveuser"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('lawyer_log/',views.lawyer_log,name="lawyer_log"),
    path('lawyerlogin/',views.lawyerlogin,name="lawyerlogin"),
    path('lawyer_logout/',views.lawyer_logout,name="lawyer_logout"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('payment/<int:lawyers_id>/', views.payment, name='payment'),
    path('searchBar/',views.searchBar,name="searchBar"),
    path('approval/<int:pk>/', views.aproval, name='aproval'),
    path('thanks_page/',views.thanks_page,name="thanks_page"),
    path("chatbot/", Groq_View.as_view(), name="chatbot"),
    path('user/bookings/', views.user_bookings, name='user_bookings'),
    path('lawyer/bookings/', views.lawyer_bookings, name='lawyer_bookings'),
    
    path('send-otp/', send_otp, name='send_otp'),
    path('verify-otp/', verify_otp, name='verify_otp'),
    path('reset-password/', reset_password, name='reset_password'),
    path('request-otp/', request_otp_page, name='request_otp_page'),
    path('verify-otp-page/', verify_otp_page, name='verify_otp_page'),
    path('reset-password-page/', reset_password_page, name='reset_password_page'),

]

# path("chatbot/", Groq_View.as_view(), name="chatbot"),