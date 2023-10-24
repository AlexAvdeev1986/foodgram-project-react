import asyncio
from csv import DictReader
from asgiref.sync import sync_to_async

from django.core.management.base import BaseCommand
from recipes.models import Ingredient

csv_files = [
    {
        "model": Ingredient,
        "filename": "ingredients.csv",
        "fieldnames": ["name", "measurement_unit"],
    },
]

class Command(BaseCommand):
    help = "Загружает ингредиенты из файла csv."

    async def async_update_or_create(self, model, row):
        try:
            # Using sync_to_async to turn the synchronous Django ORM operation into an async one
            await sync_to_async(model.objects.update_or_create, thread_sensitive=True)(
                name=row["name"], defaults=row
            )
            return True
        except Exception as error:
            print(row)
            print(f"Ошибка записи в таблицу модели {model.__name__}, {str(error)}")
            return False

    async def csv_loader(self, cf):
        csv_file = "static/data/ingredients.csv"
        with open(csv_file, encoding="utf-8", newline="") as csvfile:
            reader = DictReader(csvfile, fieldnames=cf["fieldnames"])
            print(f'Загрузка в таблицу модели {cf["model"].__name__}')

            tasks = []
            i, err, r = 0, 0, 0

            async for row in reader:
                # Creating a task for each row to be inserted
                task = asyncio.create_task(self.async_update_or_create(cf["model"], row))
                tasks.append(task)

            # Waiting for all tasks to complete
            for task in asyncio.as_completed(tasks):
                success = await task
                if success:
                    r += 1
                else:
                    err += 1
                i += 1

            print(f"Всего: {i} строк. Загружено: {r} строк. Ошибки: {err} строк.")

    async def async_handle(self, *args, **options):
        print("Идет загрузка данных...")
        for cf in csv_files:
            await self.csv_loader(cf)
        print("Загрузка завершена.")

    def handle(self, *args, **options):
        asyncio.run(self.async_handle(*args, **options))
