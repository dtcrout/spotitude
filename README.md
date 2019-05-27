# Spotitude

Yet another Spotify user analytics visualizer!

Spotify unfortunately doesn't provide users their top tracks. Spotitude is a simple visualization tool for your top 25 tracks. It produces a 5x5 grid of your top tracks along with their names.
You can take a screenshot of this visualization and share it with other music fans on your favorite forums or image boards!

![Example](examples/example.png)

### Requirements
* Python 3
* pip3
* Access to Spotify's API

### Getting Started

First, install the dependencies by running:

```
$ make deps
```

After the dependencies are installed, we need to configure the credentials. Spotitude requires the user to have access to [Spotify's API](https://developer.spotify.com/).
Once you have finished creating your app and have your credentials, we need to create a config file to save your credentials. To create a config file, run:

```
$ make config
```

Open up the newly created `spotitude.config` and input your credentials.

### Create Visualizations!

To create your visualization, run:

```
$ python3 spotitude.py
```
