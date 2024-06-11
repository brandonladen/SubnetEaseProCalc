from .models import SubnettingHistory

def subnet_history(request):
    if request.user.is_authenticated:
        history = SubnettingHistory.objects.filter(user=request.user)
        return {'history': history}
    return {}