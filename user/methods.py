from user.models import *


import datetime
import random
import string

def id_generator():
    today = datetime.datetime.now()
    year = str(today.year)
    year = year[2:]
    while True:
        new_account_id = ''.join([str(random.choice(string.digits)) for n in range(8)])
        new_account_id = year + new_account_id
        if model_data.objects.filter(model_id=new_account_id).exists() :
            pass
        else:
            break
    return new_account_id