from django.shortcuts import render

# Create your views here.
def main(request, teamId):
    return render(request, 'teamproject/main.html', {'teamId':teamId})

def create(request):
    return render(request, 'teamproject/create.html', {})

def create_process(request):
    return render(request, 'teamproject/create.html', {})
