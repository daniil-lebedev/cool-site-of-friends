from django.shortcuts import render

# Create your views here.
def renatoPage(request):
	return render(request, 'renato.html')