# coding: utf-8

"""
    Terminal API

    Terminal is a unified API that makes it easy to integrate with the leading telematics service providers.  Contact Support:  Name: Terminal  Email: connect@withterminal.com

    The version of the OpenAPI document: 1.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import terminal_python_sdk
from terminal_python_sdk.paths.issues import get
from terminal_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestIssues(ApiTestMixin, unittest.TestCase):
    """
    Issues unit test stubs
        List Issues
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
