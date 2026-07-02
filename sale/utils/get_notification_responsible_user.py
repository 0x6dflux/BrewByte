from general.models import BusinessSetting


def get_notification_responsible_user():
    setting = BusinessSetting.objects.first()
    return setting.default_notification_responsible_user_id if setting else None
