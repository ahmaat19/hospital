from django.conf import settings
from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        max_length=6, choices=gender_choices, default='Male')
    birth_date = models.DateField(max_length=10)
    address_choices = [
        ('Banaadir', 'Banaadir'),
        ('Jubbada Dhexe', 'Jubbada Dhexe'),
        ('Jubbada Hoose', 'Jubbada Hoose'),
        ('Mudug', 'Mudug'),
        ('Hiiran', 'Hiiran'),
        ('Awdal', 'Awdal'),
        ('Bakool', 'Bakool'),
        ('Bari', 'Bari'),
        ('Baay', 'Baay'),
        ('Galgaduud', 'Galgaduud'),
        ('Gedo', 'Gedo'),
        ('Nugaal', 'Nugaal'),
        ('Sanaag', 'Sanaag'),
        ('Shabeellaha Hoose', 'Shabeellaha Hoose'),
        ('Shabeellaha Dhexe', 'Shabeellaha Dhee'),
        ('Sool', 'Sool'),
        ('Togdheer', 'Togdheer'),
        ('Woqooyi Galbeed', 'Woqooyi Galbeed')
    ]
    address = models.CharField(
        max_length=20, choices=address_choices, default='Banaadir')
    mobile = models.CharField(max_length=15)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    emp_type_choices = [
        ('Nurse', 'Nurse'),
        ('Other', 'Other'),
    ]
    emp_type = models.CharField(
        max_length=5, choices=emp_type_choices, default='Nurse')
    title = models.CharField(max_length=100)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        max_length=6, choices=gender_choices, default='Male')
    birth_date = models.DateField(max_length=10)
    address_choices = [
        ('Banaadir', 'Banaadir'),
        ('Jubbada Dhexe', 'Jubbada Dhexe'),
        ('Jubbada Hoose', 'Jubbada Hoose'),
        ('Mudug', 'Mudug'),
        ('Hiiran', 'Hiiran'),
        ('Awdal', 'Awdal'),
        ('Bakool', 'Bakool'),
        ('Bari', 'Bari'),
        ('Baay', 'Baay'),
        ('Galgaduud', 'Galgaduud'),
        ('Gedo', 'Gedo'),
        ('Nugaal', 'Nugaal'),
        ('Sanaag', 'Sanaag'),
        ('Shabeellaha Hoose', 'Shabeellaha Hoose'),
        ('Shabeellaha Dhexe', 'Shabeellaha Dhee'),
        ('Sool', 'Sool'),
        ('Togdheer', 'Togdheer'),
        ('Woqooyi Galbeed', 'Woqooyi Galbeed')
    ]
    address = models.CharField(
        max_length=20, choices=address_choices, default='Banaadir')
    mobile = models.CharField(max_length=15)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    speciality_choices = [
        ('Allergy & immunology', 'Allergy & immunology'),
        ('Anesthesiology', 'Anesthesiology'),
        ('Dermatology', 'Dermatology'),
        ('Diagnostic radiology', 'Diagnostic radiology'),
        ('Emergency medicine', 'Emergency medicine'),
        ('Family medicine', 'Family medicine'),
        ('Internal medicine', 'Internal medicine'),
        ('Medical genetics', 'Medical genetics'),
        ('Neurology', 'Neurology'),
        ('Nuclear medicine', 'Nuclear medicine'),
        ('Obstetrics and gynecology', 'Obstetrics and gynecology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Pathology', 'Pathology'),
        ('Pediatrics', 'Pediatrics'),
        ('Physical medicine & rehabilitation',
         'Physical medicine & rehabilitation'),
        ('Preventive medicine', 'Preventive medicine'),
        ('Psychiatry', 'Psychiatry'),
        ('Radiation oncology', 'Radiation oncology'),
        ('Surgery', 'Surgery'),
        ('Urology', 'Urology')
    ]
    speciality = models.CharField(
        max_length=100, choices=speciality_choices, default='Family medicine')
    title = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    department = models.CharField(max_length=50, unique=True,)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.department


class Room(models.Model):
    name = models.CharField(max_length=10, unique=True)
    type_choices = [
        ('Normal', 'Normal'),
        ('VIP', 'VIP'),
    ]
    type = models.CharField(
        max_length=6, choices=type_choices, default='Normal')
    bed = models.CharField(max_length=2)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Drug(models.Model):
    drug = models.CharField(max_length=100, unique=True,)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.drug


class Lab_Group(models.Model):
    group = models.CharField(max_length=100, unique=True,)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.group


class Lab(models.Model):
    laboratory = models.CharField(max_length=50, unique=True)
    group = models.ForeignKey(Lab_Group, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.laboratory

    class Meta:
        ordering = ['group']


class Operation_Group(models.Model):
    group = models.CharField(max_length=100, unique=True,)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.group


class Operation(models.Model):
    operation = models.CharField(max_length=50, unique=True)
    group = models.ForeignKey(Operation_Group, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.operation


class Service_Group(models.Model):
    group = models.CharField(max_length=100, unique=True,)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.group


class Service(models.Model):
    service = models.CharField(max_length=50, unique=True)
    group = models.ForeignKey(Service_Group, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.service


class Image_Group(models.Model):
    group = models.CharField(max_length=100, unique=True,)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.group


class Image(models.Model):
    image = models.CharField(max_length=50, unique=True)
    group = models.ForeignKey(Image_Group, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.image


class Delivery(models.Model):
    delivery = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.delivery


class Sponsor(models.Model):
    sponsor = models.CharField(max_length=50, unique=True)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sponsor


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(
        max_length=6, choices=gender_choices, default='Male')
    birth_date = models.DateField(max_length=10)
    address_choices = [
        ('Banaadir', 'Banaadir'),
        ('Jubbada Dhexe', 'Jubbada Dhexe'),
        ('Jubbada Hoose', 'Jubbada Hoose'),
        ('Mudug', 'Mudug'),
        ('Hiiran', 'Hiiran'),
        ('Awdal', 'Awdal'),
        ('Bakool', 'Bakool'),
        ('Bari', 'Bari'),
        ('Baay', 'Baay'),
        ('Galgaduud', 'Galgaduud'),
        ('Gedo', 'Gedo'),
        ('Nugaal', 'Nugaal'),
        ('Sanaag', 'Sanaag'),
        ('Shabeellaha Hoose', 'Shabeellaha Hoose'),
        ('Shabeellaha Dhexe', 'Shabeellaha Dhee'),
        ('Sool', 'Sool'),
        ('Togdheer', 'Togdheer'),
        ('Woqooyi Galbeed', 'Woqooyi Galbeed')
    ]
    address = models.CharField(
        max_length=20, choices=address_choices, default='Banaadir')
    mobile = models.CharField(max_length=15)
    status_choices = [
        ('Child', 'Child'),
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    status = models.CharField(
        max_length=7, choices=status_choices, default='Single')
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    status_choices = [
        ('OutPatient', 'OutPatient'),
        ('Emergency', 'Emergency'),
        ('Delivery', 'Delivery')]
    status = models.CharField(
        max_length=10, choices=status_choices, default='OutPatient')
    ticket_no = models.IntegerField()
    is_active = models.IntegerField(default=1)
    has_cancelled = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.patient.name


class Diagnose(models.Model):
    diagnose = models.CharField(max_length=100, unique=True)
    active_choices = [('Yes', 'Yes'),
                      ('No', 'No')]
    active = models.CharField(
        max_length=6, choices=active_choices, default='Yes')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.diagnose


# History Taking Models =================================================>>


class SurgeryHistory(models.Model):
    cheif_complain = models.CharField(max_length=400)
    past_medical_history_choices = [
        ('DM', 'DM'),
        ('HTN', 'HTN'),
        ('Cardiac', 'Cardiac'),
        ('Other', 'Other')
    ]
    past_medical_history = MultiSelectField(
        choices=past_medical_history_choices)
    other = models.CharField(max_length=400, blank=True, null=True)
    past_surgical_history = models.CharField(max_length=300)
    bp = models.CharField(max_length=10)
    p = models.CharField(max_length=10)
    temprature = models.CharField(max_length=10)
    spo = models.CharField(max_length=10)
    clinical_examination = models.CharField(max_length=300)
    diagnose = models.ForeignKey(Diagnose, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.cheif_complain

# Finished History Taking Models


class LabRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    lab_test = models.ManyToManyField(Lab)
    paid = models.IntegerField(default=0)
    examined = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.ticket.patient.name

    class Meta:
        ordering = ['-lab_test__group.id']
