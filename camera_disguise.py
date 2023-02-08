import sys
import os
from subprocess import run
import multiprocessing
from multiprocessing import freeze_support
from subprocess import DEVNULL
def cmd_generator(mimic_model):
     if mimic_model=="7RM5":
        return 'exiftool -uniquecameramodel="Sony ILCE-7RM5" - -model="ILCE-7RM5" -make="SONY" -overwrite_original_in_place '
     if mimic_model=="X-H2":
        return 'exiftool -uniquecameramodel="Fujifilm X-H2" -model="X-H2" -make="FUJIFILM" -overwrite_original_in_place '

def process(filepath,current_model,mimic_model):
        if filepath:
            cmd = 'exiftool "'+filepath+'" |grep "Camera Model Name"'
            run_result=run(cmd, capture_output=True,shell=True).stdout.decode("utf_8")
            if(run_result.__contains__(current_model)):
                    cmd2 = cmd_generator(mimic_model)+'"'+filepath+'"'
                    run(cmd2,capture_output=False,shell=True)
                    return str("modified\t"+filepath+"\tto\t"+mimic_model)

if __name__ == '__main__':
    freeze_support()
    try:
        run("exiftool",shell=True,capture_output=False,stdout=DEVNULL)
    except:
        print("exiftool not found, please install exiftool first!")
        sys.exit

    #     try:
    #         run("brew install exiftool",shell=True)
    #     except:
    #          print("brew is not installed, installing brew and exiftool")
    #          time.sleep(3)
    #          run('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"',shell=True)
    #          print("brew installed.")
    #          try:
    #               run("brew install exiftool",shell=True)
    #          except:
    #               print("something went wrong, please retry")
        


    args = sys.argv
    if len(args)==1:
        print("how to use:")
        print("please convert the files to DNG first, using the Adobe DNG Convert Tool")
        print("command:")
        print("python camera_disguise.py directory_path <your_model> <target_model>")
        print("try X-H2 for most fuji-matched recipes")
        print("try 7RM5 for BionzXR recipes")
        print("examples:--------------------------")
        print("python camera_disguise.py /User/JohnDoe/Desktop 7RM4 7RM5")
        print("if there's a space in your path, please use a quote to make sure it can be read correctly:")
        print("python camera_disguise.py '/User/John Doe/Desk top' 7RM4 7RM5")
        print("-----------------------------------")
        print("This disguises your camera from A7R4 to A7R5")
        sys.exit()
    x=""
    current_model=""
    mimic_model=""
    x=args[1]
    current_model=args[2]
    mimic_model=args[3]
    res=[]
    if args[1]:
        print("location: ",args[1])
        rootdir=args[1]  
        for root, subFolders, files in os.walk(rootdir):
            for name in files:
                if name.endswith(("dng","DNG")):
                    x=os.path.join(root,name)
                    res.append(x)
    p=multiprocessing.Pool()
    y_results=[]
    for x in res:
        y=p.apply(process,(x,current_model,mimic_model))
        if y:
             y_results.append(y)
    for items in y_results:
         print(items)
    p.close()
    p.join()