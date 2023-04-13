import customtkinter as ctk
import pytube, pywhatkit, os
from tkinter import messagebox

class Download_Youtube_UI():
    def __init__(self):
        self.master = ctk.CTk()
        self.master.geometry("360x300")
        self.master.resizable(False, False)
        self.master.title("Youtube Downloader")
        self.master.iconbitmap("IMG\\ytico.ico")
        self.frame1 = ctk.CTkFrame(self.master, width= 360, height= 320)
        self.frame1.pack()
        self.frame1.pack_propagate(False)
        self.entry1 = ctk.CTkEntry(self.frame1, width= 360, height= 30, font= ("Roboto", 16), placeholder_text= "Please input your url of video here")
        self.entry1.pack()
        self.entry1.place(x = 0, y = 30)
        
        self.entry2 = ctk.CTkEntry(self.frame1, width= 360, height= 30, font= ("Roboto", 16), placeholder_text= "Please input your path you want to download")
        self.entry2.pack()
        self.entry2.place(x = 0, y = 80)
        
        checkboxVariable = ctk.IntVar()
        checkboxVariable.set(0)
        def download():
            url = self.entry1.get()
            video = pytube.YouTube(url)
            if self.entry2.get() == "":
                messagebox.showerror("Error", "Please enter your path you want to download in to the second box")
            else:
                if checkboxVariable.get() == 1:
                    streams = video.streams.get_audio_only().download(self.entry2.get())
                    new_file = os.path.splitext(streams)
                    os.rename(streams, new_file[0] + " Audio File.mp3")
                    messagebox.showinfo("Notify", "Your file is download completely")
                else:
                    video.streams.get_highest_resolution().download(self.entry2.get())
                    messagebox.showinfo("Notify", "Your file is download completely")
                
            
        self.button1 = ctk.CTkButton(self.frame1, width= 200, height= 30, text= "Download now", font= ("Roboto", 32), command= download)
        self.button1.pack()
        self.button1.place(x = 50, y = 120)
        
        self.CB1 = ctk.CTkCheckBox(self.frame1, text= "Mp3", variable= checkboxVariable)
        self.CB1.pack()
        self.CB1.place(x = 0, y = 170)
        
        
    def run(self):
        self.master.mainloop()
        
if __name__ == "__main__":
    Gui = Download_Youtube_UI()
    Gui.run()