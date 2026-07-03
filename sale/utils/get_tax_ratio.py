from general.models import BusinessSetting
from decimal import Decimal


def get_tax_ratio():
    setting = BusinessSetting.objects.first()
    return Decimal(float(setting.default_tax_ratio) / 100) if setting else Decimal(0)
