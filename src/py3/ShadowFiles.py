#ShadowFile Linux version python 2.x
#Github author address: https://github.com/tetration
#Contact: Tetration@outlook.com
#Written for Python 2.x and 3.x
#Warning This version is for Python 3 Only!
import os

path =  os.getcwd()
filenames = os.listdir(path)

def Welcome():
	print("ShadowFiles the script that helps you hide or show files in a folder")

def Question():
	
	print("Would you like to show hidden files or hide visible files in the current directory(where this script is located at)?")
	print("Type: 1 to hide files")
	print("Type: 2 to make files visible again")
#	print("Type: 3 to change directory before deciding what to do") [PART OF THE CODE THAT NEEDS FIXING]
	user=str(input())
	if user=='1':
		HideFiles()
		
	if user=='2':
		ShowFiles()
	else:
		print("Please type 1 or 2")
		Question()

# Code that I needs fixing to add later on before adding to the script
#	if user=='3':
#		ChangeDir()
#
#	elif user!='1' or user!='2' or user!='3':
#		print("Please type 1, 2 or 3!")
#		Question()
#
#
# if we added the .lower() option it would also make all filenames lowercase

#def ChangeDir():
#	print("Please type the directory then")
#	print("Example: /home/YourUsername/Desktop/Folder_that_you_want_to_Hide_or_show_files")
#	path=raw_input()
#	os.chdir(path)
#	filenames = os.listdir(path)
#	print("Directory changed! Returning to mainmenu...")
#	Question()
#
def ShowFiles():
	for filename in filenames:
			if filename[0]=='.' and filename!='ShadowFiles.py':
				os.rename(filename,filename.replace(filename,filename[1:]))#When placing filename[1:] we are asking for everything except the first letter of it

	print("Files are visible now!")
	exit()
def HideFiles():
	for filename in filenames:
			if filename!='ShadowFiles.py' and filename[0]!='.':
					os.rename(filename,filename.replace(filename, "."+filename))
	print("Files are hidden now!")
	exit()

#os.rename(filename, filename.replace(filename, "."+filename).lower()) 
# the .lower() makes all letters of the filename lowercase 
def main():
	Welcome()
	Question()


#Starts the script
main()