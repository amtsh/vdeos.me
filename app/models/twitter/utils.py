import re


def get_url(text):
    return re.findall('https?\S+', text)
