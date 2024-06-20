from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from clients.forms import ClientStatusForm
from clients.models import Client


@login_required
def client_list(request):
    clients = Client.objects.filter(responsible_person=request.user.full_name)
    return render(request, 'client_list.html', {'clients': clients})


@login_required
def update_client_status(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientStatusForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            if request.accepts("text/html"):
                return JsonResponse({'status': 'success'}, status=200)
    return JsonResponse(data=None, status=400)
