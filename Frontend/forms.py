from django import forms
from Frontend.models import Booking_Model
from django.utils import timezone


class Groq_Chat_Form(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control my-1',
            'placeholder': 'Ask anything . . .',
            'style': 'background-color:rgba(255, 255, 255, 0.4); height: 100px;',  # Adjust height
            'rows': 3,  # Set initial rows
        })
    )


# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking_Model
#         fields = ['booking_date', 'booking_time']

#     booking_date = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date()}),
#     )

#     booking_time = forms.TimeField(
#         widget=forms.TimeInput(attrs={'type': 'time'}),
#     )
