from django.http import HttpResponse
def home1(request):
    html = "<p style='text-align:center;font-size:40px'>Hello World</p>"
    return HttpResponse(html)