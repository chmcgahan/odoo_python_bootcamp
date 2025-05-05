import os
import subprocess
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Authenticate with Spotify
sp = Spotify(auth_manager=SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
))

# Playlist ID to fetch tracks from
# PLAYLIST_ID = "4RVNd8UwGiAqzfPjbgv0O3" #kasabian
PLAYLIST_ID = "5orZL8SetQM1LR3pMXZMOa" #random top 100

# Get playlist tracks
def get_tracks(playlist_id):
    results = sp.playlist_items(playlist_id)
    tracks = []
    for item in results['items']:
        track = item['track']
        if track:
            name = track['name']
            artist = track['artists'][0]['name']
            tracks.append((artist, name))
    return tracks

# Let user select a track
def choose_track(tracks):
    print("\nAvailable tracks:")
    for i, (artist, name) in enumerate(tracks):
        print(f"{i + 1}. {artist} - {name}")

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

def download_track(artist, name):
    query = f"ytsearch1:{artist} {name}"
    filename = f"downloads/{artist} - {name}.mp3"
    os.makedirs("downloads", exist_ok=True)
    print(f"\nDownloading: {artist} - {name}")
    subprocess.run([
        'yt-dlp', '-x', '--audio-format', 'mp3',
        '-o', filename,
        query
    ])
    print(f"Saved to {filename}")

# Main loop
def main():
    print("=== Spotify Playlist Downloader ===")
    tracks = get_tracks(PLAYLIST_ID)

    while True:
        selected = choose_track(tracks)
        if not selected:
            print("Goodbye!")
            break
        artist, name = selected
        download_track(artist, name)

if __name__ == "__main__":
    main()
