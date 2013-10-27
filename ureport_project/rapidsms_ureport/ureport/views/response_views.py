from django.db import transaction
from django.db.models import Q, Count
from django.views.decorators.http import require_GET
from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404, \
    render_to_response
from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required, \
    permission_required
from django.utils import simplejson
from django.utils.safestring import mark_safe
from rapidsms_httprouter.router import get_router
from rapidsms.messages.outgoing import OutgoingMessage
from models import Response,ResponseCategory
from rapidsms.contrib.locations.models import Location
from rapidsms.models import Connection, Backend
from eav.models import Attribute
from django.core.urlresolvers import reverse
from django.views.decorators.cache import cache_control
from django.conf import settings


from forms import *


def view_scouts_responses(req, pol):


    responses= Response.objects.filter(contact__groups__name='scout',poll__pk=pol)
    template = 'ureport/scout_poll_results.html'
    return render_to_response(template, {
        'responses': responses,
        })

   
def view_guides_responses(req, pol):

    responses= Response.objects.filter(contact__groups__name='guide',poll__pk=pol)
    template = 'ureport/guide_poll_results.html'
    return render_to_response(template, {
        'responses': responses,
        })
        
def view_redcross_responses(req, pol):

    responses= Response.objects.filter(contact__groups__name='redcross',poll__pk=pol)
    template = 'ureport/redcross_poll_results.html'
    return render_to_response(template, {
        'responses': responses,
        })
