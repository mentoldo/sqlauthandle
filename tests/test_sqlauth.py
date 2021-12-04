#!/usr/bin/env python

"""Tests for `sqlauth` package."""

import pytest

from click.testing import CliRunner

from sqlauth import sqlauth
from sqlauth import cli
import configparser

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'sqlauth.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

@pytest.fixture
def temp_fileconf(tmpdir):
    temp_fileconf = tmpdir.join("fileconf.txt")
    
    yield temp_fileconf

def test_for_init_fileconf(temp_fileconf):
    
    fileconf = temp_fileconf
    config = configparser.ConfigParser()
    
    auth = sqlauth.Sqlauth(fileconf)

    auth.set_credentials(app='sqlauth',
                         dialect='postgresql',
                         host='localhost',
                         port='5432',
                         user='usuario',
                         db_name='encuesta',
                         passwd='1234')
    
    config.read(fileconf)
    assert config['credentials']['app'] == 'sqlauth'
    assert config['credentials']['dialect'] == 'postgresql'
    assert config['credentials']['host'] == 'localhost'
    assert config['credentials']['port'] == '5432'
    assert config['credentials']['user'] == 'usuario'
    assert config['credentials']['db_name'] == 'encuesta'

