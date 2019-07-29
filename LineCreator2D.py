# coding: utf-8

import matplotlib.pyplot as plt

class LineCreator2D():
    def __init__(self, parent, figure_num):
        self.fig, self.axes = plt.subplots()
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
                not self.parent.c_data_box.get():
                self.parent.status_bar_str.set('Select data from Data List')
            # x-y line
            elif self.parent.x_data_box.get() and \
                self.parent.y_data_box.get():
                self.create_x_y_line()
            else:
                self.parent.status_bar_str.set('Select data from Data List')
    
    def create_x_y_line(self):
        x_group_data_name = self.parent.x_data_box.get().split(',')
        x_group_name = x_group_data_name[0]
        x_data_name = x_group_data_name[1]
        x_data = self.parent.dict_data_frame[x_group_name][x_data_name]
        y_group_data_name = self.parent.y_data_box.get().split(',')
        y_group_name = y_group_data_name[0]
        y_data_name = y_group_data_name[1]
        y_data = self.parent.dict_data_frame[y_group_name][y_data_name]
        color = self.parent.color_list_cmbbox.get()
        self.axes.plot(x_data, y_data, c=color, linestyle='solid', linewidth=3)
        plt.pause(0.00001)