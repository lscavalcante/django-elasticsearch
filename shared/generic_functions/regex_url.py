def regex_url(parameter: str) -> str:
    return f'(?P<{parameter}>[0-9a-f-]+)'
