from rest_framework import serializers
from .models import Folder, Document, Topic

class FolderSerializer(serializers.ModelSerializer):
      class Meta:
            model = Folder
            fields = '__all__'
            
class DocumentSerializer(serializers.ModelSerializer):
      class Meta:
            model = Document
            fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
      class Meta:
            model = Topic
            fields = '__all__'
            