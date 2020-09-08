"""
    Author : Anshul Agrawal
"""
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import Progressbar
from pytube import YouTube

def clickDownload():
    if(getURL.get() == ""):
        messagebox.showinfo("ERROR", "ENTER url ")
        return
    elif (getLoc.get() == ""):
        messagebox.showinfo("ERROR", "ENTER LOCATION ")
        return

    select = listbox.curselection()
    quality = videos[select[0]]
    global file_size
    file_size = quality.filesize
    location = getLoc.get()
    quality.download(location)
    messagebox.showinfo("Downloading Finish", yt.title+" has been downloaded Sucessfully!!!")

def setURL():
    #Get URL of the Video
    url = getURL.get()
    print(url)

    #Create Object to hold the URL
    global yt
    try:
        yt = YouTube(url, on_progress_callback=progressCheck)
        print(yt.title)
    except:
        messagebox.showinfo("Error in pytube! Try updating pytube.")

    # Get the Quality of the Videos and store in the 'videos' variable
    global videos
    videos = yt.streams.filter(mime_type='video/mp4', progressive=True).desc()
    #Get Quality and display as list in the Listbox

    for v in videos:
        listbox.insert(END, "Resolution: "+str(v.resolution)+"    FPS: "+str(v.fps)+"\n\n")

def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def clickReset():
    getURL.set("")
    getLoc.set("")
    progress["value"] = 0
    listbox.delete(0,END)

def progressCheck(stream=None, chunk=None, remaining=None):
    percent = (100*(file_size-remaining))/file_size
    progress["value"] = percent
    root.update_idletasks()

# Root Object
root = Tk()

# Title
root.title("YouTube Video Dowloader")

# Size of window
root.geometry("900x375")

# Window not Resizeable
root.resizable(False, False)

# Labels
headLabel       = Label(root, text="YOUTUBE VIDEO DOWNLOADER", font=("Century Gothic",25)).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root, text="URL",                      font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(root, text="SELECT QUALITY",           font=("Century Gothic",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(root, text="LOCATION",                 font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)
progressLabel   = Label(root, text="Progress",                 font=("Century Gothic",15)).grid(row=5, column=0, padx=10, pady=10)

# Input
getURL = StringVar()
getLoc = StringVar()

# Entry
urlEntry    = Entry(root, font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root, font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

# List box for video Quality
listbox     = Listbox(root, font=("Century Gothic",11), width = 56, height = 5, bd=3, relief=SOLID, borderwidth=1)
listbox.grid(row=2,column=1, padx=10, pady=10)

# Buttons
urlButton       = Button(root, text = "SET URL",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(root, text = "BROWSE",    font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(root, text = "DOWNLOAD",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickDownload).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(root, text = "CLEAR ALL", font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=4, column=2, padx=10, pady=10)

progress = Progressbar(root, orient = HORIZONTAL, length = 450, mode = 'determinate')
progress.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
