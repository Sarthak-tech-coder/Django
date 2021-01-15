from pytube import YouTube
import cv2
import ffpyplayer.player
import requests
import urllib.request
import urllib.parse
import re
query_string = urllib.parse.urlencode({"search_query" : input("Enter song name: ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode())
input2 = "http://www.youtube.com/watch?v=" + search_results[0]
Video = YouTube(input2)
Down = Video.streams.first()
Down.download(filename="file")
thumbnail = Video.thumbnail_url
img = requests.get(thumbnail)
with open('file.jpg', 'wb') as f:
    f.write(img.content)
    f.close()
file = 'file.jpg'
file2 = cv2.imread(file)
file2 = cv2.resize(file2, (800,500))
cv2.imshow('', file2)
player = ffpyplayer.player.MediaPlayer(filename="file.mp4")
while True:
    _, frame = player.get_frame()
    if 0xFFF and cv2.waitKey(7) == ord('q'):
        break
