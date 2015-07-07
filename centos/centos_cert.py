import os
from OpenSSL import crypto

class CentOSUserCert(object):
    DEFAULT_USER_FILE="~/.centos.cert"

    def __init__(self, filename=None):
        if filename is None:
            filename = self.DEFAULT_USER_FILE

        with open(os.path.expanduser(filename),'r') as certfile:
            self._cert = crypto.load_certificate(crypto.FILETYPE_PEM, certfile.read())
            self.__dict__.update(dict(self._cert.get_subject().get_components()))

            self.expired = self._cert.has_expired()
