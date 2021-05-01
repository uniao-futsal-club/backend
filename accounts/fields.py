from django.db import models
from django.contrib.auth.hashers import make_password


class PasswordField(models.CharField):
    description = "password encrypted field"

    def pre_save(self, model_instance, add):
        pwd = make_password(model_instance.password)
        return pwd


class UpperCaseField(models.CharField):
    description = "uppercase string field"

    def __init__(self, *args, **kwargs):
        super(UpperCaseField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        value = super(UpperCaseField, self).get_prep_value(value)
        return value.upper()


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)
