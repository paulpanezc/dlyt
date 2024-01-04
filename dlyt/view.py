from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import os
from dlyt.video import Video


class View():
    def __init__(self):
        self.window = Tk()
        self.frame = ttk.Frame(self.window, padding=10)
        self.entry_content = StringVar()
        self.entry =  ttk.Entry(self.frame, width=50, textvariable = self.entry_content)
        self.button = ttk.Button(self.frame, text="Download", command=self.handle_download) # state=DISABLED
        self.progressbar = ttk.Progressbar(self.frame, length=450)
    
    def show(self):
        self.window.title('Youtube Downloader')
        self.window.resizable(width=False, height=False)
        self.frame.grid()
        ttk.Label(self.frame, text="Youtube URL").grid(column=0, row=0)
        self.entry.grid(column=1, row=0)
        self.entry.focus()
        self.button.grid(column=2, row=0)
        self.progressbar.grid(columnspan=5, row=3)
        self.window.mainloop()

    def get_entry(self):
        if self.entry_content:
            return self.entry_content.get()
        else:
            return None
    
    def handle_download(self):
        url = self.get_entry()
        path = os.path.abspath(filedialog.askdirectory())
        if url and path:
            self.start_downloading()
            youtube_video = Video(url, path)
            youtube_video.start()
            self.monitor(youtube_video)
    
    def start_downloading(self):
        self.frame.tkraise()
        self.progressbar.start()

    def stop_downloading(self, video):
        self.frame.tkraise()
        self.progressbar.stop()
        messagebox.showinfo(title=None, message=video.message)
    
    def monitor(self, download_thread):
        if download_thread.is_alive():
            self.window.after(100, lambda: self.monitor(download_thread))
        else:
            self.stop_downloading(download_thread)
