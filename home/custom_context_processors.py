from notif.models import BroadcastNotification
def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    return {'notifications': allnotifications}