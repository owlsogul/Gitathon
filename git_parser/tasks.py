from background_task import background
from logging import getLogger

logger = getLogger(__name__)

@background(schedule=20)
def test(message):
    print(message)