from .models import Client, Project, Building
from .serializers import ProjectSerializer, ClientSerializer, BuildingSerializer, ProjectSerializerMini, BuildingSerializerMini

from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ClientList(APIView):

    def get(self, request, format=None):
        clients = Client.objects.all()
        serialized_clients=ClientSerializer(clients, many=True)
        return Response(serialized_clients.data)

    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectList(APIView):

    def get(self, request, client, format=None):

        client = client
        c = Client.objects.select_related('Project').get(pk=client)
        projects = Project.objects.filter(client=c)
        serialized_projects=ProjectSerializerMini(projects, many=True)
        return Response(serialized_projects.data)

    def post(self, request, client, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BuildingList(APIView):

    def get(self, request, client, project , format=None):

        project = project
        p = Project.objects.select_related('Building').get(pk=project)
        buildings = Building.objects.filter(project=p)
        serialized_buildings=BuildingSerializerMini(buildings, many=True)
        return Response(serialized_buildings.data)

    def post(self, request, client, project, format=None):
        serializer = BuildingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
