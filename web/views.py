# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests, json, socket
from django.shortcuts import render

def index(request):
    return render(request, 'web/index.html', {})

def details(request, ip_str):
    url = "http://freegeoip.net/json/" + str(ip_str)
    req = requests.get(url=url[:-1])
    data = json.loads(req.text)
    hst = socket.gethostbyaddr(ip_str[:-1])[0]
    return render(request, 'web/detail.html', {'data':data, 'host':hst})
