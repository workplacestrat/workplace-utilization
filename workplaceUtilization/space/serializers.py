from .models import dayRecord, spaceRecord, Space, Study
from clients.models import Building
from clients.serializers import BuildingSerializer
from rest_framework import serializers

class StudySerializer(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ('id','study_name','study_provider','dynamic')
        extra_kwargs = {
            'id': {'read_only': False},
            'study_name': {'validators': []}
            }

class StudyGrabber(serializers.ModelSerializer):
    class Meta:
        model = Study
        fields = ('id','study_name','study_provider')
        extra_kwargs = {
            'id': {'read_only': False},
            'study_name': {'validators': []}
            }



class SpaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ('space_name', 'space_type','space_data')

class SpaceGrabber(serializers.ModelSerializer):

    class Meta:
        model = Space
        fields = ('space_name','space_type')



class SpaceWriter(serializers.ModelSerializer):

    building = BuildingSerializer()

    class Meta:
        model = Space
        fields = ('building', 'space_name', 'space_type','space_data')

    def create(self, validated_data):
            building_data = validated_data.pop('building')
            b , created = Building.objects.get_or_create(building_name=building_data['building_name'])

            newsp = Space.objects.create(building=b, **validated_data)
            return newsp

class SpaceBulkWriter(serializers.ListSerializer):
    def create(self, validated_data):
        study_data = validated_data[0]['study']
        st, created = Study.objects.get_or_create(pk=study_data['id'])
        spaces = []
        for i in validated_data:
            n = i['space']['space_name']
            if n not in spaces:
                spaces.append(n)
        records = []
        for s in spaces:
            sp, created = Space.objects.get_or_create(space_name=s)
            vd = [i for i in validated_data if i['space']['space_name']==s]
            for item in vd:
                item.pop('study')
                item.pop('space')
                item['study'] = st
                item['space'] = sp
                records.append(spaceRecord(**item))
        return spaceRecord.objects.bulk_create(records)

class SpaceRecordWriter(serializers.ModelSerializer):
    space = SpaceGrabber()
    study = StudyGrabber()

    class Meta:
        model = spaceRecord
        fields = ('study','space','datetime','occ','pctmoment','pctspace','data')
        list_serializer_class = SpaceBulkWriter
    def create(self, validated_data):
        study_data = validated_data.pop('study')
        space_data = validated_data.pop('space')

        st, created = Study.objects.get_or_create(pk=study_data['id'])

        sp, created = Space.objects.get_or_create(space_name=space_data['space_name'])

        sr = spaceRecord.objects.create(study = st, space = sp, **validated_data)
        return sr


class SpaceRecordReader(serializers.ModelSerializer):
    space = SpaceSerializer()
    class Meta:
        model = spaceRecord
        fields = ('space','datetime','occ','pctmoment','pctspace','data')





class dayRecordVSerializer(serializers.ModelSerializer):

    class Meta:
        model = dayRecord
        fields = ('day','vacancy', 'peak')

class dayRecordCSerializer(serializers.ModelSerializer):

    study = StudySerializer()

    class Meta:
        model = dayRecord
        fields = ('study','day','vacancy', 'peak')

    def create(self, validated_data):
        study_data = validated_data.pop('study')
        s , created = Study.objects.get_or_create(pk=study_data['id'])

        news = dayRecord.objects.create(study=s, **validated_data)
        return news
