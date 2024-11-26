import os
import re
import base64
import hashlib
import requests_oauthlib

CODE_VERIFIER = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8")
CODE_VERIFIER = re.sub("[^a-zA-Z0-9]+", "", CODE_VERIFIER)

CODE_CHALLENGE = hashlib.sha256(CODE_VERIFIER.encode('utf-8')).digest()
CODE_CHALLENGE = base64.urlsafe_b64encode(CODE_CHALLENGE).decode('utf-8')
CODE_CHALLENGE = CODE_CHALLENGE.replace("=", "")

def create_oauth2(client_id, redirect_uri, scope):
    oauth = requests_oauthlib.OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    return oauth

def getAuthorizationURL(oauth, auth_url):
    authorization_url, state = oauth.authorization_url(
        auth_url, code_challenge=CODE_CHALLENGE, code_challenge_method='S256'
    )
    return authorization_url

def getToken(oauth, token_url, client_secret, code, headers):
    token = oauth.fetch_token(
        token_url=token_url, client_secret=client_secret, code_verifier=CODE_VERIFIER, code=code
    )
    return token
