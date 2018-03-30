from .models import Study, Space, dayRecord, spaceRecord
from .serializers import StudySerializer, SpaceSerializer, SpaceWriter, dayRecordCSerializer, SpaceRecordWriter, SpaceRecordReader, StudyGrabber, dayRecordVSerializer
from clients.models import Building
from django.http import Http404
from datetime import datetime
from datetime import timedelta

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class StudyList(APIView):

    def get(self, request, client,project,building, format=None):

        building = building
        b = Building.objects.get(pk=building)
        studies = Study.objects.filter(building=b)
        serialized_studies=StudyGrabber(studies, many=True)
        return Response(serialized_studies.data)

    def post(self, request, client, format=None):
        serializer = StudySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SpaceList(APIView):

    def get(self, request, client,project,building, format=None):

        building = building
        b = Building.objects.get(pk=building)
        spaces = Space.objects.filter(building=b)
        serialized_spaces=SpaceWriter(spaces, many=True)
        return Response(serialized_spaces.data)

    def post(self, request, client,project,building, format=None):
        serializer = SpaceWriter(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DayRecordList(APIView):

    def get(self, request, client, project, building, study, format=None):

        study = study
        s = Study.objects.get(pk=study)
        dr = dayRecord.objects.filter(study=s)
        serialized_drs = dayRecordVSerializer(dr, many=True)
        return Response(serialized_drs.data)
    def post(self, request, client, project, building, study, format=None):

        serializer = dayRecordCSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpaceRecordList(APIView):

    def get(self, request, client, project, building, study, format=None):
        first = datetime.strptime(self.request.query_params.get('first', None),'%m%d%Y')
        last = datetime.strptime(self.request.query_params.get('last', None),'%m%d%Y')+ timedelta(days=1)

        days = (last - first).days
        if (days <= 7):
            study = study
            s = Study.objects.get(pk=study)
            sr = spaceRecord.objects.filter(study=s, datetime__range = [first,last]).prefetch_related('space')
            serialized_srs = SpaceRecordReader(sr, many=True)
            ss = [{'name': s['space']['space_name'],'type': s['space']['space_type'], 'datetime': s['datetime'], 'occ': s['occ'], 'pctmoment': s['pctmoment'], 'pctspace': s['pctspace']} for s in serialized_srs.data]

            return Response(ss)
        else:
            return Response("Date Range is longer than one week")
    def post(self, request, client, project, building, study, format=None):

        serializer = SpaceRecordWriter(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpaceRecordListVIEW(APIView):

    def get(self, request, client, project, building, study, format=None):
        first = datetime.strptime(self.request.query_params.get('first', None),'%m%d%Y')
        last = datetime.strptime(self.request.query_params.get('last', None),'%m%d%Y')+ timedelta(days=1)

        days = (last - first).days
        if (days <= 7):
            study = study
            s = Study.objects.get(pk=study)
            sr = spaceRecord.objects.filter(study=s, datetime__range = [first,last])
            serialized_srs = SpaceRecordWriter(sr, many=True)
            return Response(serialized_srs.data)
        else:
            return Response("Date Range is longer than one week")
    def post(self, request, client, project, building, study, format=None):

        serializer = SpaceRecordWriter(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
