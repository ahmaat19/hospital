from django import template
from dashboard.models import Ticket

register = template.Library()


@register.simple_tag
def check_patient_already_exists(request, pk):
    return Ticket.objects.filter(patient=pk, is_active=1, has_cancelled=0).exists()
