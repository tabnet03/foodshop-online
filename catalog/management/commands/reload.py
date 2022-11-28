from django.core.management.base import BaseCommand
from django.conf import settings
import pathlib


class Command(BaseCommand):
    def handle(self, *args, **options):
        # print('Reload') bu ./manage.py qilinganda reload yozish imkonini beradi va terminalda
        # reload yozuvini chiqaradi
        # print(settings.INSTALLED_APPS) #bu installad app lani chiqarish usuli
        for app in settings.INSTALLED_APPS:
            if '.' in app:
                continue
            files = pathlib.Path(settings.BASE_DIR / app).rglob('*.py')

            a = 0
            for f in files:

                # p = open(files, 'r')
                # print(((p.read()).strip()).count('\n'))
                # print(list(files))
                if files:
                    a += 1
                    continue

            print(a, "ta *.py filelar bor")
