import requests
import cv2
import os
import numpy
import json
import database
nasaKey = "g16onw6OFs5dXytx5gNiFBzrqr4XIRB5baxzo5rj"
link = f"https://api.nasa.gov/planetary/apod?api_key={nasaKey}"


class nasalink:
    def defi(self):
        print('Starting Process')
        self.link = link
        self.page_content = requests.get(self.link)
        self.decoded_page = self.page_content.content.decode()
        print('decoding')
        self.json = json.loads(self.decoded_page)
        print('json')
        self.title = self.json['title']
        self.url = self.json['url']
        print('getting img')
        self.pic = requests.get(self.url)
        print('database')
        database.obj.input2(self.url, self.title)
        print('writing ing')
        with open('pic.jpg', 'wb') as f:
            f.write(self.pic.content)
            f.close()
        print('img writen')
    def show(self):
        print('img showing')
        frame = cv2.imread("pic.jpg", 1)
        np2 = numpy.array([(0, 900), (900, 900), (0, 850), (900, 850)], numpy.int32)
        frame = cv2.resize(frame, (500,500))
        cv2.putText(frame,  str(self.title), (0, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
        cv2.imshow("", frame)
        cv2.waitKey(0)
        os.remove("pic.jpg")
    def prin(self):
        database.obj.show()

if __name__ == "__main__":
    obj = nasalink()
    obj.defi()
    obj.show()
    obj.prin()
