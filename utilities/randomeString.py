import string
import random

def random_string_generator(size=5,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



def screenname_genrator(size=10, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))
