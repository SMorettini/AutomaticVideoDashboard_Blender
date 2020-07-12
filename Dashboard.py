
######################VARIABLE TO SET####################################

KEY_COLUMN_LINE_CHART=['accelerometer_x','accelerometer_y']  #List all the column name that correspond to a line chart
MAKE_LINE_GRAPH=False #Put a True to make the line chart, remember it can be slow and it WILL DELETE THE LINE CHART ALREADY IN THE SCENE WITH THE SAME NAME
current_folder='/home/**/**/**/workspace/Dashboard/' #Folder of this file and of the data.csv
########################################################################

packages_path=current_folder+'venv/lib/python3.7/site-packages'
path_of_data=current_folder+"data.csv"

import bpy
import sys

sys.path.append(packages_path)
sys.path.append(current_folder)

import pandas as pd
from lineChart import LineChart


class Dashboard(object):
    x_acc=2
    y_acc=3

    def __init__(self):
        bpy.app.handlers.frame_change_pre.clear()

    def load_csv(self, path):
        self.df=pd.read_table(path, delimiter=",")
        #create dictionary for text {label:[values]}
        return

    def make_line_graph(self):
        lineCreator=LineChart()
        sizes=(0.03,0.03,0.03)
        for k in KEY_COLUMN_LINE_CHART:
            if(k in self.df.keys()):
                lineCreator.plotdata(self.x_acc,self.y_acc,-4, -1, 0, 4, 0, self.df[k], k, sizes)
        return


    def recalculate_text(self,scene):
        scene = bpy.context.scene
        keys=self.df.keys()
        text_keys = [s for s in keys if "text_" in s]
        for k in text_keys:
            obj = scene.objects[k]
            if(scene.frame_current>=0 and len(self.df[k])>scene.frame_current):
                obj.data.body = self.df[k][scene.frame_current]

    def make_text_update(self):
        bpy.app.handlers.frame_change_pre.append(self.recalculate_text)
        return

    def recalculate_notification(self,scene):
        scene = bpy.context.scene
        keys=self.df.keys()
        not_keys = [s for s in keys if "not_" in s]
        for k in not_keys:
            obj_off = scene.objects[k]
            obj = scene.objects[k+"_off"]
            if(scene.frame_current>=0 and len(self.df[k])>scene.frame_current):
                obj.hide_render = self.df[k][scene.frame_current]#obj.hide_render = ("TRUE"==str(self.df[k][scene.frame_current]).upper())
                obj.hide_viewport = self.df[k][scene.frame_current]#obj.hide_viewport = ("TRUE"==str(self.df[k][scene.frame_current]).upper())
                obj_off.hide_render = not self.df[k][scene.frame_current]
                obj_off.hide_viewport = not self.df[k][scene.frame_current]

    def make_notification_update(self):
        bpy.app.handlers.frame_change_pre.append(self.recalculate_notification)
        return


dashboard=Dashboard()
dashboard.load_csv(path_of_data)
if(MAKE_LINE_GRAPH):
    dashboard.make_line_graph()
dashboard.make_text_update()
dashboard.make_notification_update()
print("Finish")
