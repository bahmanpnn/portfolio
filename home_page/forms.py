from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Fullname',
                           widget=forms.TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Fullname'
                           }),
                           error_messages={
                               'required': 'please enter your fullname'
                           })
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Email'

                             }),
                             error_messages={
                                 'required': 'please enter your email'
                             })
    phone = forms.CharField(label='Phone Number',
                            widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Phone Number'

                            }),
                            error_messages={
                                'required': 'please enter your phone number'
                            })
    text = forms.CharField(label='Message',
                           widget=forms.Textarea(attrs={
                               'class': 'form-control',
                               'id': 'message',
                               'rows': 4,
                               'placeholder': 'Message'
                           }),
                           error_messages={
                               'required': 'please enter your Message'
                           })
