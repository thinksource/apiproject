from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from pulse.models import Pulse
from pulse.serializers import PulseSerializer
from rest_framework import permissions
from django.core.paginator import Paginator
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#        'users': reverse('users:user-list', request=request, format=format),
#        'todos': reverse('todos:todo-list', request=request, format=format),
# })

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

class PulseList(generics.ListCreateAPIView):

    serializer_class= PulseSerializer
    permission_class = (permissions.AllowAny)

    def get_queryset(self, page=0):
        paginator = Paginator(Pulse.objects.all(), 5)
        return paginator.get_page(page)

    def list(self, request):
        page=request.GET.get('page',0)
        queryset = self.get_queryset(page)
        serializer = PulseSerializer(queryset, many=True)
        return Response(serializer.data)


class PulseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PulseSerializer
    permission_class = (permissions.AllowAny)
    # http_method_names = ['get', 'post', 'put']

    def get_queryset(self, pid):
        # print(dir(Pulse.objects))
        return Pulse.objects.get(pk=pid)
       
    # def post_queryset(self,pid):
    #     s = PulaseSerializer(data=self.request.data)
    #     instance=Pulase.objects.get(pk=pid)

    #     if instance:
    #         if s.is_valid():
    
    #     else:
    #         if s.is_valid():
    #             s.save()
    #             return Response(s.data, status=status.HTTP_201_CREATED)
    #     return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        id=kwargs.get('pk',1)
        # print(id)
        queryset=self.get_queryset(id)
        serializer = PulseSerializer(queryset)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        id=kwargs.get('pk',1)
        instance=self.get_queryset(id)
        if instance:
            return self.put(request, *args, **kwargs)
        else:
            s = PulaseSerializer(data=self.request.data)
            if s.is_valid():
                s.save()
                return Response(s.data, status=status.HTTP_201_CREATED)
        
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        id=kwargs.get('pk',1)
        instance=self.get_queryset(id)
        instance.name=request.data.get("name", instance.name)
        instance.ctype=request.data.get("type", instance.ctype)
        instance.maximum_rabi_rate=request.data.get("maximum_rabi_rate",instance.maximum_rabi_rate)
        instance.polar_angle=request.data.get("polar_angle",instance.polar_angle)
        instance.save()
        serializer = PulseSerializer(instance)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)

class PulseCreate(generics.CreateAPIView):
    queryset = Pulse.objects.all()
    serializer_class= PulseSerializer

    def post_queryset(self):
        s=PulaseSerializer(data=self.request.data)
        print(self.request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
 