from django import forms

# Create your forms here.

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'YOUR NAME'}), required=True)
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'YOUR EMAIL'}),required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ENTER SUBJECT'}),required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'MESSAGE HERE...'}), required=True)
    
    