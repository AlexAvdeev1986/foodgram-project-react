"""
Import of ingredients from *.csv file to the database.
"""
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
                # Проверка наличия ингредиента перед созданием
                ingredient, created = Ingredient.objects.get_or_create(
                    name=name, measurement_unit=measurement_unit
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully imported ingredient: {name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Ingredient {name} already exists. Skipping.'))
