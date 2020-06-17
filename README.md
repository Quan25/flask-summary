# Flask Summary

** PreSumm modules was originally from https://github.com/nlpyang/PreSumm **

Features
--------
 * generate summary on given text

Installation In A Nutshell (on localhost)
--------------------------
 1. Install [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#installation)
 2. pyrouge is an essential module for PreSumm to run, please follow the instruction [here](https://github.com/bheinzerling/pyrouge) about how to install pyrouge
 3. Please install pytorch 1.1.0 with this comand
### GPU
```
  conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch
```
## CPU Only
```
conda install pytorch-cpu==1.1.0 torchvision-cpu==0.3.0 cpuonly -c pytorch
```
 4. Run `python app.py` in the flask-summary directory.
 5. Start web server by running `python app.py` while in the server_example directory.
 6. Browse the examples using a browser. *(defaults to port `5000`)*
