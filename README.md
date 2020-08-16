# CsvDataAnalyzer
A CSV file data analyzer using pure Python.  

## Table of contents

## About this repository
This is a CSV file data analyzer based on Python.  

Features:  

1. Easy to use.  
2. Statistics(Sum, Mean, Std, Max and Min) of each data are calculated automatically.  
3. It can create multiple 2/3D graph.  

## Gallery
* Launched on Windows 10
![](img/gallery.PNG)

## Requirements
* Python 3.6.x or higher
* matplotlib
* mpl_toolkits
* numpy
* seaborn
* pandas
* tkinter

## Getting Started
1. Clone this repository.
2. Install required libraries.
3. Execute the following command and a GUI will be opened.
```shell script
$ python src/CsvDataAnalyzer.py
```
![](img/GUI.PNG)

## How to use

### Reading CSV file
* "Files" at left top of GUI -> "Read csv file"  
![](img/Files_Read_CSV.PNG)  

* A file dialog will be oped.  
* Multiple CSV files can be selected too.
![](img/FileDialog.PNG)  

* Reading will finish like this.  
![](img/FinishedReading.PNG)

### Calculating Statics
* Max, Min, Mean and Sigma(Std) will be calculated automatically.  
* Those values are displayed on GUI.  
![](img/Statistics.PNG)

### Creating Graph
* Select data you want to analyze on GUI.  
* Selected data is colored blue by left click.  
![](img/SelectData.PNG)

* Set data to X axis by pushing "X Data Set".  
![](img/XDataSet.PNG)

* Set another data to Y axis by pushing "Y Data Set".  
![](img/YDataSet.PNG)

* Select plot color from pull-down menu.  
![](img/PlotColor.PNG)

### 2D Line Graph
* After setting data, select "Create 2D Line" from "Figures" menu.  
![](img/Create2DLine.PNG)  

* A empty figure will be opened.  
![](img/EmptyFigure.PNG)

* On the figure, click the right button. -> The 2D line graph will be shown.  
![](img/2DLineGraph.PNG)

* Another data can be shown on the same figure.  
![](img/2DLineGraphMulti.PNG)

### 2D Scatter Graph
* After setting data, select "Create 2D Scatter" from "Figures" menu.  
![](img/Create2DScatter.PNG)  

* By following the above procedure, the 2D scatter graph will be shown.  
![](img/2DScatterGraph.PNG)  

* By setting a color data to "C Data Set", a heatmap can be created.  
![](img/CDataSet.PNG)  

![](img/2DHeatMap.PNG)

* You can set min/max velues of color bar.  
![](img/CMinMax.PNG)

![](img/2DColoredHeatMap.PNG)

### 3D Line Graph
* After setting data, select "Create 3D Line" from "Figures" menu.  
![](img/Create3DLine.PNG)  

* Set another data to "Z Data Set".  
![](img/ZDataSet.PNG)

* By following the above procedure, a 3D line graph will be shown.  
![](img/3DLineGraph.PNG)

### 3D Scatter Graph
* After setting data, select "Create 3D Scatter" from "Figures" menu.  
![](img/Create3DScatter.PNG)  

* By following the above procedure, a 3D scatter graph will be shown.  
![](img/3DScatterGraph.PNG)  

* 3D heatmap can be created too.  
![](img/3DHeatMap.PNG)

### Histogram
* After setting data, select "Create 3D Histgram" from "Figures" menu.  
![](img/CreateHistogram.PNG)  

* This histogram shows X data distribution.  
![](img/Histogram.PNG)  

### Axis Equal
* You can switch ON/OFF from a pull-down menu "Axis Equal"".  
![](img/AxisEqual.PNG)  

### Kernel Density Estimation
* When a histogram graph is created, you can show a kernel density function together.  
![](img/HistogramKde.PNG)  

* You can switch ON/OFF from a pull-down menu "Hist KDE".  
![](img/HistKde.PNG)  

## License
MIT

## Author
* [Shisato Yano](https://github.com/ShisatoYano)([@4310sy](https://twitter.com/4310sy))
