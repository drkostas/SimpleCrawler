"""
module for normalising urls

why?
    a web crawler might encounter urls that look different
    but are otherwise the same

    e.g.
    * HTTPS://:@WWW.EXAMPLE.COM?greeting=hello world
    * https://www.example.com/?greeting=hello+world

    these are the same and although many web devs building hrefs won't be
    make these mistakes, they can be encountered and need to be handled

"""
import doctest


def normalise_scheme(scheme: str) -> str:
    """
    normalise scheme (e.g. https)

    :param scheme: (str) https, http, ftp, etc
    :return: (str) lower case scheme

    >>> normalise_scheme('')
    ''
    >>> normalise_scheme('https')
    'https'
    >>> normalise_scheme('HTTPS')
    'https'
    """
    scheme = scheme.lower()
    return scheme


def normalise_host(host: str) -> str:
    """
    normalise host (e.g. localhost, www.google.com)

    :param host: (str) any host
    :return: (str) normalised lower case host

    >>> normalise_host('')
    ''
    >>> normalise_host('www.google.com')
    'www.google.com'
    >>> normalise_host('www.EXAMPLE.com')
    'www.example.com'
    >>> normalise_host('www.example.com.')
    'www.example.com'

    todo: idna?
    """
    host = host.lower()
    host = host.strip(".")
    return host


def normalise_userinfo(userinfo: str) -> str:
    """
    normalise userinfo (e.g. hello:world)
    NB: passwords are NOT recommended to be sent via clear text

    :param userinfo: (str) any defined user info, with username and/or password
    :return: (str) normalised user info

    >>> normalise_userinfo('')
    ''
    >>> normalise_userinfo('hello:world')
    'hello:world'
    >>> normalise_userinfo('hello:')
    'hello'
    >>> normalise_userinfo(':')
    ''
    """
    userinfo = userinfo.strip(":")
    return userinfo


if __name__ == "__main__":
    doctest.testmod()
