from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

class ListingList(APIView):
    def get(self, request):
        return Response({"message": "Listings endpoint - GET"})

class ListingDetail(APIView):
    def get(self, request, pk):
        return Response({"message": f"Listing detail endpoint - GET {pk}"})