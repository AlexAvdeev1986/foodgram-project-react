import csv
from django.core.management.base import BaseCommand
from recipes.models import Ingredient

class Command(BaseCommand):
    help = 'Import ingredients from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file) as f:
            reader = csv.reader(f)
            for row in reader:
                name, measurement_unit = row

                # Проверяем, существует ли уже такая запись
                existing_ingredient = Ingredient.objects.filter(name=name, measurement_unit=measurement_unit).first()

                if not existing_ingredient:
                    # Создаем новую запись, если не существует
                    ingredient = Ingredient.objects.create(
                        name=name, measurement_unit=measurement_unit
                    )
                    ingredient.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported ingredient: {name}, {measurement_unit}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Ingredient already exists: {name}, {measurement_unit}'))
