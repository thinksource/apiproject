from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from pulse.models import Pulse
from pulse.serializers import PulseSerializer
from rest_framework import permissions
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
import json
from myproject import settings
from myproject.utils import csvParser
from django.http import HttpResponse


class PulseList(generics.ListCreateAPIView):
    http_method_names = ['get']
    serializer_class = PulseSerializer
    permission_class = (permissions.AllowAny)

    def get_queryset(self, page=1):
        paginator = Paginator(Pulse.objects.all(), settings.REST_FRAMEWORK['PAGE_SIZE'])
        return paginator.get_page(page)

    def list(self, request):
        page = request.GET.get('page', 1)
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

    def post_queryset(self):
        s = PulseSerializer(data=self.request.data)
        # print(self.request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk', 1)
        # print(id)
        try:
            queryset = self.get_queryset(id)
        except ObjectDoesNotExist as e:
            error = {"error": "No object found by id:"+str(id)}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = PulseSerializer(queryset)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if id:
            try:
                instance = self.get_queryset(id)
            except ObjectDoesNotExist:
                return self.post_queryset()
            else:
                return self.put(request, *args, **kwargs)
        else:
            return self.post_queryset()

    def put(self, request, *args, **kwargs):
        id = kwargs.get('pk', 1)
        try:
            instance = self.get_queryset(id)
        except ObjectDoesNotExist as e:
            error = {"error": "No object found by id:"+str(id)}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = PulseSerializer(instance)
            serializer.update(instance, request.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            instance = self.get_queryset(id)
        except ObjectDoesNotExist as e:
            error = {"error": "No object found by id:"+str(id)}
            return Response(error, status=status.HTTP_404_NOT_FOUND)
        else:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class PulseCreate(generics.CreateAPIView):
    queryset = Pulse.objects.all()
    http_method_names = ['post']
    serializer_class = PulseSerializer

    def post_queryset(self):
        s = PulaseSerializer(data=self.request.data)
        # print(self.request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(APIView):
    http_method_names = ['post', 'get']
    serializer_class = PulseSerializer
    permission_class = (permissions.AllowAny)
    parser_classes = (MultiPartParser,)

    def get_queryset(self):
        return super(FileUploaderView, self).get_queryset()

    def post(self, request, filename="file", format=None):
        file_keys = list(request.FILES.keys())
        update_items = []
        for key in file_keys:
            file_obj = request.FILES[key]
            update_items.extend(csvParser.readercsv(file_obj))
            for i in update_items:
                s = PulseSerializer(data=i)
                if s.is_valid():
                    s.save()
        return Response(update_items, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        outputfile=csvParser.writecsv(Pulse.objects.all())
        response = HttpResponse(outputfile.getvalue(), content_type='text/csv')

        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        # response['X-Sendfile'] = outputfile.getvalue()
        
        return response
