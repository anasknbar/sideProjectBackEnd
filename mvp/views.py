from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import TagSerializers,ConversationSerializers,CommentSerializers,VoteSerializers,PromptTemplateSerializers
from .models import Conversation,Tag,Comment,Vote,PromptTemplate
from rest_framework.permissions import IsAdminUser,IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import isOwnerOrReadOnly

# Create your views here.

class TagListView(ListAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializers
class TagCreateView(CreateAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializers
class TagDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Tag.objects.all()
  serializer_class = TagSerializers
  
# -------------------------------------------------------------------

class ConversationListView(ListAPIView):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializers
  
class ConversationCreateView(CreateAPIView):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializers
 
  
class ConversationDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Conversation.objects.all()
  serializer_class = ConversationSerializers
  permission_classes = [isOwnerOrReadOnly]
  
# -------------------------------------------------------------------

class CommentListView(ListAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializers
class CommentCreateView(CreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializers
class CommentDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializers  
  permission_classes = [isOwnerOrReadOnly]
  
# -------------------------------------------------------------------

class VoteListView(ListAPIView):
  queryset = Vote.objects.all()
  serializer_class = VoteSerializers
class VoteCreateView(CreateAPIView):
  queryset = Vote.objects.all()
  serializer_class = VoteSerializers
class VoteDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = Vote.objects.all()
  serializer_class = VoteSerializers
  permission_classes = [isOwnerOrReadOnly]
  
# -------------------------------------------------------------------

class PromptTemplateListView(ListAPIView):
  queryset = PromptTemplate.objects.all()
  serializer_class = PromptTemplateSerializers
class PromptTemplateCreateView(CreateAPIView):
  queryset = PromptTemplate.objects.all()
  serializer_class = PromptTemplateSerializers
class PromptTemplateDetailsView(RetrieveUpdateDestroyAPIView):
  queryset = PromptTemplate.objects.all()
  serializer_class = PromptTemplateSerializers
  permission_classes = [isOwnerOrReadOnly]
  
# -------------------------------------------------------------------
