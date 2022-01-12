from django.contrib import admin

# Register your models here.
from SoulPlace.models import Feedback

class FeedbackModelAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = [
        'fullname',
        'email',
        'number',
        'suggestion_p',
        ]


admin.site.register(Feedback, FeedbackModelAdmin)