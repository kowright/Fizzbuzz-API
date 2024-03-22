#endpoints
from lib2to3.fixes.fix_apply import FixApply
from django.http import JsonResponse
from .models import Fizzbuzz
from .serializers import FizzBuzzSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

@swagger_auto_schema(
    method='GET',
    operation_summary="Get a list of all fizzbuzzes",
    operation_description="A list of all fizzbuzzes.",
    responses={200: "OK"}
)
@swagger_auto_schema(
    method='POST',
    operation_summary="Create a new fizzbuzz",
    operation_description="A new fizzbuzz is created.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["message"],
        properties={
            'fizzbuzz_id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'useragent': openapi.Schema(type=openapi.TYPE_STRING),
            'creation_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
            'message': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ),
    responses={200: "Retrieved", 201: "Created", 400: "Could not create"}
)
@api_view(['GET', 'POST'])

def fizzbuzz(request):
   
    if request.method == 'GET':
        fizzbuzzes = Fizzbuzz.objects.all()
        serializer = FizzBuzzSerializer(fizzbuzzes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        useragent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        data = request.data.copy() 
        data['useragent'] = useragent 
        serializer = FizzBuzzSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='GET',
    operation_summary="Get a single fizzbuzz",
    operation_description="Get a single fizzbuzz.",
    responses={
        200: openapi.Response(
            description="OK",
            schema=FizzBuzzSerializer,
        ), 404: "NOT FOUND"}
)
@api_view(['GET'])
def fizzbuzz_detail(request, id): 
    try: 
        fizz = Fizzbuzz.objects.get(pk=id)
    except Fizzbuzz.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    Fizzbuzz.objects.get(pk=id)
    if request.method == 'GET':
        serializer = FizzBuzzSerializer(fizz)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FizzBuzzViewSet(viewsets.ModelViewSet):
    queryset = Fizzbuzz.objects.all()
    serializer_class = FizzBuzzSerializer

