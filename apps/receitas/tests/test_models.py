
from django.test import TestCase, RequestFactory
from apps.receitas.models import Receita
from datetime import datetime

class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.receita = Receita.objects.create(
            pessoa = 'Teste',
            nomeReceita = 'Teste',
            ingredientes = 'Teste Teste Teste Teste Teste ',
            modoPreparo = 'Teste Teste Teste Teste Teste ',
            tempoPreparo = 10,
            rendimento = 'Teste',
            categoria = 'Teste',
            dataReceita = datetime.now,
            publicada = False,
            fotoReceita = '',
        )
    
    def test_receita_cadastrado_com_caracteristicas(self):
        """Teste que verifica se o receita está cadastrado com suas respectivas características"""
        self.assertEqual(self.receita.nomeReceita, 'Teste')