from django import forms
from .models import Book, Student2, Document

class BookForm(forms.ModelForm):
    
    title = forms.CharField(
        max_length=50,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter book title',
            'class': 'form-control'
        })
    )
    author = forms.CharField(
        max_length=50,
        label="Author",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter author name',
            'class': 'form-control'
        })
    )
    price = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Price",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter price',
            'class': 'form-control'
        })
    )
    edition = forms.IntegerField(
        label="Edition",
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter edition',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'address']

from django import forms
from .models import Student3


class Student3Form(forms.ModelForm):
    class Meta:
        model  = Student3
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),  
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model  = Document
        fields = ['title', 'file']

