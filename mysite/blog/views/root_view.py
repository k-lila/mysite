from django.http import HttpResponse
from django.views import generic

class RootView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('RootView')