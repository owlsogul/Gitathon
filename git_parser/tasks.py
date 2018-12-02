from background_task import background
from logging import getLogger
#from teamproject.models import Commit


@background(schedule=60)
def test(message):
    print(message)

@background(schedule=60)
def lookCommit(message):
    print(message)
