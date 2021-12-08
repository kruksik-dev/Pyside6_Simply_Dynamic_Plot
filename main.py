import random
import sys
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton, QWidget
from PySide6.QtCharts import QChartView, QLineSeries, QChart,QValueAxis,QDateTimeAxis
from view import *




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newbtn = QPushButton("Siema")
        self.plotting  = Widget_plot()
        self.ui.plotlayout.addWidget(self.plotting.chart_view)
        self.ui.plot1btn.clicked.connect(self.runthread)
        

        
        self.show()
        
        
    def runthread(self):
        self.worker = ThreadUpdate()
        self.worker.start()
        self.worker.values.connect(self.plotting.plot_data)
        
    def closeEvent(self,event):
        self.worker.stop()
        result = QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QMessageBox.Yes| QMessageBox.No)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()


    
        


class Widget_plot(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.create_chart()
        self.create_series()
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.firsttime = 0
    
  
        self.max_xrange = QDateTime.currentDateTime() 
        self.min_xrange = 0
        self.max_yrange = 0
        self.min_yrange = 0
        
   
        
        
        

    def create_chart(self):
       
        self.chart = QChart()
        self.chart.setAnimationOptions(QChart.AllAnimations)
        self.chart.setBackgroundVisible(False)
        self.chart.legend().setAlignment(Qt.AlignLeft)
        self.chart.createDefaultAxes()
        
        self.axis_x = QDateTimeAxis()
        self.axis_x.setFormat("dd.MM h:mm:ss")
        self.axis_x.setLabelsAngle(70)
        self.axis_x.setTickCount(15)
        self.axis_x.setTitleText("X data")
        self.axis_x.setMax(QDateTime.currentDateTime().addSecs(10))
        self.axis_x.setMin(QDateTime.currentDateTime())
     
        
        self.axis_y = QValueAxis()
        self.axis_y.setTickCount(15)
        self.axis_y.setTitleText("Y data")
        self.axis_y.setMax(10)
        self.axis_y.setMin(0)
        
        
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        
    
    def create_series(self):
        self.series = QLineSeries()
        self.series.setName("Series 1 plotting")
        self.series.setPointsVisible(True)
        self.series.setMarkerSize(4)
 
        self.chart.addSeries(self.series)

        self.series.attachAxis(self.axis_y)
        self.series.attachAxis(self.axis_x)

    def rescale_x_axis(self,down_time,up_time):
        self.axis_x.setMax(QDateTime.currentDateTime().addSecs(up_time))
        self.axis_x.setMin(QDateTime.currentDateTime().addSecs(down_time))
        
        
        
    @Slot()
    def plot_data(self,values):
        x = QDateTime.currentDateTime()
        self.series.append(float(x.toMSecsSinceEpoch()),float(values))
        self.resize_axis(x,values)
    
    def resize_axis(self,x,y):
        if x > self.max_xrange:
            if not self.firsttime: self.rescale_x_axis(-2,30) 
            t_m, t_M = min(x, self.axis_x.min()), max(x, self.axis_x.max())
            self.max_xrange = t_M.addSecs(5)
            if self.firsttime > 5:
                self.min_xrange = t_m.addSecs(5)
            else:
                self.min_xrange = t_m
                
        if y > self.max_yrange:
            M = max(y, self.axis_y.max())
            print(f'MAX: {y} {self.max_yrange}')
            self.max_yrange = M + 0.3*M
            
        elif y < self.min_yrange:
            print(f'MIN: {y} {self.min_yrange}')
            m = min(y, self.axis_y.min())
            self.min_yrange = m + 0.3*m
            
        self.axis_x.setRange(self.min_xrange,self.max_xrange)
        self.axis_y.setRange(self.min_yrange ,self.max_yrange)
        self.firsttime += 1
        
     

        
  
class ThreadUpdate(QThread):
    values = Signal(int)
    
    def __init__(self):
        super().__init__()
        self.run_status = True
        
    def run(self):
        while self.run_status:
            self.values.emit(random.randint(-25,50))
            for _ in range(1):
                if self.run_status:
                    self.sleep(1)
                else:
                    break
    
    def stop(self):
        self.run_status = False                
        
               
        
       
  
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())