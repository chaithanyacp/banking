from django import forms
from .models import Customer,Branch,District

DISTRICT_CHOICES = (
            ('Ernakulam','Ernakulam'),
            ('Thrissur','Thrissur'),
            ('Kozhikode','Kozhikode'),
            ('Thiruvananthapuram','Thiruvananthapuram'),
            ('Kannur','Kannur'))
GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'))
class CustomerForm(forms.ModelForm):

    # district = forms.ChoiceField(choices=DISTRICT_CHOICES)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField( widget=forms.RadioSelect,choices=GENDER_CHOICES)
    # branch = forms.ChoiceField(choices=[('Aluva','Aluva'),('Thalassery','Thalassery'),
    #                                     ('Payyanur','Payyanur'),('kannur main','kannur main'),
    #                                     ('Chalakudy','Chalakudy'),('Ernakulam town','Ernakulam town'),
    #                                     ('Vadakara','Vadakara'),('Koyilandy','Koyilandy')])
    account_type = forms.ChoiceField(choices=[('savings', 'Savings'),
                                              ('current', 'Current')])
    materials_provide = forms.MultipleChoiceField(choices=[('debit', 'Debit Card'),
                                                           ('credit', 'Credit Card'),
                                                           ('cheque', 'Cheque Book')],
                                                  widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Customer
        fields = ('name', 'dob','age', 'gender', 'phone_number', 'email', 'address', 'account_type', 'materials_provide')
