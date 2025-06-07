import json
from django.shortcuts import render
from .models import Requestlog
from django.db.models import Count

def home(request):
    logs = Requestlog.objects.all().order_by('-timestamp')[:50]

    status_data = (
        Requestlog.objects
        .values('status_code')
        .annotate(count=Count('status_code'))
        .order_by('status_code')
    )

    status_labels = [str(item['status_code']) for item in status_data]
    status_counts = [item['count'] for item in status_data]

    context = {
        'logs': logs,
        'status_labels': json.dumps(status_labels),  
        'status_counts': json.dumps(status_counts),  
    }

    return render(request, 'loggerapp/home.html', context)
