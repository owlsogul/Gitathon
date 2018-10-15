from django.shortcuts import redirect, render

# Create your views here.
def main(request, teamId):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/main.html', {
            'memberId':request.session['memberId'],
            'teamId':teamId,
        })

def create(request):
    if not 'memberId' in request.session:
        return redirect('/lobby')
    else:
        return render(request, 'teamproject/create.html', {
            'memberId':request.session['memberId'],
        })

def create_process(request):
    return render(request, 'teamproject/create.html', {})
