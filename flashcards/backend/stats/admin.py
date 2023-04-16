from django.contrib import admin

from stats.models import DeckStudy, FlashcardStudy


class FlashcardStudyAdminConfig(admin.ModelAdmin):
    """Class **FlashcardStudyAdminConfig** displays flashcard study logs list in admin panel
    based on :class:`stats.models.FlashcardStudyLog` model."""

    list_display = ("flashcard", "user", "study_date", "correct_answers")
    search_fields = ("flashcard",)
    list_display_links = ("flashcard",)
    save_on_top = True
    list_filter = (
        "flashcard",
        "user",
    )
    list_per_page = 50


class DeckStudyAdminConfig(admin.ModelAdmin):
    """Class **DeckStudyAdminConfig** displays deck study logs list in admin panel
    based on :class:`stats.models.DeckStudyLog` model."""

    list_display = ("deck", "user", "study_date", "correct_answers", "study_duration", "realization")
    search_fields = ("deck",)
    list_display_links = ("deck",)
    save_on_top = True
    list_filter = (
        "deck",
        "user",
    )
    list_per_page = 50


admin.site.register(FlashcardStudy, FlashcardStudyAdminConfig)
admin.site.register(DeckStudy, DeckStudyAdminConfig)
