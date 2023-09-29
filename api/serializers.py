from api.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        models = Blog
        fields = ['title', 'slug', 'author', 'content', 'created_at', 'updated_at', 'id']
        depth = 1
