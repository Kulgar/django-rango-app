from django.http import HttpResponse

def index(request):
  return HttpResponse("Rango say hey there world! <a href='/rango/about'>About</a>")

def about(request):
  return HttpResponse("About page <a href='/rango/'>Index</a>")
