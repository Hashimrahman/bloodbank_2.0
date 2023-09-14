from django.core.management.base import BaseCommand
from myapp.models import Registration  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Clear the Registration table'

    def handle(self, *args, **kwargs):
        Registration.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Cleared the Registration table.'))
