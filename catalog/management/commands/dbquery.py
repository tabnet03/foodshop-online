
from django.core.management.base import BaseCommand
from django.db import connection
import datetime
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        query = """
        INSERT INTO "books" ("name", "content", "price", "status", "added_at", "updated_at") VALUES (%s, %s, %s, "0", %s, %s);
        """
        now = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"
        for i in range(10):
            with connection.cursor() as c:
                c.execute(query, [
                    f"Name {i}",
                    f"Content {i}",
                    random.randint(1000, 100000),
                    now,
                    now
                ])
