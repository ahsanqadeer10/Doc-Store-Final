from django.urls import path

from . import views

urlpatterns = [
      path('', views.index, name="index"),
      path('folders/', views.folders, name="folders"),
      path('folder-detail/<int:folder_id>/', views.folderDetail, name="folder-detail"),
      path('folder-documents/<int:folder_id>/', views.folderDocuments, name="folder-documents"),
      path('folder-create/', views.folderCreate, name="folder-create"),
      path('folder-update/<int:folder_id>/', views.folderUpdate, name="folder-update"),
      path('folder-delete/<int:folder_id>/', views.folderDelete, name="folder-delete"),
      path('documents/', views.documents, name="documents"),
      path('document-detail/<int:document_id>/', views.documentDetail, name="document-detail"),
      path('document-create/', views.documentCreate, name="document-create"),
      path('document-update/<int:document_id>/', views.documentUpdate, name="document-update"),
      path('document-delete/<int:document_id>/', views.documentDelete, name="document-delete"),
      path('topics/', views.topics, name="topics"),
      path('topic-detail/<int:topic_id>/', views.topicDetail, name="topic-detail"),
      path('topic-create/', views.topicCreate, name="topic-create"),
      path('topic-update/<int:topic_id>/', views.topicUpdate, name="topic-update"),
      path('topic-delete/<int:topic_id>/', views.topicDelete, name="topic-delete")
]