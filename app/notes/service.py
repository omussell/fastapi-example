from notes.models import *
from typing import List
#import orm

async def get_all():
    notes = await Note.objects.all()
    return
