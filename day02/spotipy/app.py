import os
import subprocess
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Track:
    def __init__(self, artist: str, name: str):
        self.artist = artist
        self.name = name

    def __str__(self):
        return f"{self.artist} - {self.name}"

class SpotifyDownloader:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.sp = Spotify(auth_manager=SpotifyClientCredentials(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
        ))

    def get_tracks(self):
        results = self.sp.playlist_items(self.playlist_id)
        tracks = []
        for item in results['items']:
            track_data = item.get('track')
            if track_data:
                name = track_data['name']
                artist = track_data['artists'][0]['name']
                tracks.append(Track(artist, name))
        return tracks

    def choose_track(self, tracks):
        print("\nAvailable tracks:")
        for i, track in enumerate(tracks):
            print(f"{i + 1}. {track}")

        while True:
            try:
                choice = int(input("\nEnter the number of the track to download (0 to quit): "))
                if choice == 0:
                    return None
                if 1 <= choice <= len(tracks):
                    return tracks[choice - 1]
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a number.")

    def download_track(self, track: Track):
        query = f"ytsearch1:{track.artist} {track.name}"
        filename = f"downloads/{track.artist} - {track.name}.mp3"
        os.makedirs("downloads", exist_ok=True)
        print(f"\nDownloading: {track}")
        subprocess.run([
            'yt-dlp', '--quiet', '-x', '--audio-format', 'mp3',
            '-o', filename,
            query
        ])
        print(f"Saved to {filename}")

def main():
    print("=== Spotify Playlist Downloader ===")

    # Change this ID for other playlists
    playlist_id = "5orZL8SetQM1LR3pMXZMOa"
    
    downloader = SpotifyDownloader(playlist_id)

    tracks = downloader.get_tracks()

    while True:
        selected_track = downloader.choose_track(tracks)
        if not selected_track:
            print("Goodbye!")
            break
        downloader.download_track(selected_track)

if __name__ == "__main__":
    main()


# === EXOS ===

# Add a loop to download several tracks in a row OR
# Let users choose multiple tracks one after another before quitting.

# Create a Playlist class
# That holds the list of Track objects and a method like show_downloaded_tracks() to see what has already been downloaded

# Add a display_name() method to Track
# To centralize how we show a track (instead of formatting everywhere).

# Ask the user for the playlist URL
# Instead of hardcoding it, let the user paste a link.

# Sort tracks alphabetically before displaying them
# Practice sorting and working with lists of objects.

# Add a confirmation before downloading
# A simple Are you sure? (y/n) prompt after selection.

# Count and show how many tracks are in the playlist
# Add a .count() method or just print len(tracks).

# Show a progress message while downloading
# Something like Downloading 1 of 3: Artist - Track.

# Save downloaded track info in a text file
# Like downloaded.txt to practice working with files.

# Create a simple logo or header printed with ASCII art
# For fun, and to make the script feel more personal.