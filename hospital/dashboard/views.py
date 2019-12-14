from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime, date
from django.contrib import messages
from .forms import *
from .models import *

# Create your views here.


def IndexView(request):
    return render(request, 'index.html')


@login_required
def EmployeeView(request):
    form = EmployeeModelForm(request.POST or None)
    employee_list = Employee.objects.order_by('-id')
    paginator = Paginator(employee_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    employees = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = employee_list.count()
    if queryset:
        queryset = Employee.objects.filter(
            Q(name__icontains=queryset) | Q(mobile__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Employee was added successfully.')
        return redirect('/dashboard/employee')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Employees',
        'queryset': queryset,
        'total': total,
        'employees': employees,
    }
    return render(request, 'dashboard/employee.html', context)


@login_required
def EmployeeUpdateView(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeModelForm(request.POST or None, instance=employee)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Employee was updated successfully.')
        return redirect('/dashboard/employee')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Employee',
    }
    return render(request, 'dashboard/employee.html', context)


@login_required
def DoctorView(request):
    form = DoctorModelForm(request.POST or None)
    doctor_list = Doctor.objects.order_by('-id')
    paginator = Paginator(doctor_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    doctors = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = doctor_list.count()
    if queryset:
        queryset = Doctor.objects.filter(
            Q(name__icontains=queryset) | Q(mobile__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Doctor was added successfully.')
        return redirect('/dashboard/doctor')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Doctors',
        'queryset': queryset,
        'total': total,
        'doctors': doctors,
    }
    return render(request, 'dashboard/doctor.html', context)


@login_required
def DoctorUpdateView(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    form = DoctorModelForm(request.POST or None, instance=doctor)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Doctor was updated successfully.')
        return redirect('/dashboard/doctor')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Doctor',
    }
    return render(request, 'dashboard/doctor.html', context)


@login_required
def DepartmentView(request):
    form = DepartmentModelForm(request.POST or None)
    department_list = Department.objects.order_by('-id')
    paginator = Paginator(department_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    departments = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = department_list.count()
    if queryset:
        queryset = Department.objects.filter(Q(department__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Department added successfully.')
        return redirect('/dashboard/department')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Departments',
        'queryset': queryset,
        'total': total,
        'departments': departments
    }
    return render(request, 'dashboard/department.html', context)


@login_required
def DepartmentUpdateView(request, pk):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentModelForm(request.POST or None, instance=department)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Department was updated successfully.')
        return redirect('/dashboard/department')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Department',
    }
    return render(request, 'dashboard/department.html', context)


@login_required
def RoomView(request):
    form = RoomModelForm(request.POST or None)
    room_list = Room.objects.order_by('-id')
    paginator = Paginator(room_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    rooms = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = room_list.count()
    if queryset:
        queryset = Room.objects.filter(Q(name__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Room added successfully.')
        return redirect('/dashboard/room')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Rooms',
        'queryset': queryset,
        'total': total,
        'rooms': rooms
    }
    return render(request, 'dashboard/room.html', context)


@login_required
def RoomUpdateView(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomModelForm(request.POST or None, instance=room)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Room was updated successfully.')
        return redirect('/dashboard/room')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Room',
    }
    return render(request, 'dashboard/room.html', context)


@login_required
def DrugView(request):
    form = DrugModelForm(request.POST or None)
    drug_list = Drug.objects.order_by('-id')
    paginator = Paginator(drug_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    drugs = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = drug_list.count()
    if queryset:
        queryset = Drug.objects.filter(Q(drug__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Drug added successfully.')
        return redirect('/dashboard/drug')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Drugs',
        'queryset': queryset,
        'total': total,
        'drugs': drugs
    }
    return render(request, 'dashboard/drug.html', context)


@login_required
def DrugUpdateView(request, pk):
    drug = get_object_or_404(Drug, pk=pk)
    form = DrugModelForm(request.POST or None, instance=drug)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Drug was updated successfully.')
        return redirect('/dashboard/drug')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Drug',
    }
    return render(request, 'dashboard/drug.html', context)


@login_required
def LabView(request):
    form = LabModelForm(request.POST or None)
    lab_list = Lab.objects.order_by('-id')
    paginator = Paginator(lab_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    labs = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = lab_list.count()
    if queryset:
        queryset = Lab.objects.filter(Q(laboratory__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Lab Test added successfully.')
        return redirect('/dashboard/laboratory')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Laboratory Tests',
        'queryset': queryset,
        'total': total,
        'labs': labs
    }
    return render(request, 'dashboard/laboratory.html', context)


@login_required
def LabUpdateView(request, pk):
    labs = get_object_or_404(Lab, pk=pk)
    form = LabModelForm(request.POST or None, instance=labs)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Lab Test was updated successfully.')
        return redirect('/dashboard/laboratory')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update lab Test',
    }
    return render(request, 'dashboard/laboratory.html', context)


@login_required
def OperationView(request):
    form = OperationModelForm(request.POST or None)
    operation_list = Operation.objects.order_by('-id')
    paginator = Paginator(operation_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    operations = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = operation_list.count()
    if queryset:
        queryset = Operation.objects.filter(Q(operation__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Operation added successfully.')
        return redirect('/dashboard/operation')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Operations',
        'queryset': queryset,
        'total': total,
        'operations': operations
    }
    return render(request, 'dashboard/operation.html', context)


@login_required
def OperationUpdateView(request, pk):
    operations = get_object_or_404(Operation, pk=pk)
    form = OperationModelForm(request.POST or None, instance=operations)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Operation was updated successfully.')
        return redirect('/dashboard/operation')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Operation',
    }
    return render(request, 'dashboard/operation.html', context)


@login_required
def ServiceView(request):
    form = ServiceModelForm(request.POST or None)
    service_list = Service.objects.order_by('-id')
    paginator = Paginator(service_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    services = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = service_list.count()
    if queryset:
        queryset = Service.objects.filter(Q(service__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Service added successfully.')
        return redirect('/dashboard/service')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Services',
        'queryset': queryset,
        'total': total,
        'services': services
    }
    return render(request, 'dashboard/service.html', context)


@login_required
def ServiceUpdateView(request, pk):
    services = get_object_or_404(Service, pk=pk)
    form = ServiceModelForm(request.POST or None, instance=services)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Service was updated successfully.')
        return redirect('/dashboard/service')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Service',
    }
    return render(request, 'dashboard/service.html', context)


@login_required
def ImageView(request):
    form = ImageModelForm(request.POST or None)
    image_list = Image.objects.order_by('-id')
    paginator = Paginator(image_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    images = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = image_list.count()
    if queryset:
        queryset = Image.objects.filter(Q(image__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Image added successfully.')
        return redirect('/dashboard/image')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Images',
        'queryset': queryset,
        'total': total,
        'images': images
    }
    return render(request, 'dashboard/image.html', context)


@login_required
def ImageUpdateView(request, pk):
    images = get_object_or_404(Image, pk=pk)
    form = ImageModelForm(request.POST or None, instance=images)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Image was updated successfully.')
        return redirect('/dashboard/image')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Image',
    }
    return render(request, 'dashboard/image.html', context)


@login_required
def DeliveryView(request):
    form = DeliveryModelForm(request.POST or None)
    delivery_list = Delivery.objects.order_by('-id')
    paginator = Paginator(delivery_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    deliveries = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = delivery_list.count()
    if queryset:
        queryset = Delivery.objects.filter(Q(delivery__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Delivery added successfully.')
        return redirect('/dashboard/delivery')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Deliveries',
        'queryset': queryset,
        'total': total,
        'deliveries': deliveries
    }
    return render(request, 'dashboard/delivery.html', context)


@login_required
def DeliveryUpdateView(request, pk):
    deliveries = get_object_or_404(Delivery, pk=pk)
    form = DeliveryModelForm(request.POST or None, instance=deliveries)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Delivery was updated successfully.')
        return redirect('/dashboard/delivery')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Delivery',
    }
    return render(request, 'dashboard/delivery.html', context)


@login_required
def SponsorView(request):
    form = SponsorModelForm(request.POST or None)
    sponsors_list = Sponsor.objects.order_by('-id')
    paginator = Paginator(sponsors_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    sponsors = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = sponsors_list.count()
    if queryset:
        queryset = Sponsor.objects.filter(Q(sponsor__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Sponsor added successfully.')
        return redirect('/dashboard/sponsor')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Sponsors',
        'queryset': queryset,
        'total': total,
        'sponsors': sponsors
    }
    return render(request, 'dashboard/sponsor.html', context)


@login_required
def SponsorUpdateView(request, pk):
    sponsors = get_object_or_404(Sponsor, pk=pk)
    form = SponsorModelForm(request.POST or None, instance=sponsors)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Sponsor was updated successfully.')
        return redirect('/dashboard/sponsor')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Sponsor',
    }
    return render(request, 'dashboard/sponsor.html', context)


@login_required
def DiagnoseView(request):
    form = DiagnoseModelForm(request.POST or None)
    diagnoses_list = Diagnose.objects.order_by('-id')
    paginator = Paginator(diagnoses_list, 10)  # Show 10 contacts per page
    page = request.GET.get('page')
    diagnoses = paginator.get_page(page)

    queryset = request.GET.get('q')
    total = diagnoses_list.count()
    if queryset:
        queryset = Diagnose.objects.filter(Q(diagnose__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Diagnose added successfully.')
        return redirect('/dashboard/diagnose')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Diagnoses',
        'queryset': queryset,
        'total': total,
        'diagnoses': diagnoses
    }
    return render(request, 'dashboard/diagnose.html', context)


@login_required
def DiagnoseUpdateView(request, pk):
    diagnoses = get_object_or_404(Diagnose, pk=pk)
    form = DiagnoseModelForm(request.POST or None, instance=diagnoses)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Diagnose was updated successfully.')
        return redirect('/dashboard/diagnose')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Diagnose',
    }
    return render(request, 'dashboard/diagnose.html', context)


@login_required
def PatientView(request):
    form = PatientModelForm(request.POST or None)
    patient_list = Patient.objects.order_by('-id')
    paginator = Paginator(patient_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    patients = paginator.get_page(page)
    queryset = request.GET.get('q')
    total = patient_list.count()
    if queryset:
        queryset = Patient.objects.filter(
            Q(name__icontains=queryset) | Q(mobile__icontains=queryset) | Q(id__icontains=queryset))
        total = queryset.count()
    if form.is_valid():
        obj = form.save(commit=False)
        obj.created_by = request.user.id
        obj.save()
        messages.success(request, 'Patient was added successfully.')
        return redirect('/dashboard/patient')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Patients',
        'queryset': queryset,
        'total': total,
        'patients': patients,
    }
    return render(request, 'dashboard/patient.html', context)


@login_required
def PatientUpdateView(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientModelForm(request.POST or None, instance=patient)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        obj.save()
        messages.success(request, 'Patient was updated successfully.')
        return redirect('/dashboard/patient')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Patient',
    }
    return render(request, 'dashboard/patient.html', context)


@login_required
def TicketView(request):
    total = ''
    tickets = ''
    queryset = request.GET.get('q')
    if queryset:
        queryset = Ticket.objects.filter(
            Q(patient__id__icontains=queryset), is_active=1, has_cancelled=0)
        paginator = Paginator(queryset, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        tickets = paginator.get_page(page)
        total = queryset.count()
    context = {
        'title': 'Tickets',
        'queryset': queryset,
        'total': total,
        'tickets': tickets,
    }
    return render(request, 'dashboard/ticket.html', context)


@login_required
def TicketToGenerateView(request, pk):
    ready_ticket = Ticket.objects.filter(
        patient_id=pk, is_active=1, has_cancelled=0)
    if not ready_ticket:
        ticket = get_object_or_404(Patient, pk=pk, active='Yes')

        form = TicketModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.patient_id = ticket.id
            obj.created_by = request.user.id
            doctorID = request.POST['doctor']
            value = get_object_or_404(Doctor, pk=doctorID)
            obj.value = value.value
            today = date.today()
            obj.ticket_no = Ticket.objects.filter(created__year=today.year,
                                                  created__month=today.month,
                                                  created__day=today.day,
                                                  doctor_id=request.POST['doctor']).count()+1
            obj.save()
            messages.success(request, 'Patient assigned successfully.')
            return redirect('/dashboard/ticket')
    else:
        messages.success(
            request, 'This patient has already been assigned to a doctor.')
        return redirect('/dashboard/patient')
    context = {
        'form': form,
        'valueBtn': 'Add',
        'title': 'Tickets',
        'ticket': ticket,
    }
    return render(request, 'dashboard/ticket.html', context)


@login_required
def TicketUpdateView(request, pk):
    ticket_id = get_object_or_404(Ticket, pk=pk, has_cancelled=0, is_active=1)
    form = TicketModelForm(request.POST or None, instance=ticket_id)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.updated_by = request.user.id
        doctorID = request.POST['doctor']
        value = get_object_or_404(Doctor, pk=doctorID)
        obj.value = value.value
        today = date.today()
        obj.ticket_no = Ticket.objects.filter(created__year=today.year,
                                              created__month=today.month,
                                              created__day=today.day,
                                              doctor_id=request.POST['doctor']).count()+1
        obj.save()
        messages.success(request, 'Ticket was updated successfully.')
        return redirect('/dashboard/ticket')
    context = {
        'form': form,
        'valueBtn': 'Update',
        'title': 'Update Ticket',
        'ticket': ticket_id
    }
    return render(request, 'dashboard/ticket.html', context)


@login_required
def TicketCancelView(request, pk):
    Ticket.objects.filter(pk=pk, has_cancelled=0, is_active=1).update(
        has_cancelled=1, updated_by=request.user.id, is_active=0)
    messages.success(request, 'Ticket has been cancelled successfully.')
    return redirect('/dashboard/ticket')


@login_required
def TicketPrintView(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, has_cancelled=0, is_active=1)
    context = {
        'ticket': ticket,
        'being': 'Ticket',
        'user': request.user,
        'today': date.today()
    }
    return render(request, 'dashboard/ticket_print.html', context)


@login_required
def HistoryView(request):
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    patients = ''
    total = ''
    for doc in doctor:
        patient_list = Ticket.objects.filter(
            has_cancelled=0, is_active=1, doctor=doc.id).order_by('-created')
        paginator = Paginator(patient_list, 10)  # Show 10 contacts per page
        page = request.GET.get('page')
        patients = paginator.get_page(page)
        total = patient_list.count()
    queryset = request.GET.get('q')
    if queryset:
        for doc in doctor:
            queryset = Ticket.objects.filter(
                Q(patient__id__icontains=queryset), has_cancelled=0, is_active=1, doctor=doc.id).order_by('-created')
            total = queryset.count()
    context = {
        'patients': patients,
        'queryset': queryset,
        'title': 'Waiting Patients',
        'total': total
    }
    return render(request, 'dashboard/history.html', context)


@login_required
def HistoryTakingView(request, pk):
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    form = ''
    for doc in doctor:
        ticket = get_object_or_404(
            Ticket, pk=pk, has_cancelled=0, is_active=1, doctor=doc.id)
        if doc.speciality == 'Surgery':
            form = SurgeryHistoryModelForm(request.POST or None)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.created_by = request.user.id
                obj.ticket = ticket
                obj.save()
                Ticket.objects.filter(pk=pk, has_cancelled=0, is_active=1).update(
                    is_active=0, updated_by=request.user.id)
                messages.success(
                    request, 'Surgical History was taken successfully.')
                return redirect('/dashboard/history')
    context = {
        'title': 'History Taking',
        'surgery_form': form,
        'valueBtn': 'Save',
    }
    return render(request, 'dashboard/historytaking.html', context)


@login_required
def HistoryTakingUpdateView(request, pk):
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    form = ''
    for doc in doctor:
        surgery_history_id = get_object_or_404(SurgeryHistory, pk=pk)
        if doc.speciality == 'Surgery':
            form = SurgeryHistoryModelForm(
                request.POST or None, instance=surgery_history_id)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.updated_by = request.user.id
                obj.save()
                messages.success(
                    request, 'Surgical History was updated successfully.')
                return redirect('/dashboard/historytaking')
    context = {
        'title': 'Update History Taking',
        'surgery_form': form,
        'valueBtn': 'Update',
    }
    return render(request, 'dashboard/historytaking.html', context)


@login_required
def HistoryTakingDisplay(request):
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    history = ''
    total = ''
    queryset = ''
    docSpec = ''
    for doc in doctor:
        docSpec = doc.speciality
        if docSpec == 'Surgery':
            history = SurgeryHistory.objects.all().order_by('-created')
            queryset = request.GET.get('q')
            if queryset:
                queryset = SurgeryHistory.objects.filter(
                    Q(ticket__patient__id__icontains=queryset) | Q(ticket__patient__name__icontains=queryset))
                paginator = Paginator(queryset, 10)
                page = request.GET.get('page')
                history = paginator.get_page(page)
                total = queryset.count()

    context = {
        'title': 'History Taken',
        'history': history,
        'docSpec': docSpec,
        'total': total
    }
    return render(request, 'dashboard/historytaking.html', context)


@login_required
def LabRequestView(request):
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    total = ''
    queryset = request.GET.get('q')
    if queryset:
        for doc in doctor:
            queryset = Ticket.objects.filter(
                Q(patient__id__icontains=queryset), has_cancelled=0, is_active=0, doctor=doc).order_by('-created')
            total = queryset.count()
    context = {
        'queryset': queryset,
        'title': 'Laboratory Request',
        'total': total
    }
    return render(request, 'dashboard/labrequest.html', context)


@login_required
def LabRequestToGenerateView(request, pk):
    lab_group = ''
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    for doc in doctor:
        ticket = get_object_or_404(
            Ticket, pk=pk, has_cancelled=0, is_active=0, doctor=doc.id)
        lab_group = Lab_Group.objects.all()
        if request.POST.getlist('lab_test'):
            lab_test = request.POST.getlist('lab_test')
            laboratory = Lab.objects.filter(id__in=lab_test)
            lab_test_id = LabRequest.objects.filter(examined=0, paid=0, lab_test__in=lab_test, ticket__patient=ticket.patient.id)
            if lab_test_id:
                messages.success(
                     request, 'Some lab tests have not been examined.')
                return redirect('/dashboard/lab-request')
            else:
                instance = LabRequest.objects.create(
                    ticket=ticket, created_by=request.user.id)
                instance.lab_test.add(*laboratory)
                messages.success(
                    request, 'Lab Request has been sent successfully.')
                return redirect('/dashboard/lab-request')
    context = {
        'title': 'Laboratory Request',
        'valueBtn': 'Save',
        'lab_group': lab_group
    }
    return render(request, 'dashboard/laboratory_request.html', context)


@login_required
def LabRequestDisplay(request):
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    labrequest = ''
    total = ''
    queryset = ''
    for doc in doctor:
        labrequest = LabRequest.objects.filter(
            ticket__doctor=doc.id, examined=0, paid=0).order_by('-created')
        paginator = Paginator(labrequest, 10)
        page = request.GET.get('page')
        labrequest = paginator.get_page(page)
        queryset = request.GET.get('q')
        if queryset:
            queryset = LabRequest.objects.filter(
                Q(ticket__patient__id__icontains=queryset) | Q(ticket__patient__name__icontains=queryset), examined=0, paid=0)
            paginator = Paginator(queryset, 10)
            page = request.GET.get('page')
            labrequest = paginator.get_page(page)
            total = queryset.count()

    context = {
        'title': 'Laboratory Requested List',
        'labrequest': labrequest,
        'total': total
    }
    return render(request, 'dashboard/laboratory_request_view.html', context)



@login_required
def LabRequestUpdateView(request, pk):
    lab_group = ''
    doctor = Doctor.objects.filter(user_id=request.user.id, active='Yes')
    for doc in doctor:
        lab_request_id = get_object_or_404(
            LabRequest, pk=pk, ticket__doctor=doc.id)
        form = LabRequestModelForm(
            request.POST or None, instance=lab_request_id)
        lab_group = Lab_Group.objects.all()
        if request.POST.getlist('lab_test'):
            lab_test = request.POST.getlist('lab_test')
            laboratory = Lab.objects.filter(id__in=lab_test)
            lab_test_id = LabRequest.objects.filter(
                examined=0, paid=0, lab_test__in=lab_test, ticket__patient=ticket.patient.id)
            if lab_test_id:
                messages.success(
                    request, 'Some lab tests have not been examined.')
                return redirect('/dashboard/lab-request')
            else:
                instance = LabRequest.objects.update(
                    ticket=ticket, created_by=request.user.id)
                instance.lab_test.set(*laboratory)
                messages.success(
                    request, 'Lab Request has been sent successfully.')
                return redirect('/dashboard/lab-request')
    
    context = {
        'title': 'Laboratory Request',
        'valueBtn': 'Save',
        'lab_group': lab_group,
        'lab_request_id': lab_request_id,
        'form':form
    }
    return render(request, 'dashboard/laboratory_request.html', context)

@login_required
def LabRequestPrintView(request, pk):
    lab_request = get_object_or_404(
        LabRequest, pk=pk, examined=0, paid=0)
    context = {
        'lab_request': lab_request,
        'being': 'Lab Request',
        'user': request.user,
        'today': date.today(),     
    }
    return render(request, 'dashboard/lab_request_print.html', context)
