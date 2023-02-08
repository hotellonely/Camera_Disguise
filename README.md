# Camera_Disguise
A small python+exiftool script tool to disguise your RAW files, enabling different Camera Matching Profiles in Adobe Camera Raw or Lightroom. 

# Requirements
- Python 3
- Exiftool: 
see the installation guide here: https://exiftool.org/install.html
- A DNG Converter to convert the RAW file to DNG:
https://helpx.adobe.com/camera-raw/using/adobe-dng-converter.html
- You can also use the Lightroom to convert your files in library to DNG, see guide here:
https://fstoptraining.com/convert-raw-files-to-dng/

# Usage:
In the commandline / terminal:
to get help:
python camera_disguise.py

typical usage:
```
python camera_disguise.py "path to your dng files" "your camera model" "disguise model"
```
e.g.
Windows:
```
python camera_disguise.py "C:\Photos To Edit\" A7R4 A7R5
```
```
python camera_disguise.py "C:\Photos\" A7S3 A7R5
```
Mac/Linux:
```
python camera_disguise.py "/Volumes/MyBigSSD/Photos/" A7S3 A7R5
```
