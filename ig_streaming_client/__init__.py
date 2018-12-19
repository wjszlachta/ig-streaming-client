# Copyright (c) 2018 Wojciech Szlachta
#
# Licensed under the ISC License. See LICENSE file in the project root for full license information.

from ig_rest_client import IgRestSessionUsingVersion2LogIn
from lightstreamer_client import LightstreamerClient


class IgStreamingSession(IgRestSessionUsingVersion2LogIn, LightstreamerClient):
    """IG streaming API session using both IgRestSession and LightstreamerClient."""

    def __init__(self, api_key: str, account_id: str, rest_api_username: str, rest_api_password: str, **kwargs):
        IgRestSessionUsingVersion2LogIn.__init__(self, api_key, account_id, rest_api_username, rest_api_password, **kwargs)

        self._connect_lighstreamer_client()

    def _connect_lighstreamer_client(self):
        session_details = self.session_details()

        lightstreamer_username = self._account_id
        lightstreamer_password = f"CST-{self._authorization_headers['CST']}|XST-{self._authorization_headers['X-SECURITY-TOKEN']}"
        lightstreamer_url = session_details['lightstreamerEndpoint']

        LightstreamerClient.__init__(self, lightstreamer_username, lightstreamer_password, lightstreamer_url)

        self.connect()

    def switch_session_account(self, account_id: str, default_account: bool = False) -> dict:
        self.disconnect()

        result_json = IgRestSessionUsingVersion2LogIn.switch_session_account(self, account_id, default_account=default_account)

        self._connect_lighstreamer_client()

        return result_json

    def log_out(self) -> None:
        self.disconnect()

        IgRestSessionUsingVersion2LogIn.log_out(self)
