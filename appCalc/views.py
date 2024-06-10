from django.shortcuts import render, redirect, get_object_or_404
import requests
from django.contrib.auth.decorators import login_required

from authentication.forms import userprofileform
from .models import SubnettingHistory
from django.views.decorators.http import require_http_methods


# Create your views here.
def landing_page(request):
    return render(request,'Arsha/index.html')
@login_required
def home(request):
    if request.method == 'POST':
        form = userprofileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = userprofileform(instance=request.user)
    context = {
        'form': form
    }
    return render(request, template_name='appCalc/index.html',context=context)


@login_required
def subnet(request):
    response_data = None
    error_message = None

    if request.method == 'POST':
        ipAddress = request.POST.get('ipAddress')
        subnet = request.POST.get('subnet')
        address = f"{ipAddress}/{subnet}"

        try:
            response = requests.get(f"https://networkcalc.com/api/ip/{address}")

            if response.status_code == 200:
                response_data = response.json()["address"]
            else:
                response_data = {"error": "Error: Invalid address!"}
            SubnettingHistory.objects.create(
                user=request.user,
                ipaddress=response_data['cidr_notation'],
                subnetmask=response_data['subnet_mask'],
                wildcardmask=response_data['wildcard_mask'],
                networkbits=response_data['subnet_bits'],
                networkadddress=response_data['network_address'],
                first_ip=response_data['first_assignable_host'],
                last_ip=response_data['last_assignable_host'],
                broadcast_address=response_data['broadcast_address']
            )
        except ConnectionError:
            error_message = "Failed to connect to the network service. Please check your internet connection and try again."
        except Exception as e:
            error_message = "An unexpected error occurred. Please check your internet and try again."
        # view_subnet_history(request)
    return render(request, 'appCalc/index.html', {"response": response_data, 'error_message': error_message})


@login_required
def view_subnet_history(request):
    history = SubnettingHistory.objects.filter(user=request.user)

    context = {
        'history': history
    }
    return render(request, 'core/base.html', context)


@login_required
@require_http_methods(["DELETE"])
def delete_subnet_history(request, pk):
    subnet = get_object_or_404(SubnettingHistory, pk=int(pk))
    subnet.delete()
    return redirect('home')
