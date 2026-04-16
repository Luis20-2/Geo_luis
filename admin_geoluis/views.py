import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema

from core_api.parsers import PlainTextJSONParser


class MobileAuthRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class MobileAuthResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    username = serializers.CharField()
    token = serializers.CharField()
    access = serializers.CharField()
    refresh = serializers.CharField()


def build_auth_response(user, message, http_status):
    token, _ = Token.objects.get_or_create(user=user)
    refresh = RefreshToken.for_user(user)
    return Response({
        'message': message,
        'username': user.username,
        'token': token.key,
        'access': str(refresh.access_token),
        'refresh': str(refresh),
    }, status=http_status)


@ensure_csrf_cookie
def home(request):
    context = {
        "message": "Hola a todos"
    }

    return render(request, 'login.html', context)


@ensure_csrf_cookie
def panel(request):
    context = {
        "message": "Hola a todos"
    }

    return render(request, 'index.html', context)


@require_POST
def register_user(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'JSON inválido'}, status=400)

    username = (payload.get('username') or '').strip()
    password = payload.get('password') or ''
    password2 = payload.get('password2') or ''

    if not username or not password or not password2:
        return JsonResponse({'error': 'Todos los campos son obligatorios'}, status=400)
    if password != password2:
        return JsonResponse({'error': 'Las contraseñas no coinciden'}, status=400)
    if len(password) < 6:
        return JsonResponse({'error': 'La contraseña debe tener al menos 6 caracteres'}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'El usuario ya existe'}, status=400)

    user = User.objects.create_user(username=username, password=password)
    login(request, user)
    token, _ = Token.objects.get_or_create(user=user)
    return JsonResponse({'message': 'Usuario creado', 'username': user.username, 'token': token.key}, status=201)


@extend_schema(
    tags=['Autenticación'],
    request=MobileAuthRequestSerializer,
    responses={201: MobileAuthResponseSerializer},
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser, FormParser, MultiPartParser, PlainTextJSONParser])
def mobile_register(request):
    username = (request.data.get('username') or '').strip()
    password = request.data.get('password') or ''

    if not username or not password:
        return Response({'error': 'Usuario y contraseña son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)
    if len(password) < 6:
        return Response({'error': 'La contraseña debe tener al menos 6 caracteres'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).exists():
        return Response({'error': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return build_auth_response(user, 'Usuario creado', status.HTTP_201_CREATED)


@extend_schema(
    tags=['Autenticación'],
    request=MobileAuthRequestSerializer,
    responses={200: MobileAuthResponseSerializer},
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser, FormParser, MultiPartParser, PlainTextJSONParser])
def mobile_login(request):
    username = (request.data.get('username') or '').strip()
    password = request.data.get('password') or ''

    if not username or not password:
        return Response({'error': 'Usuario y contraseña son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

    return build_auth_response(user, 'Login correcto', status.HTTP_200_OK)


@extend_schema(
    tags=['Autenticación'],
    request=MobileAuthRequestSerializer,
    responses={200: MobileAuthResponseSerializer},
)
@api_view(['POST'])
@permission_classes([AllowAny])
@parser_classes([JSONParser, FormParser, MultiPartParser, PlainTextJSONParser])
def jwt_login(request):
    username = (request.data.get('username') or '').strip()
    password = request.data.get('password') or ''

    if not username or not password:
        return Response({'error': 'Usuario y contraseña son obligatorios'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=username, password=password)
    if not user:
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

    return build_auth_response(user, 'Login JWT correcto', status.HTTP_200_OK)