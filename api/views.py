from rest_framework import viewsets, permissions
from django.db.models import Q

from api.models import Blog
from api.serializers import BlogSerializer

# Create your views here.
class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = permissions.AllowAny
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        title_filter = self.request.query_params.get('title')

        if title_filter:
            queryset = queryset.filter(Q(title__icontains=title_filter))

        return queryset
