# coding: utf-8

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ScatterCreator3D():
    def __init__(self, parent, figure_num):
        self.fig  = plt.figure()
        self.axes = self.fig.add_subplot(111, projection='3d')
        self.parent         = parent
        self.data_list      = []
        self.data_name_list = []
        self.color_list     = []
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.figure_num     = figure_num
        self.axes.grid(True)
        plt.pause(0.00001)
    
    def on_click(self, event):
        if event.button == 3:
            # set axis equal or not
            if self.parent.equal_list_cmbbox.get() == 'ON':
                self.axes.axis('equal')
            # no data is selected
            if not self.parent.x_data_box.get() and \
                not self.parent.y_data_box.get() and \
                not self.parent.z_data_box.get() and \
                not self.parent.c_data_box.get():
                self.parent.status_bar_str.set('Select data from Data List')
            # x-y-z scatter
            elif self.parent.x_data_box.get() and \
                self.parent.y_data_box.get() and \
                self.parent.z_data_box.get() and \
                not self.parent.c_data_box.get():
                self.create_x_y_z_scatter()
            # x-y-z heatmap
            elif self.parent.x_data_box.get() and \
                self.parent.y_data_box.get() and \
                self.parent.z_data_box.get() and \
                self.parent.c_data_box.get():
                self.create_x_y_z_heatmap()
            else:
                self.parent.status_bar_str.set('Select data from Data List')
    
    def create_x_y_z_scatter(self):
        x_group_data_name = self.parent.x_data_box.get().split(',')
        x_group_name = x_group_data_name[0]
        x_data_name = x_group_data_name[1]
        x_data = self.parent.dict_data_frame[x_group_name][x_data_name]
        y_group_data_name = self.parent.y_data_box.get().split(',')
        y_group_name = y_group_data_name[0]
        y_data_name = y_group_data_name[1]
        y_data = self.parent.dict_data_frame[y_group_name][y_data_name]
        z_group_data_name = self.parent.z_data_box.get().split(',')
        z_group_name = z_group_data_name[0]
        z_data_name = z_group_data_name[1]
        z_data = self.parent.dict_data_frame[z_group_name][z_data_name]
        color = self.parent.color_list_cmbbox.get()
        self.axes.scatter(x_data, y_data, z_data, c=color, marker='.', s=30)
        plt.pause(0.00001)
    
    def create_x_y_z_heatmap(self):
        x_group_data_name = self.parent.x_data_box.get().split(',')
        x_group_name = x_group_data_name[0]
        x_data_name = x_group_data_name[1]
        x_data = self.parent.dict_data_frame[x_group_name][x_data_name]
        y_group_data_name = self.parent.y_data_box.get().split(',')
        y_group_name = y_group_data_name[0]
        y_data_name = y_group_data_name[1]
        y_data = self.parent.dict_data_frame[y_group_name][y_data_name]
        z_group_data_name = self.parent.z_data_box.get().split(',')
        z_group_name = z_group_data_name[0]
        z_data_name = z_group_data_name[1]
        z_data = self.parent.dict_data_frame[z_group_name][z_data_name]
        c_group_data_name = self.parent.c_data_box.get().split(',')
        c_group_name = c_group_data_name[0]
        c_data_name = c_group_data_name[1]
        c_data = self.parent.dict_data_frame[c_group_name][c_data_name]
        c_min = self.parent.cmin_box.get()
        c_max = self.parent.cmax_box.get()
        if c_min and c_max:
            vmin = round(float(c_min), 1)
            vmax = round(float(c_max), 1)
            sc = self.axes.scatter(x_data, y_data, z_data, c=c_data, vmin=vmin, 
                                   vmax=vmax, cmap='jet', marker='.', s=30)
        else:
            sc = self.axes.scatter(x_data, y_data, z_data, c=c_data, cmap='jet', marker='.', s=30)
        plt.colorbar(sc)
        plt.pause(0.00001)