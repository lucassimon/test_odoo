# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import odoorpc

import pytest

import unittest

from datetime import datetime

from faker import Factory


class OdooTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.customer_id = 0

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

    def test_add_customer(self):
        """
        Inserir um cliente no Odoo via api,
        com os seus dados (Nome, email, telefone, cep)
        """

        Customer = self.odoo.env['res.partner']

        email = self.fake.email()

        self.customer_id = Customer.create(
            {
                'name': self.fake.name(),
                'email': email,
                'phone': self.fake.phone_number(),
                'zip': self.fake.postcode()
            }
        )

        customer = Customer.browse(self.customer_id)

        self.assertEqual(
            customer.email,
            email
        )
