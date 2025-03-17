from django import forms


class Groq_Chat_Form(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control my-1',
            'placeholder': 'Ask anything . . .',
            'style': 'background-color:rgba(255, 255, 255, 0.4); height: 100px;',  # Adjust height
            'rows': 3,  # Set initial rows
        })
    )
