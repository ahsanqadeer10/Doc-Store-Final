from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Folder, Document, Topic
from .serializers import FolderSerializer, DocumentSerializer, TopicSerializer

# Create your views here.

# Index returns all API URLs
@api_view(["GET"])
def index(request):
      api_urls = {
            'Folders': 'folders/?created=<asc, dsc>&updated=<asc, dsc>&topic=<topic_id_1,topic_id_2,...>',
            'Folder Detail': 'folder-detail/<int:folder_id>/',
            'Folder Documents': 'folder-documents/<int:folder_id>/?created=<asc, dsc>&updated=<asc, dsc>&topic=<topic_id_1,topic_id_2,...>',
            'Folder Create': 'folder-create/',
            'Folder Update': 'folder-update/<int:folder_id>/',
            'Folder Delete': 'folder-delete/<int:folder_id>/',
            'Documents': 'documents/?created=<asc, dsc>&updated=<asc, dsc>&topic=<topic_id_1,topic_id_2,...>',
            'Document Detail': 'document-detail/<int:document_id>/',
            'Document Create': 'document-create/',
            'Document Update': 'document-update/<int:document_id>/',
            'Document Delete': 'document-delete/<int:document_id>/',
            'Topics': 'topics/',
            'Topic Detail': 'topic-detail/<int:topic_id>/',
            'Topic Create': 'topic-create/',
            'Topic Update': 'topic-update/<int:topic_id>/',
            'Topic Delete': 'topic-delete/<int:topic_id>/'
      }
      return Response(api_urls)


# Folders
@api_view(["GET"])
def folders(request):
      folders = Folder.objects.all()

      # Sorting and filtering dataset according to query parameters
      param_created = request.GET.get('created')
      param_updated = request.GET.get('updated')      
      param_topic = request.GET.get('topic')
      if param_created:
            if param_created == "asc":
                  folders = folders.order_by('created_at')
            elif param_created == "dsc":
                  folders = folders.order_by('-created_at')
      if param_updated:
            if param_updated == "asc":
                  folders = folders.order_by('updated_at')
            elif param_updated == "dsc":
                  folders = folders.order_by('-updated_at')
      if param_topic:
            param_topic = param_topic.split(",")
            folders = folders.filter(topic__in=param_topic).distinct()
      
      serializer = FolderSerializer(folders, many=True)
      return Response(serializer.data)


@api_view(["GET"])
def folderDetail(request, folder_id):
      folder = Folder.objects.get(id = folder_id)
      serializer = FolderSerializer(folder, many=False)
      return Response(serializer.data)


@api_view(["GET"])
def folderDocuments(request, folder_id):
      documents = Document.objects.filter(folder = folder_id)

     # Sorting and filtering dataset according to query parameters
      param_created = request.GET.get('created')
      param_updated = request.GET.get('updated')      
      param_topic = request.GET.get('topic')
      if param_created:
            if param_created == "asc":
                  documents = documents.order_by('created_at')
            elif param_created == "dsc":
                  documents = documents.order_by('-created_at')
      if param_updated:
            if param_updated == "asc":
                  documents = documents.order_by('updated_at')
            elif param_updated == "dsc":
                  documents = documents.order_by('-updated_at')
      if param_topic:
            param_topic = param_topic.split(",")
            documents = documents.filter(topic__in=param_topic).distinct()
 
      serializer = DocumentSerializer(documents, many=True)
      return Response(serializer.data)


@api_view(["POST"])
def folderCreate(request):
      serializer = FolderSerializer(data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)


@api_view(["POST"])
def folderUpdate(request, folder_id):
      folder = Folder.objects.get(id = folder_id)
      serializer = FolderSerializer(instance = folder, data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)


@api_view(["DELETE"])
def folderDelete(request, folder_id):
      folder = Folder.objects.get(id = folder_id)
      folder.delete()
      return Response(f"Folder {folder} successfully deleted!")


# Documents
@api_view(["GET"])
def documents(request):
      documents = Document.objects.all()
      
      # Sorting and filtering dataset according to query parameters
      param_created = request.GET.get('created')
      param_updated = request.GET.get('updated')      
      param_topic = request.GET.get('topic')
      if param_created:
            if param_created == "asc":
                  documents = documents.order_by('created_at')
            elif param_created == "dsc":
                  documents = documents.order_by('-created_at')
      if param_updated:
            if param_updated == "asc":
                  documents = documents.order_by('updated_at')
            elif param_updated == "dsc":
                  documents = documents.order_by('-updated_at')
      if param_topic:
            param_topic = param_topic.split(",")
            documents = documents.filter(topic__in=param_topic).distinct()
      
      serializer = DocumentSerializer(documents, many=True)
      return Response(serializer.data)


@api_view(["GET"])
def documentDetail(request, document_id):
      document = Document.objects.get(id = document_id)
      serializer = DocumentSerializer(document, many=False)
      return Response(serializer.data)


@api_view(["POST"])
def documentCreate(request):
      serializer = DocumentSerializer(data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)


@api_view(["POST"])
def documentUpdate(request, document_id):
      document = Document.objects.get(id = document_id)
      serializer = DocumentSerializer(instance = document, data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)


@api_view(["DELETE"])
def documentDelete(request, document_id):
      document = Document.objects.get(id = document_id)
      document.delete()
      return Response(f"Document {document} successfully deleted!")


# Topics
@api_view(["GET"])
def topics(request):
      topics = Topic.objects.all()
      serializer = TopicSerializer(topics, many=True)
      return Response(serializer.data)


@api_view(["GET"])
def topicDetail(request, topic_id):
      topic = Topic.objects.get(id = topic_id)
      serializer = TopicSerializer(topic, many=False)
      return Response(serializer.data)


@api_view(["POST"])
def topicCreate(request):
      serializer = TopicSerializer(data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)


@api_view(["POST"])
def topicUpdate(request, topic_id):
      topic = Topic.objects.get(id = topic_id)
      serializer = TopicSerializer(instance = topic, data = request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)


@api_view(["DELETE"])
def topicDelete(request, topic_id):
      topic = Topic.objects.get(id = topic_id)
      topic.delete()
      return Response(f"Topic {topic} successfully deleted!")
