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

    def test_customer(self):

        self.assertEqual(
            1,
            1
        )
