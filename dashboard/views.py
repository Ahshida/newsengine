from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import json

from forms import SearchForm
from webhoseProcess import Process
from alchemyConnect import AlchemyConnect
import os
from django.conf import settings
from django.template import RequestContext
# Create your views here.


def render_dashboard(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            val = form.cleaned_data['searchTerm']
            obj = Process()
            result = obj.processing(val)
            return render(request, 'dashboard.html', {'data': result, 'form': form})
    else:
        form = SearchForm()

    return render(request, 'dashboard.html', {'form': form})


def render_dash(request):
    if request.method == 'POST':
        params = request.POST
        val = params.get('keyword')
        obj = Process()
        result = obj.processing(val)
        return render(request, 'dash.html', {'resultSet': result})
    else:
        form = SearchForm()

    return render(request, 'dash.html', {'form': form})

def render_analysis(request):
    print "hey"
    if request.method == 'POST':
        params = request.POST
        val = params.get('reqUrl')
        al = AlchemyConnect()
        al.entityExtraction(val)
        return HttpResponse(json.dumps({'name': val}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'name': 'fail'}), content_type="application/json")

def render_treemap(request):
    print "inside Treemap"
    template="treemap.html"
    return render_to_response(template, ontext_instance=RequestContext(request))

def render_json(request):
    print "inside json rendering to Treemap"
    file_path_read = os.path.join(settings.BASE_DIR, 'entity_current.json')
    print "*****-"+file_path_read
    with open(file_path_read, 'r') as frender:
        data = frender.read()
        print data
    return HttpResponse(data, content_type="application/json")