from rest_framework import generics, mixins, response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import UserAct
from datetime import datetime
import requests,pytz
from .serializers import UserActSerializer,RegisterSerializer
from rest_framework.response import Response

class ListUsers(generics.ListAPIView,mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserActSerializer
    queryset = UserAct.objects.all()

    def get(self,request):

        global st
        global tz
        st=''
        client_ip = request.META.get("HTTP_X_FORWARDED_FOR")
        if not client_ip:
            client_ip = request.META.get("REMOTE_ADDR")
        ip_dtl = requests.get('https://ipapi.co/{}/json/'.format(client_ip)).json()
        tz=ip_dtl['timezone']
        st=datetime.now(tz=pytz.timezone(tz)).strftime("%b %d %Y  %I:%M %p")
        print("ST  ",st)
        res= {
            'ok':True,
            'members':self.get_queryset().values('id','real_name','list_act')
        }
        return Response(res)

    def logoutt(self,request):

        global st
        global tz
        print("St from Logout : ", st)
        et = datetime.now(tz=pytz.timezone(tz)).strftime("%b %d %Y  %I:%M %p")
        session_time = {"tz": tz, "start_time": st, "end_time": et}
        print("ET ", et)
        u_act = self.get_queryset().get(username=request.user.username)
        u_act.list_act.append(session_time)
        u_act.save()
        request.session.flush()
        request.session.set_expiry(1)
        return

class Logout(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        log=ListUsers()
        log.logoutt(request)
        return Response("Logged Out")


class Register(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    queryset = UserAct.objects.all()

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user=serializer.save()
            data['response']="Successfully registered"
            data['username'] = user.username
        else:
            data= serializer.errors
        return response.Response(data)
