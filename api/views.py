from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ShortUrl

# Create your views here.
# https://www.django-rest-framework.org/tutorial/2-requests-and-responses/


@api_view(['GET'])
def get_url(request, shortcode: str):
    """
    Returns the full URL for the given short url.
    """
    try:
        short_url = ShortUrl.objects.get(shortcode=shortcode)
        return HttpResponseRedirect(short_url.full_url)
    except:
        raise Http404
