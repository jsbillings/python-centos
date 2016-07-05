import os
import requests

from OpenSSL import crypto
from centos import defaults

class CentOSUserCert(object):

    def __init__(self, filename=None):
        if filename is None:
            filename = defaults.USER_CERT_FILE

        with open(os.path.expanduser(filename),'r') as certfile:
            try:
                self._cert = crypto.load_certificate(crypto.FILETYPE_PEM, certfile.read())
            except crypto.Error:
                raise IOError("Invalid or empty certificate file: {0}".format(filename))


            # The components of the subject (like the CN and the Email Address)
            # are all pieces of data we want to reference in this class
            self.__dict__.update(dict(self._cert.get_subject().get_components()))

            self.expired = self._cert.has_expired() != 0L
            self.serial = self._cert.get_serial_number()

    @property
    def valid(self):
        crl_response = requests.get(defaults.FAS_CRL)
        crl = crypto.load_crl(crypto.FILETYPE_PEM, crl_response.text)

        if self.serial in (long(x.get_serial(), 16) for x in crl.get_revoked()):
            return False

        if self.expired:
            return False

        return True

