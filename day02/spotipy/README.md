# Our very own super first app : Flask Spotify Playlist Downloader

This is a minimal Flask web application that connects to the **Spotify API** to fetch a playlist's tracks and uses **yt-dlp** to download them from YouTube as MP3 files. It’s a practical way to learn about APIs, Flask, and external command usage from Python.

---

##  What You’ll Learn

- How to use environment variables to store API keys
- How to interact with the Spotify Web API via `spotipy`
- How to send data between Flask views and HTML templates
- How to download audio with `yt-dlp` using `subprocess`

---

### 1. Register your app on Spotify for developers to gain access to your API credentials.

The client ID is your app's public usernmae. The client secret is your app secret password
Together, they identify and authenticate your app when it makes requests to the Spotify API.

You get both by registering your app at:

[https://developer.spotify.com/dashboard]

- Log in with your Spotify account
- Create an app
- Copy the Client ID and Client Secret
- Paste them into your .env

### 2. Once your program is up and running, let's try to improve this ! Do any of the following points, in ascending order of dicculty (kinda)

- Download multiple tracks at once: Modify the program so the user can enter multiple track numbers separated by commas (e.g. 1,3,5) and all selected songs are downloaded.
- Filter the track list: Let the user enter a search keyword (e.g. "drake") and only display matching tracks before prompting for download.
- Add track duration display: Show each track's duration in minutes and seconds alongside the title (e.g. Drake - God's Plan (3:18)).
- Handle duplicate file names: Prevent overwriting downloaded MP3 files. If a file already exists, add a number like -1, -2, etc., or ask the user whether to skip, overwrite, or rename.
- Random track download: Add an option to randomly download one song from the playlist without user input.
- Download the full playlist: Add an option to download all tracks in the playlist at once (warn the user and confirm before proceeding).
- Progress feedback: Show a progress bar or simple "downloading X of Y" message when downloading multiple songs.
- Choose from multiple playlists: Let the user choose between several predefined playlist IDs (e.g. rock, pop, rap). Use a dictionary to store playlist names and IDs.
- Download history log: Keep a log file (e.g. downloaded.txt) that records each downloaded song with timestamp. Before downloading, check if it’s already been downloaded.
- Pretty print the list in a table: Format the song list into neat columns (e.g. using str.ljust() or tabulate) so it looks more polished in the terminal.
