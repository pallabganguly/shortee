import random
import string
from django.conf import settings

MIN_SHORTCODE = getattr(settings, 'MIN_SHORTCODE', 8)

def code_generator(size=MIN_SHORTCODE, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

# here instance means instance of the model
def create_shortcode(instance, size=MIN_SHORTCODE):
    newcode = code_generator(size=size) # first size is the argument of code_generator, second one is the parameter being passed
    print('instance: ',instance)
    print('class: ',instance.__class__)
    print('name: ',instance.__class__.__name__)
    InheritClass = instance.__class__ # get class this instance beloongs to
    queryset = InheritClass.objects.all() # get a query-set of all members of this class. just like from shell
    exists = InheritClass.objects.filter(shortcode=newcode).exists() # check if shortcode just created already exists in any object
    if exists:
        return create_shortcode(size=size)
    return newcode
