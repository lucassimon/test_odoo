# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest
import unittest
from datetime import datetime


from faker import Factory


class OdooTestCaseBase(unittest.TestCase):

    def setUp(self):

        self.fake = Factory.create('pt_BR')


class CustomerTestCase(OdooTestCaseBase):
    """
    Testes para o serviço Customer
    """

    def test_customer(self):

        self.assertEqual(
            1,
            1
        )
