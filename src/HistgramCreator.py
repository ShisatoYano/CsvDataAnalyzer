# coding: utf-8

import matplotlib.pyplot as plt
import seaborn as sns

class HistgramCreator():
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
            if not self.parent.x_data_box.get():
                self.parent.status_bar_str.set('Select data from Data List')
            else:
                self.create_histgram()
    
    def create_histgram(self):
        x_group_data_name = self.parent.x_data_box.get().split(',')
        x_group_name = x_group_data_name[0]
        x_data_name = x_group_data_name[1]
        x_data = self.parent.dict_data_frame[x_group_name][x_data_name]
        color = self.parent.color_list_cmbbox.get()
        if self.parent.hist_kde_list_cmbbox.get() == 'OFF':
            is_kde_enable = False
        else:
            is_kde_enable = True
        self.axes = sns.distplot(x_data, color=color, kde=is_kde_enable)
        plt.pause(0.00001)