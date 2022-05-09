import os, ffmpeg
import glob, os
import sys

if __name__ == "__main__":
	address = sys.argv[1:]
	os.chdir(address[0])
	for file in glob.glob("*.m4s"):
		if file.endswith(".m4s") and file != "all.m4s":
			os.system(f'cat {file} >> all.m4s')
	os.system("ffmpeg -i all.m4s -c copy video.mp4")