from pytube import Playlist
pl = Playlist("https://www.youtube.com/playlist?list=PLzwP33RAZTVA7-IxNZWCEr4rDZn2_PQ_F")
#pl.download_all()
# or if you want to download in a specific directory
pl.download_all('./cookieMonster/allElse') #changed unnecessary directory
