from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
    url_validator = URLValidator()
    withouthttp, withhttpp = True, True
    try:
        url_validator(value)
    except:
        withouthttp = False
    nexttry = 'http://' + value
    try:
        url_validator(nexttry)
    except:
        withhttpp = False
    if withhttpp == False and withouthttp == False:
        raise ValidationError("Invalid URL!")
    return value
