from django.contrib import admin
from .models import (
    SiteSettings, HomeContent, AboutContent,
    Program,  TeamMember, MentorshipPhilosophy, Contact
)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ("welcome_title",)

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ("mission", "vision")

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("title",)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "role", "order")
    list_filter = ("role",)
    search_fields = ("name", "designation")
    ordering = ("order",)

@admin.register(MentorshipPhilosophy)
class MentorshipPhilosophyAdmin(admin.ModelAdmin):
    list_display = ("id",)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    readonly_fields = ("created_at",)
