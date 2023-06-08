from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponseBadRequest, HttpRequest
from django import db
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShortUrl, ShortUrlStats
from .shortie_utils import generate_shortcode


@api_view(['GET'])
def get_url(request, shortcode: str):
    """
    Returns the full URL for the given short url.
    """
    try:
        short_url = ShortUrl.objects.get(shortcode=shortcode)
        short_url_stats = ShortUrlStats.objects.get(shortcode=shortcode)
        short_url_stats.times_accessed += 1
        short_url_stats.save()
        return HttpResponseRedirect(short_url.full_url)
    except:
        raise Http404


class GenerateShortUrl(APIView):

    def post(self, request: HttpRequest, format=None):
        full_url = request.POST.get('url')
        short_url = _create_short_url(full_url)
        ShortUrlStats.objects.create(shortcode=short_url)
        return Response({
            'short_url': f'{request.build_absolute_uri(short_url.shortcode)}'.replace('/getshorturl', ''),
            'full_url': full_url
        })


def _create_short_url(url: str, max_retry=4):
    num_attempts = 0

    # hardocded to admin for now
    user = User.objects.get(id=1)

    while num_attempts < max_retry:
        try:
            shortcode = generate_shortcode(length=4)
            new_shorturl = ShortUrl(user=user, full_url=url, shortcode=shortcode)
            new_shorturl.save()
            return new_shorturl
        except db.IntegrityError:
            num_attempts += 1
    return None
