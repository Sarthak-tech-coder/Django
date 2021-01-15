from pytube import YouTube
import cv2
import ffpyplayer.player
import os
class tube:
    def download(self):
        self.input = input("Please Enter Video Url: ")
        self.install()
    def install(self):
        self.Video = YouTube(self.input)
        self.Down = self.Video.streams.first()
        self.Down.download(filename="file")
        self.play()
    def play(self):
        df = cv2.VideoCapture("file.mp4")
        audio = ffpyplayer.player.MediaPlayer("file.mp4")
        while True:
            frame, vid = df.read()
            g, fram = audio.get_frame()
            if fram is not None:
                cv2.imshow('', vid)
            else:
                break
            if 0xFFF and cv2.waitKey(30)== ord('q'):
                break
    def delete(self):
        os.remove('file.mp4')
obj = tube()
obj.download()
obj.delete()
