import pafy
import vlc

#https://stackoverflow.com/questions/49354232/stream-youtube-audio-from-python-using-url-without-downloading-python

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
