"""Load Spotify API credentials and create token."""

import configparser
from spotipy import util

CONFIG = configparser.ConfigParser()
CONFIG.read("spotitude.config")


class Config:
    def __init__(self):
        self.config = CONFIG["DEFAULT"]
        self.username = self.config["USERNAME"]
        self.scope = self.config["SCOPE"]
        self.redirect_uri = self.config["REDIRECT_URI"]
        self.client_id = self.config["CLIENT_ID"]
        self.client_secret = self.config["CLIENT_SECRET"]

    def get_token(self):
        """Get API access token."""
        token = util.prompt_for_user_token(
            self.username,
            self.scope,
            self.client_id,
            self.client_secret,
            self.redirect_uri,
        )
        return token
