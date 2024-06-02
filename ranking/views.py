from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def ranking_views(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'ranking.html', context)