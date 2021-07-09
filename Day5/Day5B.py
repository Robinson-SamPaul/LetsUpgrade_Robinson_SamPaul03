from pytube import YouTube

print("\tYouTubeDownloader")

url = "https://www.youtube.com/watch?v=kMwAsGfNGMA&t=4s"
myVideo = YouTube(url)

print(myVideo.title)
print(myVideo.thumbnail_url)

myVideo = myVideo.streams.get_highest_resolution()
myVideo.download()
