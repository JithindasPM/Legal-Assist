from django.urls import path
from Frontend import views
from Frontend.views import Groq_View


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
    


]

# path("chatbot/", Groq_View.as_view(), name="chatbot"),