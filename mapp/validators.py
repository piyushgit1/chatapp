from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeEmailValidator(validators.RegexValidator):
    regex = r'^[\w.@+-]+\Z'
    message = _(
        'Enter a valid Email. This value may contain only letters, '
        'numbers, and @/./+/-/_ characters.'
    )
    flags = 0