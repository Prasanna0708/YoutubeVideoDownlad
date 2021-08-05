from pytube import YouTube

url = 'https://www.youtube.com/watch?v=DbMejWoW1XI'
my_video = YouTube(url)
# getting video title...
print(my_video.title)

#getting Thumnail image...
print(my_video.thumbnail_url)

#downloading youtube video
my_video = my_video.streams.get_highest_resolution()
# or we can use this type by using first()--->
#my_video = my_video.streams.first()
#or
#for stream in my_video.streams:
 #   print(stream)
#my_video.download()

