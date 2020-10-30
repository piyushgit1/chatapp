import time

from django_otp.oath import TOTP

from mapp import views

last_verified_counter = -1
secret_key = b'12345678901234567890'

t = False


class a:
    def totp_obj(self):
        totp = TOTP(key=secret_key, step=200, digits=6)
        totp.time = time.time()
        return totp

    def verify_token(self, token, tolerance=0):
        totps = a.totp_obj(self)
        if ((totps.t() > last_verified_counter) and
                (totps.verify(token, tolerance=tolerance))):
            self.last_verified_counter = totps.t()
            self.verified = True

        else:
            self.verified = False
        return self.verified
