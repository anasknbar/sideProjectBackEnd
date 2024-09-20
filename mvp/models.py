# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the conversation
    title = models.CharField(max_length=255, blank=True, null=True)  # Optional title
    prompt = models.TextField()  # The prompt submitted by the user
    ai_response = models.TextField()  # The AI-generated response
    tags = models.ManyToManyField(Tag, related_name='conversations', blank=True)  # Tags for categorization
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp when modified

    def __str__(self):
        return self.title if self.title else f"Conversation {self.id}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who made the comment
    conversation = models.ForeignKey(Conversation, related_name='comments', on_delete=models.CASCADE)  # The related conversation
    content = models.TextField()  # The comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp when modified

    def __str__(self):
        return f"Comment by {self.user.username} on {self.conversation.title}"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who voted
    conversation = models.ForeignKey(Conversation, related_name='votes', on_delete=models.CASCADE)  # The conversation being voted on
    vote_type = models.BooleanField(default=True)  # True for upvote, False for downvote (if needed)

    class Meta:
        unique_together = ('user', 'conversation')  # Prevent a user from voting multiple times on the same conversation

    def __str__(self):
        return f"Vote by {self.user.username} on {self.conversation.title}"

class PromptTemplate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the template
    name = models.CharField(max_length=255)  # The name of the template
    template_content = models.TextField()  # The prompt content for the template
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-add timestamp when created

    def __str__(self):
        return f"Template: {self.name} by {self.user.username}"

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link the profile to the user
#     bio = models.TextField(null=True, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

#     def __str__(self):
#         return f"Profile of {self.user.username}"
