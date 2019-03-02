from pytube import Playlist
pl = Playlist("https://www.youtube.com/playlist?list=PLDs6Txl1GILzoZmUQpJkZf9o8ZkaMFKcB")
#pl.download_all()
# or if you want to download in a specific directory
pl.download_all('/Users/hamzakhan/Documents/GitHub/cookieMonster/youtubeIronmanMP4')