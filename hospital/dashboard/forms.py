from django.conf import settings
from django import forms
from .models import *
from django.forms.widgets import CheckboxSelectMultiple
from django_select2.forms import Select2MultipleWidget


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'gender', 'mobile', 'birth_date',
                  'address', 'emp_type', 'title', 'user', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth Date'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'emp_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Employee Type'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Users'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'address': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }

    def clean_user(self, *args, **kwargs):
        instance = self.instance
        user = self.cleaned_data.get('user')
        qs = Employee.objects.filter(user=user)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                'This user has already been taken')
        return user


class DoctorModelForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'gender', 'mobile', 'birth_date',
                  'address', 'speciality', 'title', 'user', 'value', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth Date'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'speciality': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Speciality'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'user': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Users'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'address': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'value': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }

    def clean_user(self, *args, **kwargs):
        instance = self.instance
        user = self.cleaned_data.get('user')
        qs = Doctor.objects.filter(user=user)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                'This user has already been taken')
        return user


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department', 'active']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Department'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class RoomModelForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'type', 'bed', 'cost', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Name'}),
            'type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Room Type'}),
            'bed': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'No. of Beds'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Room Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class DrugModelForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['drug', 'active']
        widgets = {
            'drug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Drug Name'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),

        }


class LabModelForm(forms.ModelForm):
    class Meta:
        model = Lab
        fields = ['laboratory', 'group', 'cost', 'active']
        widgets = {
            'laboratory': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lab Test Name'}),
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Lab Groups'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lab Test Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class OperationModelForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['operation', 'group', 'cost', 'active']
        widgets = {
            'operation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Operation Name'}),
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Operation Groups'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Operation Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class ServiceModelForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['service', 'group', 'cost', 'active']
        widgets = {
            'service': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Service Name'}),
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Service Groups'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Service Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'group', 'cost', 'active']
        widgets = {
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image Name'}),
            'group': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Image Groups'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Image Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class DeliveryModelForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['delivery', 'cost', 'active']
        widgets = {
            'delivery': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Name'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Delivery Cost'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class SponsorModelForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['sponsor', 'active']
        widgets = {
            'sponsor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sponsor Name'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'gender', 'mobile', 'birth_date',
                  'address', 'status', 'active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Patient Name'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Birth Date'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status Type'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}),
            'address': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class TicketModelForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['doctor', 'status']
        widgets = {
            'doctor': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Status'}),
        }

    def clean_patient(self, *args, **kwargs):
        instance = self.instance
        patient = self.cleaned_data.get('patient')
        qs = Ticket.objects.filter(patient=patient)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                'This user has already been taken')
        return patient


class DiagnoseModelForm(forms.ModelForm):
    class Meta:
        model = Diagnose
        fields = ['diagnose', 'active']
        widgets = {
            'diagnose': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Diagnose Name'}),
            'active': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Active'}),
        }


class SurgeryHistoryModelForm(forms.ModelForm):
    past_medical_history = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=SurgeryHistory.past_medical_history_choices,
    )

    class Meta:
        model = SurgeryHistory
        fields = ['cheif_complain', 'past_medical_history', 'other', 'past_surgical_history',
                  'bp', 'p', 'temprature', 'spo', 'clinical_examination', 'diagnose']
        widgets = {
            'cheif_complain': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '30',  'placeholder': 'Cheif Complain'}),
            'other': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'If other, please type here other past medical histories'}),
            'past_surgical_history': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '30', 'placeholder': 'Type Past Surgical History'}),
            'bp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'BP'}),
            'p': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'P'}),
            'temprature': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Temprature'}),
            'spo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SPO2'}),
            'clinical_examination': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '30', 'placeholder': 'Type Clinical Examination'}),
            'diagnose': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Diagnose'}),
        }


class LabRequestModelForm(forms.ModelForm):
    lab_test = forms.ModelMultipleChoiceField(
        queryset=Lab.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = LabRequest
        fields = ['ticket', 'lab_test']
