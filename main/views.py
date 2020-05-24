from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models import *
from base58 import b58encode_int, b58decode_check, b58decode_int


class Alias(APIView):
    def get(self, request, alias=None):
        print("alias:", alias)
        if alias:
            # if b58decode_check(alias):
            #     return Response(data="Incorrect alias", status=400, content_type="text/plain")
            pk = b58decode_int(alias)
            result = URLAlias.objects.get(pk=pk)
            return Response(status=302, headers={"Location": result.url})
        else:
            return Response(data="<p>It works!</p>")


class Shorten(APIView):
    @staticmethod
    def url_is_correct(url):
        return True

    def post(self, request):
        if "url" in request.data and self.url_is_correct(request.data["url"]):
            url = request.data["url"]
            if len(URLAlias.objects.filter(url=url)) == 0:
                newAlias = URLAlias.objects.create(url=url)
            else:
                newAlias = URLAlias.objects.filter(url=url)[0]
            retAlias = b58encode_int(newAlias.id)
            return Response(data=retAlias, status=201, content_type="text/plain")
        else:
            return Response(data="The URL is absent or incorrect", status=400, content_type="text/plain")
