# coding: utf-8

"""
CsvDataAnalyzer

GUI python tool for analyzing csv data.

Author: Shisato Yano
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import matplotlib.markers as mkr
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
import ScatterCreator2D as sc2d
import LineCreator2D as l2d
import ScatterCreator3D as sc3d
import HistgramCreator as hist

class CsvDataAnalyzer(ttk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title('CsvDataAnalyzer')
        self.color_list      = clr.cnames
        self.marker_list     = mkr.MarkerStyle().markers
        self.equal_list      = ['OFF', 'ON']
        self.hist_kde_list   = ['OFF', 'ON']
        self.dict_data_frame = {}
        self.selected_data   = []
        self.created_figure  = []
        self.init_menu()
        self.init_combo_box()
        self.init_status_bar()
        self.init_data_list()
        self.init_data_set_button()
        self.init_entry_box()
    
    def init_combo_box(self):
        # plot color pattern
        self.color_list_label = tk.Label(text='Plot Color')
        self.color_list_label.pack(side=tk.LEFT, padx=25)
        self.color_list_cmbbox = ttk.Combobox(self.root, state='readonly', justify='center', width=12)
        self.color_list_cmbbox['values'] = list(self.color_list.keys())
        self.color_list_cmbbox.current(0)
        self.color_list_cmbbox.place(x=10, y=150)
        # plot marker pattern
        self.marker_list_label = tk.Label(text='Plot Marker')
        self.marker_list_label.pack(side=tk.LEFT, padx=25)
        self.marker_list_cmbbox = ttk.Combobox(self.root, state='readonly', justify='center', width=12)
        self.marker_list_cmbbox['values'] = list(self.marker_list.keys())
        self.marker_list_cmbbox.current(0)
        self.marker_list_cmbbox.place(x=120, y=150)
        # axis equal ON/OFF
        self.equal_list_label = tk.Label(text='Axis Equal')
        self.equal_list_label.place(x=25, y=230)
        self.equal_list_cmbbox = ttk.Combobox(self.root, state='readonly', justify='center', width=12)
        self.equal_list_cmbbox['values'] = self.equal_list
        self.equal_list_cmbbox.current(0)
        self.equal_list_cmbbox.place(x=10, y=250)
        # kde(gaussian kernel density estimate) ON/OFF
        self.hist_kde_list_label = tk.Label(text='Hist KDE')
        self.hist_kde_list_label.place(x=130, y=230)
        self.hist_kde_list_cmbbox = ttk.Combobox(self.root, state='readonly', justify='center', width=12)
        self.hist_kde_list_cmbbox['values'] = self.hist_kde_list
        self.hist_kde_list_cmbbox.current(0)
        self.hist_kde_list_cmbbox.place(x=120, y=250)
    
    def init_entry_box(self):
        # cmin set
        self.cmin_label = tk.Label(text='C Min')
        self.cmin_label.place(x=25, y=180)
        self.cmin_box = tk.Entry(width=15, justify='center')
        self.cmin_box.place(x=10, y=200)
        # cmax set
        self.cmax_label = tk.Label(text='C Max')
        self.cmax_label.place(x=130, y=180)
        self.cmax_box = tk.Entry(width=15, justify='center')
        self.cmax_box.place(x=120, y=200)
    
    def init_data_set_button(self):
        # x data set
        self.x_data_button = tk.Button(text='X Data Set', command=self.click_x_set_button)
        self.x_data_button.place(x=10, y=5)
        self.x_data_box = tk.Entry(width=22, justify='left')
        self.x_data_box.place(x=80, y=8)
        # y data set
        self.y_data_button = tk.Button(text='Y Data Set', command=self.click_y_set_button)
        self.y_data_button.place(x=10, y=35)
        self.y_data_box = tk.Entry(width=22, justify='left')
        self.y_data_box.place(x=80, y=38)
        # z data set
        self.z_data_button = tk.Button(text='Z Data Set', command=self.click_z_set_button)
        self.z_data_button.place(x=10, y=65)
        self.z_data_box = tk.Entry(width=22, justify='left')
        self.z_data_box.place(x=80, y=68)
        # color data set
        self.c_data_button = tk.Button(text='C Data Set', command=self.click_c_set_button)
        self.c_data_button.place(x=10, y=95)
        self.c_data_box = tk.Entry(width=22, justify='left')
        self.c_data_box.place(x=80, y=98)
    
    def click_x_set_button(self):
        self.x_data_box.delete(0, tk.END)
        if not self.selected_data:
            self.status_bar_str.set('Select data from Data List')
            return
        group_data_name_str = ','.join(self.selected_data[-1])
        self.x_data_box.insert(tk.END, group_data_name_str)
    
    def click_y_set_button(self):
        self.y_data_box.delete(0, tk.END)
        if not self.selected_data:
            self.status_bar_str.set('Select data from Data List')
            return
        group_data_name_str = ','.join(self.selected_data[-1])
        self.y_data_box.insert(tk.END, group_data_name_str)
    
    def click_z_set_button(self):
        self.z_data_box.delete(0, tk.END)
        if not self.selected_data:
            self.status_bar_str.set('Select data from Data List')
            return
        group_data_name_str = ','.join(self.selected_data[-1])
        self.z_data_box.insert(tk.END, group_data_name_str)
    
    def click_c_set_button(self):
        self.c_data_box.delete(0, tk.END)
        if not self.selected_data:
            self.status_bar_str.set('Select data from Data List')
            return
        group_data_name_str = ','.join(self.selected_data[-1])
        self.c_data_box.insert(tk.END, group_data_name_str)

    def init_status_bar(self):
        self.status_bar_str = tk.StringVar()
        self.status_bar = tk.Label(self.root,
                                   textvariable=self.status_bar_str,
                                   bd=1, relief=tk.SUNKEN,
                                   anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_bar_str.set('')
    
    def init_data_list(self):
        self.data_list_label = tk.Label(text='Data List')
        self.data_list_label.pack()
        container = ttk.Frame()
        container.pack(fill=tk.BOTH, expand=True)
        data_header = ['Data group', 'Data name', 'Max', 'Min', 'Mean', 'Sigma']
        self.data_list = ttk.Treeview(columns=data_header, show='headings')
        self.data_list.column(2, width=100)
        self.data_list.column(3, width=100)
        self.data_list.column(4, width=100)
        self.data_list.column(5, width=100)
        v_scrollbar = ttk.Scrollbar(orient='vertical', command=self.data_list.yview)
        h_scrollbar = ttk.Scrollbar(orient='horizontal', command=self.data_list.xview)
        self.data_list.configure(xscrollcommand=h_scrollbar.set,
                                 yscrollcommand=v_scrollbar.set)
        self.data_list.grid(column=0, row=0, sticky='nsew', in_=container)
        v_scrollbar.grid(column=1, row=0, sticky='ns', in_=container)
        h_scrollbar.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=3)
        container.grid_rowconfigure(0, weight=1)
        for column in data_header:
            self.data_list.heading(column, text=column.title())
    
    def init_menu(self):
        # file menu
        self.menu = tk.Menu(self.root)
        file_menu = tk.Menu(self.menu, tearoff=0)
        # read csv menu
        file_menu.add_command(label='Read csv file', command=self.read_csv_file)
        self.menu.add_cascade(label='Files', menu=file_menu)
        self.root.config(menu=self.menu)
        # figure menu
        figure_menu = tk.Menu(self.menu, tearoff=0)
        # scatter 2D
        figure_menu.add_command(label='Create 2D Scatter', command=self.create_2d_scatter)
        # line 2D
        figure_menu.add_command(label='Create 2D Line', command=self.create_2d_line)
        # scatter 3D
        figure_menu.add_command(label='Create 3D Scatter', command=self.create_3d_scatter)
        # histgram
        figure_menu.add_command(label='Create Histgram', command=self.create_histgram)
        self.menu.add_cascade(label='Figures', menu=figure_menu)
        self.root.config(menu=self.menu)
    
    def insert_data_frame(self, df, path):
        group_name = path.split('/')[-1]
        if not self.dict_data_frame.keys():
            self.dict_data_frame[group_name] = df
        else:
            last_group_name = list(self.dict_data_frame.keys())[-1]
            last_df = self.dict_data_frame[last_group_name]
            last_df_columns = last_df.columns.values.tolist()
            add_df_columns  = df.columns.values.tolist()
            if last_df_columns == add_df_columns:
                self.dict_data_frame[last_group_name] = pd.concat([self.dict_data_frame[last_group_name], df])
            else:
                self.dict_data_frame[group_name] = df
    
    def insert_data_list(self):
        for group_name in list(self.dict_data_frame.keys()):
            single_df = self.dict_data_frame[group_name]
            single_df_columns = single_df.columns.values.tolist()
            for column in single_df_columns:
                # calculate max, min, ave and sigma of each value
                data = single_df[column]
                max_value   = round(float(np.max(data)), 2)
                min_value   = round(float(np.min(data)), 2)
                mean_value  = round(float(np.mean(data)), 2)
                sigma_value = round(float(np.std(data)), 2)
                self.data_list.insert('', 'end', values=(group_name, column, max_value, 
                                      min_value, mean_value, sigma_value))
        # binding event
        self.data_list.bind('<<TreeviewSelect>>', self.select_data_from_list)
    
    def select_data_from_list(self, event):
        widget = event.widget
        self.selected_data = []
        for index in widget.selection():
            data_group_name = widget.item(index)['values']
            self.selected_data.append(data_group_name)
        self.status_bar_str.set('')

    def read_csv_file(self):
        self.data_list.delete(*self.data_list.get_children())
        self.status_bar_str.set('')
        self.status_bar_str.set('Reading csv files...')
        fType = [('CSV', '*.csv')]
        csv_file_paths = tkfd.askopenfilenames(title='Select csv files',
                                              filetypes=fType)
        if not csv_file_paths:
            self.status_bar_str.set('Select csv files')
            return
        self.dict_data_frame = {}
        for path in csv_file_paths:
            df = pd.read_csv(path)
            self.insert_data_frame(df, path)
        self.insert_data_list()
        self.status_bar_str.set('Finished!!')
    
    def create_2d_scatter(self):
        figure_num = len(self.created_figure) + 1
        self.created_figure.append(sc2d.ScatterCreator2D(self, figure_num))
    
    def create_2d_line(self):
        figure_num = len(self.created_figure) + 1
        self.created_figure.append(l2d.LineCreator2D(self, figure_num))
    
    def create_3d_scatter(self):
        figure_num = len(self.created_figure) + 1
        self.created_figure.append(sc3d.ScatterCreator3D(self, figure_num))
    
    def create_histgram(self):
        figure_num = len(self.created_figure) + 1
        self.created_figure.append(hist.HistgramCreator(self, figure_num))

def main():
    # create root frame
    root = tk.Tk()

    # main process
    cda = CsvDataAnalyzer(root)
    root.mainloop()

if __name__ == '__main__':
    main()