from django import forms
from .models import Student

'''
class StudentForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=40)
    gender = forms.CharField(label='性别', choices=Student.GENDER_ITEMS)
    phone = forms.CharField(label='电话', max_length=20)
'''

class StudentForm(forms.ModelForm):
    def clean_phone(self):
        cleaned_data = self.cleaned_data['phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字')
        return int(cleaned_data)
    class Meta:
        model = Student
        fields = {
            'name', 'gender', 'phone'
        }