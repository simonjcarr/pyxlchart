from win32com.client import Dispatch
import os
import pythoncom
pythoncom.CoInitialize


class Pyxlchart(object):
    """
    This class exports charts in an Excel Spreadsheet to the FileSystem
    win32com libraries are required.
    """
    

    def __init__(self):
        self.WorkbookDirectory = ''
        self.WorkbookFilename = ''
        self.GetAllWorkbooks = False
        self.SheetName = ''
        self.ChartName = ''
        self.GetAllWorkbookCharts = False
        self.GetAllWorksheetCharts = False
        self.ExportPath = ''
        self.ImageFilename = ''
        self.ReplaceWhiteSpaceChar = '_'
        self.ImageType = 'jpg'

    def start_export(self):
        if self.WorkbookDirectory == '':
            return "WorkbookDirectory not set"
        else:
            self._export()    

    def _export(self):
        """
        Exports Charts as determined by the settings in class variabels.
        """
        excel = Dispatch("excel.application")
        excel.Visible = False
        wb = excel.Workbooks.Open(os.path.join(self.WorkbookDirectory ,self.WorkbookFilename))
        for sht in wb.WorkSheets:
            for cht in sht.ChartObjects():
                imagename = self._get_filename(cht.Name)
                savepath = os.path.join(self.ExportPath,imagename)
                print savepath
                cht.Chart.Export(savepath,self.ImageType)
        wb.Close(False)
        excel.Quit()

    

    def _get_filename(self,chartname):
        """
        Replaces white space in self.WorkbookFileName with the value given in self.ReplaceWhiteSpaceChar
        If self.ReplaceWhiteSpaceChar is an empty string then self.WorkBookFileName is left as is
        """
        if self.ImageFilename == '':
            self.ImageFilename == chartname

        if self.ReplaceWhiteSpaceChar != '':
            chartname.replace(' ',self.ReplaceWhiteSpaceChar)

        if self.ImageFilename != "":
            return self.ImageFilename + "_" + chartname + "." + self.ImageType
        else:
            return chartname + '.' + self.ImageType

    
        

if __name__ == "__main__":
    xl = Pyxlchart()
    xl.WorkbookDirectory = "C:\\Users\\Simon\\Documents\\pychart"
    xl.WorkbookFilename = "testworkbook.xls"
    xl.SheetName = "Sheet1"
    xl.ImageFilename = "MyChart1"
    xl.ExportPath = "C:\\Users\\Simon\\Documents\\pychart"
    xl.start_export()
    print "This file does not currently allow direct access"
    print "Please import PyXLChart and run start_export()"
    
