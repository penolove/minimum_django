from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import time
import json
def index(request):
    return render(request, 'polls/index.html')

@csrf_exempt
def donate(request):
    if request.method == 'POST':
        print(request.POST);
        time.sleep(1);
        return HttpResponse(json.dumps({"689":123,"426":92}), content_type='application/json')
