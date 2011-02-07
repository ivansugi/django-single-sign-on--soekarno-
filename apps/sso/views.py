from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.validators import email_re
from Crypto.PublicKey import RSA
from django.views.decorators.csrf import csrf_exempt
import urllib2, urllib
from sso.models import Clients, SessionControl
import os

import logging

@login_required
def connect(request, template_name="sso/connect.html"):
    logging.debug('connect')
    return render_to_response(template_name, {
    }, context_instance=RequestContext(request))

@csrf_exempt
def login_server(request):
    if request.method == "OPTIONS": 
            response = HttpResponse()
            response['Access-Control-Allow-Origin'] = '*'
            response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
            response['Access-Control-Max-Age'] = 1000
            response['Access-Control-Allow-Headers'] = '*'
            return response

    logging.debug('connect123')
    if request.user.is_authenticated() :
        return HttpResponse("user is logged in")
    else :
        if request.method == 'POST':
            try :
                if email_re.match(request.POST['email']) :
                    user_login = authenticate(username=request.POST['username'], password=request.POST['password'])
                    if user_login is not None:
                        if user.is_active:
                            login(request, user_login)
                            return HttpResponse("user logged in")
                        else :
                            return HttpResponse("user is not active")
                    else :
                        return HttpResponse ("wrong id")
                    
                    
                else :
                    return HttpResponse("email error")
            except :
                return HttpResponse("no password or username taken")
                
@csrf_exempt                
def register (request) :
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = 1000
    response['Access-Control-Allow-Headers'] = '*'
    #response['Access-Control-Allow-Credentials'] = 'true'
    
    print request
    
    if request.user.is_authenticated() :
        response.write("<div id='status'>authenticated</div>")
        
        
    else :
        if request.method == 'POST':
            try :
                if email_re.match(request.POST['email']) :
                    user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                    user.is_active = True
                    user.save()
                    print('saving')
                    user_login = authenticate(username=request.POST['username'], password=request.POST['password'])
                    print('autheticating')
                    login(request, user_login)
                    print('login')
                    response.write("user has been created")
                
                    #return HttpResponse("user has been created")
                else :
                    response.write("email error")
                
                #return HttpResponse("email error")
            except :
                response.write("no password or username taken")
                #return HttpResponse("no password or username taken")
        else :
            response.write("hello")
            #return HttpResponse("hello")
    return response 

@csrf_exempt  
def check (request, user_id, token) :
    #if request.method == "OPTIONS": 
    user = User.objects.get(id=user_id)
    
    response = HttpResponse()
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
    response['Access-Control-Max-Age'] = 1000
    response['Access-Control-Allow-Headers'] = '*'
    try:
        return_string = "%s;%s;%s" % (user.id, user.username, user.email)
        response.write(return_string)
    except : 
        response.write("none")
    return response


def send(request, client):
    consumer = Clients.objects.get(name = client)
    if request.user.is_authenticated() :
        rand  = os.urandom(20).encode('hex')
        params = urllib.urlencode(dict(id=request.user.id, token=rand))
        
        urlConsumer = "%s/clients/consumer/" % consumer.url
        urlRedirect = "%s/clients/claim_data/%s" % (consumer.url, rand)
        req = urllib2.Request(urlConsumer)
        fd = urllib2.urlopen(req, params)
        req.headers['content-type'] = 'text/html; charset=windows-1251'

        print params
        print urlConsumer
        data = fd.read()
        print data
        fd.close()
        try :
            control =  SessionControl.objects.create()
            control.id=request.session.session_key
            control.client_token = rand
            control.save()
        except :
            pass
        return HttpResponseRedirect (urlRedirect)
    else :
        urlConsumer = "%s/clients/not_user/" % consumer.url
        return HttpResponseRedirect (urlConsumer)
        
@csrf_exempt    
def logout(request):
    logging.debug('connect123')
    if request.user.is_authenticated() :
        return HttpResponse("user is logged in")
    else :
        if request.method == 'POST':
            try :
                if email_re.match(request.POST['email']) :
                    user_login = authenticate(username=request.POST['username'], password=request.POST['password'])
                    if user_login is not None:
                        if user.is_active:
                            login(request, user_login)
                            return HttpResponse("user logged in")
                        else :
                            return HttpResponse("user is not active")
                    else :
                        return HttpResponse ("wrong id")
                    
                    
                else :
                    return HttpResponse("email error")
            except :
                return HttpResponse("no password or username taken")
