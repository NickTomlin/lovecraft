import re


def get_safe_pathname(path):
    ''' (str) -> (str)
    returns a lowercased "safe" version of a string with spaces replaced by "_"
    '''
    path_re = r'(\s+)'
    safe = re.sub(path_re, '_', path)
    return safe.lower()
