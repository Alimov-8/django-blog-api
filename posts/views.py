# posts/views.py
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly 
from .models import Post
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model


from rest_framework import viewsets # new

# class PostViewSet(viewsets.ModelViewSet): # new
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer