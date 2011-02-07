from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.validators import email_re
from Crypto.PublicKey import RSA
import logging

@login_required
def key(request, template_name="dashbody/connect.html"):
    logging.debug('connect')
    return render_to_response(template_name, {
    }, context_instance=RequestContext(request))