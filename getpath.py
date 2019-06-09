import os

# get the current root path
rootPath = os.getcwd()

# define folder name
folderName = 'Documents'

# define full path
fullPath = os.path.join(rootPath,folderName,'0python')

# P\rint ful\l path#
print(fullPath)

# define a certain target path
targetPath = 'C:\\Users\\INKOM06\\Pictures\\Dataset186\\906'
#fileNames = os.listdir(fullPath)
fileNames = os.listdir(targetPath)

# count total file inside the target path
nof = len(fileNames)

# list the file names
for i in range (0,nof):
	print(str(i+1)+' '+fileNames[i])	

# list the file names with complete paths  
for i in range (0,nof):
	print(targetPath+'\\'+fileNames[i])
