from django.contrib import admin
from .models import Post, Author


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'status']
    list_filter = ['title', 'author', 'created_at']
    search_fields = ['title', 'text']
    actions = ['make_published', 'withdraw', 'draft']

    def make_published(self, request, queryset):
        queryset.update(status='p')

    make_published.short_description = "Mark Selected post as published"

    def withdraw(self, request, queryset):
        queryset.update(status='w')

    withdraw.short_description = "Draft Post"

    def draft(self, request, queryset):
        queryset.update(status='d')

    draft.short_description = "Approve the draft"


admin.site.register(Post, PostAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'gender', 'birth_date', 'country']
    list_filter = ['first_name', 'last_name', 'age', 'gender', 'birth_date', 'country']
    search_fields = ['first_name', 'last_name', 'age', 'gender', 'birth_date', 'country']


admin.site.register(Author, AuthorAdmin)
