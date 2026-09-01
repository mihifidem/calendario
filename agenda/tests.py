from django.test import TestCase

from agenda.orm_examples import run_orm_examples


class OrmExamplesTests(TestCase):
    def test_run_orm_examples_creates_and_queries_objects(self):
        result = run_orm_examples()

        self.assertIn("todos", result)
        self.assertIn("filtrados", result)
        self.assertIn("nuevos", result)
        self.assertIn("actualizado", result)
        self.assertIn("categorias", result)
