import wx
import shutil
from datetime import timedelta, datetime
from os import path
import os


#File locations
src = {'label':'Folder A', 'path':'C:\Users\court\Desktop\Folder A'}
dest = {'label':'Folder B', 'path':'C:\Users\court\Desktop\Folder B'}

#Setting the time now to the deadline time of 24 hours from now
now = datetime.now()
deadline = now + timedelta(hours=-24)

def main():
        #generating the file names from Folder A
        for root, dir, files in os.walk(src['path']):
            #looping through each file to retrieve the time stamp and pathname
            for file in files:
                pathname = os.path.join(root, file)
                modified_time = datetime.fromtimestamp(os.path.getmtime(pathname))
                #comparing modification time from deadline and moving if appropriate
                if now >= modified_time >= deadline:
                    print 'modified within 24 hours: ' + pathname
                    shutil.move(pathname, dest['path'])

class fileWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,200))
        #creating panel with text and buttons
        panel = wx.Panel(self)
        originText = wx.StaticText(panel, -1, "Origin Location",(55,30))
        destinationText = wx.StaticText(panel, -1, "Destination Location",(235,30))

        origin = wx.ComboBox(panel, choices=[src['label'], dest['label']],
                             style=wx.CB_DROPDOWN, pos=(60,50))
        destination = wx.ComboBox(panel, choices=[src['label'], dest['label']],
                             style=wx.CB_DROPDOWN, pos=(250,50))
        transferButton = wx.Button(panel, wx.ID_ANY, label='Transfer',
                                   pos=(150,100))
        #referencing event for transfer
        self.Bind(wx.EVT_BUTTON, self.transferButtonClicked, transferButton)
        
        #initial pop up box
        popupQuestion = wx.MessageDialog(None, 'Would you like to check for a file \
modification within the last 24 hours?', 'Transfer', wx.YES_NO)
        popupAnswer = popupQuestion.ShowModal()
        popupQuestion.Destroy()
        
        if popupAnswer == wx.ID_NO:
            self.Close()

        #showing panel/frame
        self.Center()
        self.Show(True)

    #event defined for transfer
    def transferButtonClicked(self, event):
        main()
        popupComplete = wx.MessageDialog(None, 'Transfer Completed!', 'Transfer', wx.OK)
        popupDone = popupComplete.ShowModal()
        popupComplete.Destroy()
        self.Destroy()
            

if __name__ == '__main__':
    app = wx.App(False)
    frame = fileWindow(None, 'Transfer Files')
    
    app.MainLoop()
    

        
