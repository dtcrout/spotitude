"""Spotitude.

Get a user's top 25 tracks and return a 5x5 grid visualization.
"""

from config import Config
from data import get_top_tracks
import spotipy
from visualization import make_visualization
from playlist import Playlist
import argparse
import eel

if __name__ == "__main__":
    # Parse the input parameters.
    parser = argparse.ArgumentParser(description="Spotitude Customization")
    parser.add_argument(
        "--time_range",
        type=str,
        default="short_term",
        help="Over what time frame the top tracks are computed. "
        + "Valid values: long_term, medium_term and short_term. (default: short_term)",
    )
    args = parser.parse_args()
    if args.time_range not in ["short_term", "medium_term", "long_term"]:
        raise ValueError(
            "Valid values for time_range are: long_term, medium_term and short_term."
        )

    # Get authentication token for Spotify API
    config = Config()
    token = config.get_token()

    if token:
        spotify = spotipy.Spotify(auth=token)
        # Get user's top tracks
        top_tracks_df = get_top_tracks(
            spotify, limit=25, time_range=args.time_range, save=True
        )

        # Create visualization
        make_visualization(top_tracks_df)

        eel.init(".")

        @eel.expose
        def create_playlist():
            """
                Handles button press from top tracks visualization
            """
            spotitude_playlist = Playlist(spotify)
            spotitude_playlist.create_spotitude_playlist(
                args.time_range, top_tracks_df["id"].tolist()
            )
            print(
                f"Playlist '{spotitude_playlist.name}' created.\n{spotitude_playlist.url}"
            )

            # Change 'Create Playlist' to 'Open Playlist' and write hidden URL to html file
            with open("index.html", "r") as spot_html:
                filedata = spot_html.read()
                filedata = filedata.replace("Create Playlist", "Open Playlist")
                # Change onclick action to open playlist url, also possible independent from python script
                filedata = filedata.replace(
                    "onclick='create_playlist()'",
                    f"onclick=\"window.open('{spotitude_playlist.url}','_blank','resizable=yes')",
                )

            with open("index.html", "w") as spot_html:
                spot_html.write(filedata)

            # pylint: disable=no-member
            eel.open_url(spotitude_playlist.url)  # open playlist in web browser

        eel.start("index.html", mode="chrome")
