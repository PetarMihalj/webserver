"""
This module acts as a global storage location.
It stores the references to functions which handle certain requests.

requests_GET[path]=function_which_handles_this_path
"""

requests_GET = dict()
