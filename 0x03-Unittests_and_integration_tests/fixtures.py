#!/usr/bin/env python3
"""
This module defines fixtures for unit tests
"""

import pytest


@pytest.fixture(scope="module")
def connect_db():
    """
    Fixture that connects to the database
    """
    conn = None
    # connect to the database here
    yield conn
    # disconnect from the database here
