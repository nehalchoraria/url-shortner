from background_task import background
from .models import GeneratedLinks

@background(schedule=3600)
def clear_database():
    GeneratedLinks.objects.all().delete()

clear_database()

