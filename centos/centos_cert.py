import os
from OpenSSL import crypto

defaults = {
            'USER_CERT_FILE': '~/.centos.cert',
            'FAS_TOPURL'    : 'https://accounts.centos.org/',
            'FAS_CRL'       : 'https://accounts.centos.org/ca/crl.pem',
           }

class CentOSUserCert(object):
    DEFAULT_USER_FILE="~/.centos.cert"

    def __init__(self, filename=None):
        if filename is None:
            filename = defaults['USER_CERT_FILE']

        with open(os.path.expanduser(filename),'r') as certfile:
            self._cert = crypto.load_certificate(crypto.FILETYPE_PEM, certfile.read())

            # The components of the subject (like the CN and the Email Address)
            # are all pieces of data we want to reference in this class
            self.__dict__.update(dict(self._cert.get_subject().get_components()))

            self.expired = self._cert.has_expired() == True
            self.serial = self._cert.get_serial_number()
