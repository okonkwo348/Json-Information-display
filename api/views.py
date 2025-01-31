from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def get_inform(request):
    email="okonkwoemmanuel348@gmail.com"
    current_datetime=datetime.now().isoformat() + "Z"
    github_url="https://github.com/okonkwo348"

    msg={
        "email":email,
        "current_datetime":current_datetime,
        "github_url":github_url
    }
    return Response(msg)
