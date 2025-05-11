ffmpeg -framerate 10 -i image_%05d.jpg -c:v libx264 -pix_fmt yuv420p output.mp4
#This is rebuild the files into one video
