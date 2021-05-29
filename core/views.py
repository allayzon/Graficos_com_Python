from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        """Retorna 12 labels para a representação do x"""
        labels = [
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro"
        ]

        return labels

    def get_providers(self):
        """Retorna os nomes dos datasets."""
        datasets = [
            "Programação para Leigos",
            "Algorítmos e Lógica de Programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"
        ]
        return datasets

    def get_data(self):
        """
        Retorna 6 datasets para plotar o gráfico.

        Cada linha representa um dataset.
        Cada coluna representa um label.

        A quantidade de dados precisa ser igual aos datasets/labels

        12 labels, então 12 colunas.
        6 datasets, então 6 linhas.
        :return:
        """

        dados = []
        for c in range(6):  # Colunas
            for l in range(12):  # Linhas
                dado = [
                    randint(1, 200),  # Jan
                    randint(1, 200),  # Fev
                    randint(1, 200),  # etc
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                    randint(1, 200),
                ]
            dados.append(dado)
        return dados