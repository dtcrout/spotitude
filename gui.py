"""Open visualization file as an interactive web app using Eel.

open_visualization(): opens the visualization in browser and exposes functions to eel
"""
from playlist import Playlist
import eel


def open_visualization(spotify, data, time_range):
    """
        Opens index.html file in Chrome (or default browser as fallback) and 
        sets up connection between front-end and Python using Eel in order to 
        handle user interaction within Python code.

        Args
        ----
        spotify: Spotify object
        data: Pandas dataframe
            Top tracks data, needed for playlist creation on button press
        time_range: str
            Time range of top tracks. Possible values are:
                short_term - Approx last 4 weeks
                medium_term - Approx last 6 months
                long_term - All time
    """
    eel.init(".")

    @eel.expose
    def create_playlist():  # pylint: disable=unused-variable
        """
            Handles button press from top tracks visualization and 
            creates Spotify playlist with top tracks
        """
        # Create playlist from top tracks data using Playlist class
        spotitude_playlist = Playlist(spotify)
        spotitude_playlist.create_spotitude_playlist(time_range, data["id"].tolist())
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
        eel.open_url(spotitude_playlist.url)  # open playlist in new window

    eel.start("index.html", mode="chrome")  # default browser as fallback
