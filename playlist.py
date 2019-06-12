import spotipy


class Playlist(object):
    """
    Class for creating, loading and editing Spotify playlists.

     # Examples

        # Create new Spotitude Playlist
        spotitude_playlist = Playlist(spotify)
        spotitude_playlist.create_spotitude_playlist(
            args.time_range, top_tracks_df['id'].tolist())

        # Create custom Spotify Playlist and add tracks
        custom_playlist = Playlist(spotify)
        custom_playlist.create_playlist(
            name='My Playlist', description='This is the coolest playlist ever.')
        custom_playlist.add_tracks(['6nDKrPlXdpomGBgAlO7UdP'])  # Avicii - SOS

        # Load existing Playlist with ID
        existing_playlist = Playlist(
            spotify, playlist_id='0Knc117zgIu3sMSqmrQBzv')

        # Access Playlist attributes/properties
        print('Name:', existing_playlist.name)
        print('Description:', existing_playlist.description)
        print('URL:', existing_playlist.url)
        print('Tracks:', existing_playlist.tracks)

    """

    def __init__(self, spotify, playlist_id=None):
        """
        Initialize Playlist object with the help of the spotify object.

        Parameters
        ----------
        spotify: spotipy.Spotify object of the current session
        playlist_id: optional ID of existing playlist to access

        Raises
        ------
        AuthenticationError
            when an authentication error occurs(e.g. required scopes aren't set)
        """
        self.spotify = spotify  # TODO check scope
        self.user = self.spotify.current_user()  # Spotify Web API dictionary of user

        if playlist_id is None:
            # playlist ID --> used to load all other attributes/properties
            self.identifier = None  # playlist ID
        else:
            # playlist ID --> used to load all other attributes/properties
            self.identifier = playlist_id
            self.playlist  # check if able to load playlist

    def create_playlist(self, name, description):
        """
        Create a new empty playlist for user.

        Parameters
        ----------
        name: str
            Name of the playlist to create
        description: str
            Description of the playlist to create

        Returns
        -------
        None

        Raises
        ------
        AuthenticationError
            when an authentication error occurs
        """

        try:

            result = self.spotify.user_playlist_create(
                self.user["id"], name, public=False, description=description
            )

            self.identifier = result["id"]

        except spotipy.client.SpotifyException:
            raise AuthenticationError

    def create_spotitude_playlist(self, time_range, tracks):
        """
        Create a new spotitude playlist for user(add tracks seperately)

        Parameters
        ----------
        limit: int
            Number of top tracks
        time_range: str in ['short_term', 'medium_term', 'long_term']
            Time range that is covered by top tracks

        Returns
        -------
        None

        Raises
        ------
        TypeError
            Inappropriate time_range
        """
        descriptions = {
            "short_term": "Last 4 weeks",
            "medium_term": "Last 6 months",
            "long_term": "All time",
        }

        track_count = len(tracks)

        if time_range in descriptions.keys():
            name = f"spotitude {descriptions[time_range]}"
            description = f"Top {track_count} tracks for {descriptions[time_range].lower()}. Generated my spotitude.me"
            self.create_playlist(name, description)
            self.add_tracks(tracks)

        else:
            raise TypeError(f"Unkown type {time_range} for time_range.")

    def add_tracks(self, tracks: list, position=None):
        """
        Add tracks to playlist.

        Parameters
        ----------
        tracks: list of tracks
            List of Track IDs to add

        Returns
        -------
        string
            Status code

        Raises
        ------
        AuthenticationError
            when an authentication error occurs
        """
        if self.playlist:
            self.spotify.user_playlist_add_tracks(
                self.user["id"], self.identifier, tracks, position
            )

    @property
    def playlist(self):
        if self.identifier is None:
            raise IDError("Please specify a playlist ID or create a new one.")
        else:
            try:
                playlist = self.spotify.user_playlist(
                    self.user["id"], playlist_id=self.identifier
                )
                return playlist

            except:
                raise IDError("Unkown playlist ID.")

    @property
    def name(self):
        name = self.playlist["name"]
        return name

    @property
    def description(self):
        description = self.playlist["description"]
        return description

    @property
    def url(self):
        url = self.playlist["external_urls"]["spotify"]
        return url

    @property
    def tracks(self):
        tracks = self.playlist["tracks"]["items"]
        return tracks


class AuthenticationError(Exception):
    pass


class IDError(Exception):
    pass
