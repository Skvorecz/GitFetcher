import glob
import subprocess

print ('Fetching in git folders:')
for gitName in glob.glob(''):
    index = gitName.find(".git")
    folder = gitName[:index]
    print (folder)

    subprocess.Popen("git fetch", cwd=folder)