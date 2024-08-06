"""
Copyright 2024 BlackRock, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import time
import webbrowser
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from requests_oauthlib import OAuth2Session

_AUTH_TIMEOUT_LIMIT = 30


class StoppableThread(threading.Thread):
    """
    Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition.
    """

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        for i in range(_AUTH_TIMEOUT_LIMIT):
            if self.stopped():
                return
            diff_count = _AUTH_TIMEOUT_LIMIT - i
            print(f'  Remaining time: {diff_count} seconds. {"-" * diff_count}{" " * (_AUTH_TIMEOUT_LIMIT - diff_count)}', end='\r')
            time.sleep(1)
        print(f' Timeout. {"   " * _AUTH_TIMEOUT_LIMIT}', end='\r')


class LocalAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Will reach this method on redirect.
        self.server.auth_code = parse_qs(urlparse(self.path).query).get('code', [None])[0]
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'You can close this window now.')


def start_local_auth_handler(localhost_redirect_uri_port):
    server_address = ('', localhost_redirect_uri_port)
    httpd = HTTPServer(server_address, LocalAuthHandler)
    httpd.timeout = _AUTH_TIMEOUT_LIMIT
    httpd.handle_request()
    return httpd.auth_code


def get_refresh_token_from_oauth_server(client_id=None,
                                        client_secret=None,
                                        scopes=None,
                                        localhost_redirect_uri_port=None,
                                        authorization_url=None,
                                        token_url=None):
    """
    Client for communicating with oauth server to fetch a refresh token
    """
    countdown_thread = StoppableThread()
    try:
        if not client_id or not client_secret:
            raise ValueError("OAuth application client ID and/or secret missing")

        oauth = OAuth2Session(client_id, redirect_uri=f"http://localhost:{localhost_redirect_uri_port}", scope=scopes)
        _authorization_url, state = oauth.authorization_url(authorization_url)

        print(f"Continue on browser to authenticate... (Ctrl+C to cancel)")
        webbrowser.open(_authorization_url)
        countdown_thread.start()
        auth_code = start_local_auth_handler(localhost_redirect_uri_port)
        fetch_token_response = oauth.fetch_token(
            token_url,
            code=auth_code,
            client_secret=client_secret
        )
        refresh_token = fetch_token_response['refresh_token']
        countdown_thread.stop()
        return refresh_token
    except (KeyboardInterrupt, Exception):
        countdown_thread.stop()
        return None

