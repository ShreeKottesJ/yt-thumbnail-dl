import os
import wget
import pafy

#Getting video URL
base_url = input("Enter YouTube URL: ")
print("Please wait..!")

#Getting Video ID using pafy
video = pafy.new(base_url)
get_id = video.videoid

#Using the Video ID creating link and downloading with wget
thumbnailurl = f'https://img.youtube.com/vi/{get_id}/maxresdefault.jpg'
print("Downloading Thumbnail... \n")
wget.download(thumbnailurl)

# Renaming Thumbnail with Youtube ID
os.rename("maxresdefault.jpg", get_id+".jpg")
print("\n Thumbanil Downloaded succesfully.")
