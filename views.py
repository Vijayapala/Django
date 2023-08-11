from django.http import HttpResponse
def home(request):
    html = "<p style='text-align:center;font-size:40px'>This is my first project</p>"
    return HttpResponse(html)