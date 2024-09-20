from rest_framework import serializers
from .models import Tag,Conversation,Comment,Vote,PromptTemplate

class ConversationSerializers(serializers.ModelSerializer):
  class Meta:
    model = Conversation
    fields = '__all__'

class TagSerializers(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class VoteSerializers(serializers.ModelSerializer):
  class Meta:
    model = Vote
    fields = '__all__'

class PromptTemplateSerializers(serializers.ModelSerializer):
  class Meta:
    model = PromptTemplate
    fields = "__all__"