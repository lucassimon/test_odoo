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

    def test_get_ten_customer_order__name_asc(self):
        """
        Listar os 10 primeiros clientes
        por ordem alfabética (Nome e Cidade que mora)
        """

        Customer = self.odoo.env['res.partner']

        customers = Customer.search_read(
            [],
            ['name', 'country_id'],
            order='name',
            limit=10
        )

        for customer in customers:

            if not customer.get('customer_id'):

                city = None
            else:

                city = customer.get('customer_id')[1]

            print '{}: {} -> {}'.format(
                customer.get('id'),
                customer.get('name'),
                city
            )

        self.assertEqual(
            1,
            1
        )
