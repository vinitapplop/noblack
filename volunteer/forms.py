from django import forms
from .models import Volunteer
from django.forms.widgets import DateInput,TimeInput
forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local"
forms.TimeInput.input_type="time"
class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ('first_name','last_name','category','mobile','volunteering_for','landmark','from_date','to_date','avaiable_from','avaiable_till')
        widgets = {
            'from_date':DateInput(),
            'to_date':DateInput(),
            'avaiable_from':TimeInput(),
            'avaiable_till':TimeInput(),
        }

    def __init__(self, *args, **kwargs):
        super(VolunteerForm,self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class']= 'form-control'
            field.required = True