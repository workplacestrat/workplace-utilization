from .models import Client, Project, Building
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id','client_name','client_industry')

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = Project
        fields = ('id','client', 'project_name','project_type')
        extra_kwargs = {
                'project_name': {'validators': []},
                }

    def create(self, validated_data):
        client_data = validated_data.pop('client')
        c , created = Client.objects.get_or_create(client_name=client_data['client_name'])

        newp = Project.objects.create(client=c, **validated_data)
        return newp

class ProjectSerializerMini(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'project_name','project_type')
        extra_kwargs = {
                'project_name': {'validators': []},
                }
class BuildingSerializerMini(serializers.ModelSerializer):


    class Meta:
        model = Building
        fields = ('id', 'building_name', 'building_address')
        extra_kwargs = {
            'building_name': {'validators': []},
            'building_address': {'validators': []}
            }


class BuildingSerializer(serializers.ModelSerializer):

    project = ProjectSerializer()

    class Meta:
        model = Building
        fields = ('id', 'project','building_name', 'building_address')
        extra_kwargs = {
            'building_name': {'validators': []},
            'building_address': {'validators': []}
            }


    def create(self, validated_data):
        project_data = validated_data.pop('project')
        client_data = project_data.pop('client')
        p, created  = Project.objects.get_or_create(project_name=project_data['project_name'])
        c, created = Client.objects.get_or_create(client_name=client_data['client_name'])
        newb = Building.objects.create(project=p, **validated_data)
        return newb
