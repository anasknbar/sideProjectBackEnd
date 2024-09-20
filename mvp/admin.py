from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Conversation, Tag,Comment,Vote,PromptTemplate

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')
    search_fields = ('title', 'prompt', 'user__username')
    list_filter = ('tags', 'created_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'conversation', 'content', 'created_at')
    search_fields = ('user__username', 'conversation__title')

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'conversation', 'vote_type')
    search_fields = ('user__username', 'conversation__title')

@admin.register(PromptTemplate)
class PromptTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from allauth.account.models import EmailAddress
from django.db.models.signals import post_save
from django.dispatch import receiver

# Unregister the original UserAdmin
admin.site.unregister(User)

# Custom save function to add email to EmailAddress table
class UserAdmin(BaseUserAdmin):
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Check if the email is already in the EmailAddress table
        if not EmailAddress.objects.filter(user=obj).exists():
            EmailAddress.objects.create(
                user=obj,
                email=obj.email,
                primary=True,
                verified=True
            )

# Register the custom UserAdmin
admin.site.register(User, UserAdmin)

