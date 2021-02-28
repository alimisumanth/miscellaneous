import os
import shutil

user = os.environ['USERNAME']#To get the user's username
#storing the default spotlight lockscreen images in a variable named soure_path
source_path=r'C:\Users\\'+user+'\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'

#prompt to get custom defined destination path
destination_folder = input('Do you want to choose custom destination folder? if yes provide the path else press enter')
if len(destination_folder)<1 and not os.path.isdir(destination_folder):
     destination_folder=os.getcwd() 

#Copying the files to destination path and adding .png extension to it	 
for f in os.listdir(source_path):
    if os.path.isfile(source_path+'//'+f):
        if (not f.endswith('png')) and (not f.endswith('.py')):
            shutil.copyfile(source_path+"\\"+f,destination_folder+'\\'+f+'.png')