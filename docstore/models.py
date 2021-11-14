from django.db import models

# Create your models here.

class Folder(models.Model):
      name = models.CharField(max_length=100, unique=True, blank=False)
      description = models.CharField(max_length=256, blank=True)
      topic = models.ManyToManyField("Topic", related_name="folders", blank=True)
      created_at = models.DateTimeField(auto_now_add=True, blank=True)
      updated_at = models.DateTimeField(auto_now=True, blank=True)
      
      def __str__(self):
            return self.name


class Document(models.Model):
      name = models.CharField(max_length=100, unique=True, blank=False)
      description = models.CharField(max_length=256, blank=True)
      folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="documents")
      topic = models.ManyToManyField("Topic", related_name="documents", blank=True)
      created_at = models.DateTimeField(auto_now_add=True, blank=True)
      updated_at = models.DateTimeField(auto_now=True, blank=True)

      def __str__(self):
            return self.name


class Topic(models.Model):
      name = models.CharField(max_length=100, unique=True, null=False)
      description = models.CharField(max_length=256, blank=True)
      created_at = models.DateTimeField(auto_now_add=True, blank=True)
      updated_at = models.DateTimeField(auto_now=True, blank=True)
      
      def __str__(self):
            return self.name
