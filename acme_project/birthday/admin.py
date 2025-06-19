from django.contrib import admin

from birthday.models import Birthday, Tag

admin.site.empty_value_display = 'Не задано'

@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

