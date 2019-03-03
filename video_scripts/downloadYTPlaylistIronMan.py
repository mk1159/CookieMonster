from pytube import Playlist
pl = Playlist("https://www.youtube.com/playlist?list=PLDs6Txl1GILzoZmUQpJkZf9o8ZkaMFKcB")
#pl.download_all()
# or if you want to download in a specific directory
pl.download_all('./cookieMonster/youtubeIronmanMP4')  #changed unnecessary directory
