# AutomaticVideoDashboard_Blender
This project permit to animate a dashboard in Blender starting from data stored in a CSV file. A very simple example of the capability is shown in the gif below.

<p align="center">
<img align="center" width="60%" src="example.gif">
</p>

## Features
* Make animated line chart;
* Make text change during the animation by imposing a value for each frame;
* Show and hide some object to obtain notification effect.

All the data can be setted using a CSV file.

## How to use it

In Example.blend you can find a totally working example but before of use it you have to do the setup.

### Setup

I used it under Linux and I can't garantee that it works properly on Windows(if you try it under Windows feel free to give me some feedback).

#### Linux
First of all you have to create the environment. 
```
cd /../../folder_containing_this_project
virtualenv -p python3 venv  #Only the first time
source venv/bin/activate    #Every time
pip install pandas          #Only the first time
```
Now you have to open blender from the same terminal you run ```source venv/bin/activate```, usually it's enough to run the command ```blender```.

For more information of why we made it, look at: https://medium.com/@playgrdstar/data-analytics-in-blender-pandas-and-quandl-in-blender-d3c816237921 .

#### Windows

Since I never run it under Windows I have no procedure yet but this link should be helpful: https://blender.stackexchange.com/a/140343/98558 . The only external package needed for the code is pandas.

### Usage of the Example.blend
I suggest to start with Example.blend to understand how everything work.

1. Open Blender as specified above.
2. If the tab Text editor is close, open it. Than in the tab Text editor open the fil Dashboard.py.
3. Set the first three variable: **KEY_COLUMN_LINE_CHART** should contains all the column name of the data.csv corresponding to a line chart, **MAKE_LINE_GRAPH** should be true if you want to make line charts, by putting false, it permit to don't do the line chart and so save time, remember that every time this variable is at true, the old line chart will be delete and than new one are made, **current_folder** path of the folder containing this repository.
4. Press Run Script.

#### Create your own dashboard

First of all you have to create the data. The file should be a csv as the one in the example. Pay attention to the column name, they are very important to make the scripts work. There are three possible type of columns:
* *line chart*: it should contain in each row a number;
* *text*: the name of the column has to be of the type "text_..." and what you want instead of "...". The name has to correspond to a Text object in the Blender scene with the same exact name. The element of the columns can be whatever, they will be the one shown in the Scene, remember that every element will be remain visibile for only one frame, so repeat the element multiple time if you want it visible for multiple frames;
* *notification*: the name of the column has to be of the type "not_..." and what you want instead of "...". The name has to correspond to an object in the Blender scene with the same exact name and another with the same exact name plus a "\_off" at the end. The element of this column can be TRUE or FALSE, at true the object with the name as the column will be shown, when false, the one with the "\_off" at the end will be shown.

**NOTE**: For the line chart you need to do it one time only until you change the data, instead for the texts and the notifications, you have to run the script every time you open Blender.

After you run the code you can personalize position and materials of the different object to make the dashboard as you like more.

## Alternative

If you need to do something more static I suggest you this other plugin https://github.com/Griperis/BlenderDataVis from where I took inspiration to realize some part of my script.

## Contribute

This project for now is very basic and it could be improved if you have edit suggestion or you want to contribute I'll be happy to work together at it.
