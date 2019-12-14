from django.urls import path
from . import views


app_name = 'dashboard'

urlpatterns = [
    path('', views.IndexView, name='Index'),

    path('employee/', views.EmployeeView, name='employee'),
    path('employee/<int:pk>/update/',
         views.EmployeeUpdateView, name='employee_update'),

    path('doctor/', views.DoctorView, name='doctor'),
    path('doctor/<int:pk>/update/',
         views.DoctorUpdateView, name='doctor_update'),

    path('department/', views.DepartmentView, name='department'),
    path('department/<int:pk>/update/',
         views.DepartmentUpdateView, name='department_update'),

    path('room/', views.RoomView, name='room'),
    path('room/<int:pk>/update/', views.RoomUpdateView, name='room_update'),

    path('drug/', views.DrugView, name='drug'),
    path('drug/<int:pk>/update/', views.DrugUpdateView, name='drug_update'),

    path('laboratory/', views.LabView, name='laboratory'),
    path('laboratory/<int:pk>/update/',
         views.LabUpdateView, name='laboratory_update'),

    path('operation/', views.OperationView, name='operation'),
    path('operation/<int:pk>/update/',
         views.OperationUpdateView, name='operation_update'),

    path('service/', views.ServiceView, name='service'),
    path('service/<int:pk>/update/',
         views.ServiceUpdateView, name='service_update'),

    path('image/', views.ImageView, name='image'),
    path('image/<int:pk>/update/',
         views.ImageUpdateView, name='image_update'),

    path('delivery/', views.DeliveryView, name='delivery'),
    path('delivery/<int:pk>/update/',
         views.DeliveryUpdateView, name='delivery_update'),

    path('sponsor/', views.SponsorView, name='sponsor'),
    path('sponsor/<int:pk>/update/',
         views.SponsorUpdateView, name='sponsor_update'),

    path('diagnose/', views.DiagnoseView, name='diagnose'),
    path('diagnose/<int:pk>/update/',
         views.DiagnoseUpdateView, name='diagnose_update'),

    path('patient/', views.PatientView, name='patient'),
    path('patient/<int:pk>/update/',
         views.PatientUpdateView, name='patient_update'),

    path('ticket/', views.TicketView, name='ticket'),
    path('ticket/<int:pk>/', views.TicketToGenerateView, name='ticket_to'),
    path('ticket/<int:pk>/cancel/',
         views.TicketCancelView, name='ticket_cancel'),
    path('ticket/<int:pk>/update/',
         views.TicketUpdateView, name='ticket_update'),
    path('ticket/print/<int:pk>/', views.TicketPrintView, name='ticket_print'),

    path('history/', views.HistoryView, name='history'),
    path('historytaking/<int:pk>/',
         views.HistoryTakingView, name='history_taking'),
    path('historytaking/<int:pk>/update/',
         views.HistoryTakingUpdateView, name='history_taking_update'),
    path('historytaking/', views.HistoryTakingDisplay, name='historytaking'),

    path('lab-request/', views.LabRequestView, name='lab_request'),
    path('laboratory-request/<int:pk>/',
         views.LabRequestToGenerateView, name='laboratory_request'),
    path('laboratory-request/', views.LabRequestDisplay, name='l_request_view'),
    path('laboratory-request/<int:pk>/update/',
         views.LabRequestUpdateView, name='laboratory_request_update'),
    path('lab-request/print/<int:pk>/',
         views.LabRequestPrintView, name='lab_request_print'),

]
