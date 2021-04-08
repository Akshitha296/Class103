import os
import shutil

source = input("Enter folder name here.")
destination = input("Where do you want the files to go?")
source = source+'/'
destination = destination+'/'
list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)