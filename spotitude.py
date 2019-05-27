"""Spotitude.

Get a user's top 25 tracks and return a 5x5 grid visualization.
"""

from config import Config
from data import get_top_tracks
import spotipy
from visualization import make_visualization


if __name__ == "__main__":
    # Get authentication token for Spotify API
    config = Config()
    token = config.get_token()

    if token:
        spotify = spotipy.Spotify(auth=token)
        # Get user's top tracks
        top_tracks_df = get_top_tracks(
            spotify, limit=25, time_range="short_term", save=True
        )

        # Create visualization
        make_visualization(top_tracks_df)
