from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returndobject = HttpResponse("<h1>hello world<h1>")
    return returndobject

class HelloWorldClass(TemplateView):
    template_name = 'hello.html'