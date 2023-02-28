#!/usr/bin/env python3
"""
This module defines the function get_json
"""

import requests


def get_json(url: str) -> dict:
    """
    Sends a GET request to the specified URL and returns the JSON response

    Args:
        url (str): The URL to send the request to

    Returns:
        dict: The JSON response from the server

    Raises:
        requests.exceptions.HTTPError: If the response status code is not 200 OK
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
