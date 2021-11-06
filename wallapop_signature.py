import hmac
import hashlib
import base64
import codecs


def generate_xsignature(endpoint, method, timestamp):
    # Credits to @rmonvfer https://github.com/rmonvfer/wallapop_secret
    timestamp = timestamp.split(".")[0]
    secret_key = b"Tm93IHRoYXQgeW91J3ZlIGZvdW5kIHRoaXMsIGFyZSB5b3UgcmVhZHkgdG8gam9pbiB1cz8gam9ic0B3YWxsYXBvcC5jb20=="
    total_params = b"/api/v3/" + endpoint.encode() + b"+#+" + method.encode() + \
        b"+#+" + timestamp.encode() + b"+#+"
    signature = hmac.new(base64.b64decode(secret_key),
                         total_params, hashlib.sha256).digest()
    return str(codecs.encode(signature, 'base64').decode()).strip()
