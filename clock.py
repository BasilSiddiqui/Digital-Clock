"""
  F27SQ - Coursework 3 - Task 1

  @author: [Basil Rehan Siddiqui]
  @userid: [H00435828]
  @campus: Dubai
      
  This is GUI program to display a digital clock that updates every second 
  using the system time.
 
"""

import tkinter as tk
import datetime as dt #Importing the 2 libraries that I will use in the following code

class DigitalClock: #Creating a class to work on

    def __init__(self, main): #Initialising main 
        self.main = main
        self.main.title("Digital Clock")

        self.clock_frame = tk.Frame(main, bg="white", width=300, height=200) #To contain the elements
        self.clock_frame.pack(pady=50) 

        self.am_pm = tk.Label(self.clock_frame, text="", fg="indigo", bg="white", font=("Helvetica", 28))
        self.am_pm.place(relx=0.55, rely=0.78, anchor="e") #To differentiate between AM & PM

        self.day_label = tk.Label(self.clock_frame, text="", fg="indigo", bg="white", font=("Helvetica", 18))
        self.day_label.place(relx=0.265, rely=0.295, anchor="w") #Additional code to put the date on top

        self.time_label = tk.Label(self.clock_frame, text="00:00:00", fg="violet", bg="white", font=("Times", 36, "italic"))
        self.time_label.place(relx=0.15, rely=0.51, anchor="w") #The main clock with hours:minutes:seconds format

        self.frame1 = tk.Frame(self.clock_frame, bg="navyblue", width=4, height=54)
        self.frame1.place(relx=0.35, rely=0.52, anchor="center")

        self.frame2 = tk.Frame(self.clock_frame, bg="navyblue", width=4, height=54)
        self.frame2.place(relx=0.55, rely=0.52, anchor="center")
        
        self.frame3 = tk.Frame(self.clock_frame, bg="navyblue", width=4, height=145)
        self.frame3.place(relx=0.15, rely=0.565, anchor="center")
        
        self.frame4 = tk.Frame(self.clock_frame, bg="navyblue", width=4, height=145)
        self.frame4.place(relx=0.75, rely=0.565, anchor="center")
        
        self.frame5 = tk.Frame(self.clock_frame, bg="navyblue", width=180, height=4)
        self.frame5.place(relx=0.45, rely=0.65, anchor="center")
        
        self.frame6 = tk.Frame(self.clock_frame, bg="navyblue", width=180, height=4)
        self.frame6.place(relx=0.45, rely=0.92, anchor="center")
        
        self.frame7 = tk.Frame(self.clock_frame, bg="navyblue", width=180, height=4)
        self.frame7.place(relx=0.45, rely=0.38, anchor="center")
        
        self.frame8 = tk.Frame(self.clock_frame, bg="navyblue", width=180, height=4)
        self.frame8.place(relx=0.45, rely=0.215, anchor="center")
            
        #All the frames to make the clock look good and easy to read^^^
        
        self.update_time() #To update the time

    def update_time(self):
        
        t = dt.datetime.now()
        time_str = t.strftime("%H %M %S") #Keeping the format as mentioned above too
        self.time_label.config(text=time_str)
        day_of_month = t.strftime("%D") #Simple one word format for the date
        self.day_label.config(text=day_of_month) 

        if t.hour >= 12:                  #After 12, 
            self.am_pm.config(text="PM")  #the am/pm label changes to PM
        else:
            self.am_pm.config(text="AM")  #or else its AM

        self.main.after(1000, self.update_time) #To make it update every second (1000 milleseconds = 1 second)

if __name__ == "__main__": #To start the clock
    main = tk.Tk()
    clock = DigitalClock(main)
    main.mainloop()