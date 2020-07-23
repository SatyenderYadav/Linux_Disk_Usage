#!/bin/bash/python3

import sys
import os
def size(path):
	total  = 0

	for entry in os.scandir(path):
		try:
			if entry.is_dir(follow_symlinks=False):
			 	total += size(entry.path)
			 	
			else:
				total += entry.stat(follow_symlinks=False).st_size
		except :
			total+=0
	return total

if __name__ == '__main__':
	os.system('clear')
	banner = """\033[1m\033[91m
\t\t·▄▄▄▄  ▪  .▄▄ · ▄ •▄     ▄• ▄▌.▄▄ ·  ▄▄▄·  ▄▄ • ▄▄▄ .
\t\t██▪ ██ ██ ▐█ ▀. █▌▄▌▪    █▪██▌▐█ ▀. ▐█ ▀█ ▐█ ▀ ▪▀▄.▀·
\t\t▐█· ▐█▌▐█·▄▀▀▀█▄▐▀▀▄·    █▌▐█▌▄▀▀▀█▄▄█▀▀█ ▄█ ▀█▄▐▀▀▪▄
\t\t██. ██ ▐█▌▐█▄▪▐█▐█.█▌    ▐█▄█▌▐█▄▪▐█▐█ ▪▐▌▐█▄▪▐█▐█▄▄▌
\t\t▀▀▀▀▀• ▀▀▀ ▀▀▀▀ ·▀  ▀     ▀▀▀  ▀▀▀▀  ▀  ▀ ·▀▀▀▀  ▀▀▀                                                                               

           \t\t\t\t\t\t\033[92m- By l3v1ath4n
    """
	print(banner)
	
	directory = input("\n\033[1m\033[34mEnter the directory or path of the directory you want size : ")
	for entry in os.scandir(directory):
		if entry.is_dir(follow_symlinks=False):
			
			sizes = size(entry.path)
			kb = round(sizes/1024,3)
			Mb = round(kb/1024,3)
			Gb = round(Mb/1024,3)
			if Gb > 1:
				print("\n\033[1m\033[36mDirectory : " + str(entry.path))
				print("\033[1m\033[36mTotal Size : "+ str(Gb)+" Gb")
			else:
				if Mb>1:
					print("\n\033[1m\033[36mDirectory : " + str(entry.path))
					print("\033[1m\033[36mTotal Size : "+ str(Mb)+" Mb")
				else:
					print("\n\033[1m\033[36mDirectory : " + str(entry.path))
					print("\033[1m\033[36mTotal Size : "+ str(kb)+" Kb")
			print()					