from api.models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'author', 'content', 'created_at', 'updated_at', 'id']
        depth = 1
