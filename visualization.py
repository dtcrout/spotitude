"""Create visualization for user's Spotify track data.

Visualize top 25 tracks from dataframe and display them in a 5x5 grid.
"""

import pandas as pd

PATH = "visualization.html"


def opening():
    """HTML boilerplate."""
    return """<html>\n<table style="width:0%">\n<tr>\n"""


def closing():
    """HTML boilerplate."""
    return """</tr>\n</html>"""


def new_entry(path, scale=40):
    """Insert album art in table.

    Args
    ----
    path: str
        Path to album art image.
    scale: int
        Percentage of image scaling.
    """
    entry = """<td><img src="{}", style="height:{}%;"></td>\n""".format(path, scale)
    return entry


def tracks_entry(tracks):
    """
    Insert tracks for table row.

    Args
    ----
    tracks: list
        Tracks for row of 5 album art covers.
    """
    tracks_entry = """<td><p>{}<br>{}<br>{}<br>{}<br>{}</p></td>\n""".format(*tracks)
    return tracks_entry


def get_track_entries(top_tracks_df, start_index, end_index):
    """
    Get 5 row slice of dataframe and make track strings.

    Args
    ----
    top_tracks_df: Pandas dataframe
        User top tracks dataframe.
    start_index: int
        Start index of slice of dataframe.
    end_index: int
        End index of slice of dataframe.

    Returns
    -------
    track_entries: list
        List of tracks for row of table.
    """
    slice = top_tracks_df.iloc[start_index:end_index]
    artists = slice["artist"].values
    tracks = slice["track"].values
    track_entries = [artist + " - " + track for artist, track in zip(artists, tracks)]
    return track_entries


def make_visualization(top_tracks_df, path=PATH):
    """Make visualization HTML file.

    Args
    ----
    top_tracks_df: Pandas dataframe
        User top tracks dataframe.
    path: str
        Path to save visualization.
    """
    with open(path, "w") as f:
        f.write(opening())

        for index, row in top_tracks_df.iterrows():
            album_art = row["album_art"]
            entry = new_entry(album_art)

            if index % 5 == 0 and index != 0:
                track_entries = get_track_entries(top_tracks_df, index - 5, index)
                f.write(tracks_entry(track_entries))
                f.write("</tr>\n<tr>\n")
            f.write(entry)

        track_entries = get_track_entries(top_tracks_df, 20, 25)
        f.write(tracks_entry(track_entries))

        f.write(closing())
