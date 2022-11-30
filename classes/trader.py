from smartapi import SmartConnect
from classes.namespaces import CONFIG
import json
import pyotp
import os

TRADING_PASSWORD = os.environ["angelone_password"]


class Trader:
    def __init__(self, config: json = {}) -> None:
        self.config = config
        self.totp = self.get_totp()
        self.smart_connect_obj = SmartConnect(api_key=self.get_api_key())
        self.refresh_token = self.get_refresh_token()

    def _get_config(self, key: str = ""):
        if key in self.config.keys():
            return self.config[key]
        else:
            raise Exception(f"No {key} name found")

    def get_totp(self) -> str:
        return pyotp.TOTP(self._get_config(key=CONFIG["TOTP"])).now()

    def get_broker_name(self) -> str:
        return self._get_config(key=CONFIG["BROKER"])

    def get_broker_id(self) -> str:
        return self._get_config(key=CONFIG["BROKER_ID"])

    def get_api_key(self) -> str:
        return self._get_config(key=CONFIG["API_KEY"])

    def get_secret_key(self) -> str:
        return self._get_config(key=CONFIG["SECRET_KEY"])

    def get_refresh_token(self):
        return self.smart_connect_obj.generateSession(
            clientCode=self.get_broker_id(),
            password=TRADING_PASSWORD,
            totp=self.totp,
        )

    def get_user_profile(self):
        return self.smart_connect_obj.getProfile(self.refresh_token)

    def get_candle_data(self, param: json = ""):
        return self.smart_connect_obj.getCandleData(param)
