from django.urls import path
from .views import (
  TagListView,TagCreateView,TagDetailsView,
  ConversationListView,ConversationCreateView,ConversationDetailsView,
  CommentListView,CommentCreateView,CommentDetailsView,
  VoteListView,VoteCreateView,VoteDetailsView,
  PromptTemplateListView,PromptTemplateCreateView,PromptTemplateDetailsView,
  
  
  
  
)
urlpatterns = [
  
  path('tag/',TagListView.as_view(),name='tag'),
  path('tag/create/',TagCreateView.as_view(),name='create_tag'),
  path('tag/<int:pk>/',TagDetailsView.as_view(),name='tag_details'),
  
  path('conversation/',ConversationListView.as_view(),name='conversation'),
  path('conversation/create/',ConversationCreateView.as_view(),name='create_conversation'),
  path('conversation/<int:pk>',ConversationDetailsView.as_view(),name='conversation_details'),
  
  path('comment/',CommentListView.as_view(),name='comment'),
  path('comment/create/',CommentCreateView.as_view(),name='create_comment'),
  path('comment/<int:pk>/',CommentDetailsView.as_view(),name='comment_details'),
  
  path('vote/',VoteListView.as_view(),name='vote'),
  path('vote/create/',VoteCreateView.as_view(),name='create_vote'),
  path('vote/<int:pk>',VoteDetailsView.as_view(),name='vote_details'),
  
  path('prompt_template/',PromptTemplateListView.as_view(),name='prompt_template'),
  path('prompt_template/create/',PromptTemplateCreateView.as_view(),name='create_prompt_template'),
  path('prompt_template/<int:pk>/',PromptTemplateDetailsView.as_view(),name='prompt_template_details'),
  
]