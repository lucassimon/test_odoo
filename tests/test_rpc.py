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

    def test_june_invoices(self):

        Order = self.odoo.env['sale.order']

        ids = Order.search(
            [
                ('invoice_status', '=', 'to invoice'),
                '|',
                ('invoice_status', '=', 'invoiced'),
                ('confirmation_date', '>=', '2017-07-01'),
                ('confirmation_date', '<', '2017-08-01')
            ],
        )

        count = len(ids)

        total = 0

        for order in Order.browse(ids):

            total += order.amount_total

        print '{0} notas a faturar no mês de julho/2017 é $ {1:.2f}'.format(
            count,
            total
        )

        self.assertEqual(
            1,
            1
        )
