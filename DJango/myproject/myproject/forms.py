from django import forms

class Calculation(forms.Form):
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    email=forms.EmailField()
    name=forms.CharField(max_length=20,required=False)
    operator = forms.ChoiceField(choices=[("+", "Add"), ("-", "Subtract"), ("*", "Multiply"), ("/", "Divide")])