from tkinter import *
from pytube import YouTube
import glob
import os

root = Tk()
root.title("YoutubeDownloader")
root.geometry("600x300")
root.configure(bg='grey')


def clear():
    my_text.delete(1.0, END)


def get_mp3():
    link = my_text.get(1.0, END)
    my_label.config(text="Download completed", font=("Helvetica", 11, 'bold'))
    print(link)
    if "https://" in link:
        print("Valid link")
        mp3_downloader(link)
    else:
        print("Invalid link")


def get_mp4():
    link = my_text.get(1.0, END)
    my_label.config(text="Download completed", font=("Helvetica", 11, 'bold'))
    print(link)
    if "https://" in link:
        print("Valid link")
        mp4_downloader(link)
    else:
        print("Invalid link")


def mp3_downloader(link):
    youtube_video = YouTube(link)

    print("################### Download Video ###################")
    print("######## Wait until the download is finished #########")

    to_download = youtube_video.streams.get_audio_only(). \
        download("C:/Downloads")

    print("Video is downloaded")
    print("###### Done ######")
    convert()


def mp4_downloader(link):
    youtube_video = YouTube(link)

    print("################### Download Video ###################")
    print("######## Wait until the download is finished #########")

    to_download = youtube_video.streams.first().download(
        "C:/Downloads")

    print("Video is downloaded")
    print("###### Done ######")
    convert()


def convert():
    print("Converting to mp3.....")

    list_of_files = glob.glob("D:/Downloads/*.mp4")
    sorted_by_mtime_descending = sorted(list_of_files, key=lambda t: -os.stat(t).st_mtime)
    list_of_files.sort(key=os.path.getmtime, reverse=True)
    file = list_of_files[0]
    new_file = file[:-4] + ".mp3"
    os.rename(file, new_file)


my_text = Text(root, width=90, height=5, font=("Helvetica", 14))
my_text.pack(pady=20, padx=10)

button_frame = Frame(root)
button_frame.pack()

next_convert_button = Button(button_frame, text="Next Convert", command=clear,
                             font=("Helvetica", 12, 'bold'), bg='red', fg='white')
next_convert_button.grid(row=0, column=0, padx=10)

mp3_convert = Button(button_frame, text="mp3 Convert", command=get_mp3,
                     font=("Helvetica", 12, 'bold'), bg='red', fg='white')
mp3_convert.grid(row=0, column=1, padx=10, pady=10)

mp4_convert = Button(button_frame, text="mp4 Convert", command=get_mp4,
                     font=("Helvetica", 12, 'bold'), bg='red', fg='white')
mp4_convert.grid(row=0, column=2, padx=10, pady=10)

my_label = Label(root, text="Insert valid url", font=("Helvetica", 10, 'bold'))
my_label.pack(pady=15)

root.mainloop()
