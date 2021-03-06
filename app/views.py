from django.shortcuts import render
from rest_framework import permissions,authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics,mixins
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q

###For generating manual tokens
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class StatusListAPI(APIView):
    permission_classes=[]
    authentication_classes=[]

    def get(self,request,format=None):
        qs=Status.objects.all()
        data=StatusSerializer(qs,many=True)
        return Response(data.data)
    def post(self,request,format=None):
        qs=Status.objects.all()
        data=StatusSerializer(qs,many=True)
        return Response(data.data)
class StatusAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

    def get_queryset(self):
        qs=Status.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(content__icontains=query)
        return qs
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class StatusGETApi(APIView):
    permission_classes=[]
    authentication_classes=[]
    def get(self,request,*args,**kwargs):
        try:
            qs=Status.objects.get(id=kwargs['id'])
            serializer=StatusSerializer(qs)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response("Nahi hai object")
        # if qs.exists():
        #     return Response(StatusSerializer(qs[0]).data)
        # else:
        #     return Response("Gand mara")
class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    #def perform_create(self,serializer):
    def get_serializer(self, instance=None, data=None,many=False,partial=False):
         return super(StatusCreateAPIView, self).get_serializer(instance=instance, data=data, many=True, partial=partial)
class StatusDetailAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'
class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'
class StatusView(mixins.CreateModelMixin,generics.ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer

    def get_queryset(self):
        qs=Status.objects.all()
        q=self.request.GET.get('q')
        if q is not None:
            qs=qs.filter(content__icontains=q)
        return qs
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class StatusView1(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[]
    authentication_classes=[]
    queryset=Status.objects.all()
    serializer_class=StatusSerializer
    lookup_field='id'
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)

class AuthView(APIView):
    authentication_classes=[]
    permission_classes=[permissions.AllowAny]
    def post(self,request,*args,**kwargs):
        print(request.user)
        data=request.POST.get('hello')
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        x=User.objects.create_user(username=username,password=password,email=email)
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                print(request.user)
                return Response({'loggedIN':'Ho gaye login'})
        return Response({'token':'hello'})

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class LoginView(APIView):
    authentication_classes=[]
    permission_classes=[permissions.AllowAny]
    def post(self,request,*args,**kwargs):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        qs=User.objects.filter(
            Q(username__iexact=username) |
            Q(email__iexact=username)##We can also use email here
        )
        if qs.count()==1:
            user_obj=qs.first()
            if user_obj.check_password(password):
                user=user_obj
                return Response(get_tokens_for_user(user))
        return Response({"error":"Sorry bro nahi ho paega"})


class RegisterSerializerView(generics.CreateAPIView):
    permission_classes=[permissions.AllowAny]
    authentication_classes=[]
    queryset=User.objects.all()
    serializer_class=RegisterSerializer



