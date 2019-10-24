from spotify import spotify

spotify = spotify()

track_id = spotify.search("Fall for U")
spotify.download_art(track_id)
