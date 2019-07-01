"""Get user data from Spotify API.

get_top_tracks(): Get user's top 25 tracks for a given time period.
"""

import pandas as pd
import spotipy


def get_top_tracks(spotify, limit=25, time_range="short_term", save=False):
    """Call the Spotify API and get a user's top 25 tracks for time period.

    Args
    ----
    spotify: Spotify object
    limit: int
        Number of tracks to return.
    time_range: str
        Time range of top tracks. Possible values are:
            short_term - Approx last 4 weeks
            medium_term - Approx last 6 months
            long_term - All time
    save: boolean
        Flag to save data to csv file.

    Returns
    -------
    top_tracks_df: Pandas dataframe
        Dataframe with:
            artist
            album
            track
            album_art
            id
    """
    # Create dataframe to store values
    top_tracks_df = pd.DataFrame(
        columns=["artist", "album", "track", "album_art", "id"]
    )

    # Call Spotify API to get user top tracks
    top_tracks = spotify.current_user_top_tracks(limit=limit, time_range=time_range)

    for n, item in enumerate(top_tracks["items"]):
        artist = item["album"]["artists"][0]["name"]
        album = item["album"]["name"]
        track = item["name"]
        album_art = item["album"]["images"][1]["url"]
        identifier = item["id"]

        # Append data to dataframe
        top_tracks_df = top_tracks_df.append(
            {
                "artist": artist,
                "album": album,
                "track": track,
                "album_art": album_art,
                "id": identifier,
            },
            ignore_index=True,
        )

    if save:
        f_name = "top_" + str(limit) + "_" + time_range + ".csv"
        top_tracks_df.to_csv(f_name)

    return top_tracks_df
