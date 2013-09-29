from django import forms

class QueryForm(forms.Form):
    student_id = forms.CharField(max_length=15)
