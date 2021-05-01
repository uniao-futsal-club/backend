from django.db import models


class UpperCaseField(models.CharField):
    description = "uppercase string field"

    def __init__(self, *args, **kwargs):
        super(UpperCaseField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super(UpperCaseField, self).get_prep_value(value)
        return value.upper()
