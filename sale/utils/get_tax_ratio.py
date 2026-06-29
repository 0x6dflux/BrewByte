from general.models import BusinessSetting


def get_tax_ratio():
        setting = BusinessSetting.objects.first()
        return float(setting.default_tax_ratio) if setting else 0