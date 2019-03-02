from pytube import YouTube
import os

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

downloadYouTube('https://www.youtube.com/watch?v=4wOlvx8igzk&list=PLDs6Txl1GILzoZmUQpJkZf9o8ZkaMFKcB', '/Users/hamzakhan/Documents/GitHub/cookieMonster/youtubeIronmanMP4')