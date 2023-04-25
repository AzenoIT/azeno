from django.contrib import admin

from comments.models import Comment


class CommentAdminConfig(admin.ModelAdmin):
    """Class **CommentAdminConfig** displays comments list in admin panel
    based on :class:`comments.models.Comment` model."""

    list_display = (
        "user",
        "flashcard",
        "deck",
        "comment",
        "created_at",
    )
    search_fields = (
        "comment",
        "user__email",
        "deck__name",
    )
    list_display_links = ("user",)
    save_on_top = True
    list_per_page = 50


admin.site.register(Comment, CommentAdminConfig)
