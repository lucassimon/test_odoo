# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import odoorpc

import pytest

import unittest

from datetime import datetime

from faker import Factory


class OdooTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.fake = Factory.create('pt_BR')
        # Prepare the connection to the server
        self.odoo = odoorpc.ODOO(
            'chocotech.trustcode.com.br',
            port=80
        )

        # Check available databases
        print(self.odoo.db.list())

        self.odoo.login(
            'chocotech',
            'demo',
            'demo'
        )


class CustomerTestCase(OdooTestCaseBase):
    """
    Testes para o serviço Customer
    """

    def test_sales_percent_closed(self):

        Order = self.odoo.env['sale.order']

        orders_budgets = Order.search(
            [
                '|',
                ('state', '=', 'sent'),
                ('state', '=', 'draft')
            ],
            count=True
        )

        orders_sales = Order.search(
            [
                ['state', '=', 'sale']
            ],
            count=True
        )

        total = orders_budgets + orders_sales

        percent = (float(orders_sales) * 100) / total

        print 'Cotações: {0}, Vendas condirmadas: {1}, Total: {2}, porcentagem {3:.2f} %'.format(
            orders_budgets,
            orders_sales,
            total,
            percent
        )

        self.assertEqual(
            1,
            1
        )
