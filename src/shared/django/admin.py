from django.contrib.admin import ModelAdmin


class TimeStampReadonlyAdmin(ModelAdmin):

    _FIELDS: list = ["created_at", "update_at"]

    readonly_fields = _FIELDS
    list_filter = _FIELDS
    search_fields = _FIELDS
