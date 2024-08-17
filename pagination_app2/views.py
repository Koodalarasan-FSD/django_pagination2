from django.shortcuts import render
from apps.home.models import EmailNotification
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def notification_view(request):

    # Fetch email datas
    email_data = EmailNotification.objects.all().order_by('-created_date')

    # Get the number of items per page from GET parameters, default to 10
    per_page = request.GET.get('per_page', 10)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10

    # Pagination
    paginator = Paginator(email_data, per_page)
    page = request.GET.get('page')
    try:
        email_data = paginator.page(page)
    except PageNotAnInteger:
        email_data = paginator.page(1)
    except EmptyPage:
        email_data = paginator.page(paginator.num_pages)

    # sending per_page and email_data with pagination
    return render(request, 'notifications.html', {'email_data': email_data, 'per_page': per_page})
