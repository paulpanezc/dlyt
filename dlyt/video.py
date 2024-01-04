from pytube import YouTube
from threading import Thread


YOUTUBE_URIS = [
    'https://youtube.com/watch?v=',
    'https://youtu.be/',
    'https://www.youtube.com/watch?v='
]
VIDEO_EXTENSIONS = [
    'mp4',
    'webm'
]


class Video(Thread):
    def __init__(self, url, path):
        super().__init__()
        self.url = url
        self.path = path
        self.message = ''
    
    def run(self):
        main_stream = None
        for uri in YOUTUBE_URIS:
            if self.url.startswith(uri):
                streams = YouTube(self.url).streams
                for extension in VIDEO_EXTENSIONS:
                    _streams = streams.filter(progressive=True, file_extension=extension)
                    if len(_streams) > 0:
                        streams = _streams.order_by('resolution').desc()
                        if len(streams) > 0:
                            main_stream = streams.first()
                            try:
                                main_stream.download(self.path)
                                self.message = 'Complete download.'
                            except FileNotFoundError as e:
                                self.message = "Video cannot be downloaded in the directory specified. {}".format(str(e))
                            break
                if not main_stream:
                    self.message = 'Video is in unrecognized format.'
                break
        if not main_stream:
            self.message = 'Please enter a valid Youtube URL.'   
