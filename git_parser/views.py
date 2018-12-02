from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from logging import getLogger

from .tasks import test

logger = getLogger(__name__)

@csrf_exempt
def tasks(request):
    if request.method == 'POST':
        return _post_tasks(request)
    else:
        return JsonResponse({}, status=405)

def _post_tasks(request):
    message = request.POST['message']
    logger.debug('calling demo_task. message={0}'.format(message))
    test(message, repeat = 20)
    return JsonResponse({}, status=302)