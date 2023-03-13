from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from apps.receitas.views import index

# Create your tests here.

class ReceitaViewsTestCase(TestCase):

    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_rota_url_utiliza_View_index(self):
        """ Teste se a home da aplicação utiliza """
        request = self.factory.get('/')
        with self.assertTemplateUsed('receitas/index.html'):
            responce = index(request)
            self.assertEqual(responce.status_code, 200)
