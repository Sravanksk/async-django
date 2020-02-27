from django.http import JsonResponse
from django_q.tasks import async_task


def index(request):
    payload = {
        'data': 'making async call with Django Q'
    }
    async_task("async_demo.utility.sleep_and_run_task", 7)
    return JsonResponse(payload)
