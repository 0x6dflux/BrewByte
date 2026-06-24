from django.contrib import admin

from activity.models import (
    CommentModel,
    FavoriteModel,
    NotificationModel,
)

admin.site.register(CommentModel)
admin.site.register(FavoriteModel)
admin.site.register(NotificationModel)
