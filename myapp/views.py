from django.shortcuts import render

# Create your views here.
def sample(request):
    context = {
        'names' : ["Vamshi","krishna","Chandra"]
    }
    return render(request, 'index.html',context)