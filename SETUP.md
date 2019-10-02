# Spotitude Credentials Setup

Once you have finished creating your app and have your credentials, we need to create a config file to save your credentials. To create a config file, run:

```
$ make config
```

Once you've run make config, there should be a file in the main directory that looks like this:
![Example] (examples/default_config.png)

### Entering Your Credentials
Now, you will need to enter your credentials

* For USERNAME, input your Spotify username, so that it reads USERNAME=yourUsername. 
* You should not need to modify the SCOPE variable. 
* You don't need to modify REDIRECT_URI either, but be sure that you have added this redirect uri to your app settings as disccused in the [README](README.md).

You will find the values that you need for CLIENT_ID and CLIENT_SECRET through the Spotify for Developers' [Dashboard](https://developer.spotify.com/dashboard/applications). The dashboard screen should look like this:
![Example] (examples/dashboard.png)
Click on the app that you created earlier. When you click on the app that you created, it should look like this:
![Example] (examples/app_info.png)
In the CLIENT_ID and CLIENT_SECRET fields in your `spotitude.config`, input the Client Id and Client Secret Key as they appear in your broswer.

Your `spotitude.config` file should now be ready to go!