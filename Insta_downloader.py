#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
import tkinter as tk
import instaloader
import PIL
from PIL import ImageTk, Image
from instaloader import Profile, Post
from tkinter import messagebox
from tkinter import ttk

instance = instaloader.Instaloader()
LARGE_FONT = ("Verdana", 12)

class IGDownloader(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default="3721672-instagram_108066.ico")
        tk.Tk.wm_title(self, "Instagram Downloader")
        
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, ProfPic, Stories, Photo, Highlight):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame(StartPage)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage (tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=
                         '''Welcome To
Instagram Downloader'''
                         , font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        
        img = Image.open("3721672-instagram_108066.ico")
        self.resized_img = ImageTk.PhotoImage(img)
        
        image = tk.Label(self, image=self.resized_img)
        image.image = image
        image.pack()
        
        def accDownload():
            ig = instaloader.Instaloader()
            userlog = entry_user.get()
            pswd = entry_pass.get()
            entry_user.delete(0, 'end')
            entry_pass.delete(0, 'end')
            entry_user.insert(0, 'Enter Username')
            entry_user.config(fg='grey')
            entry_pass.insert(0, '******')
            entry_pass.config(fg='grey')
            ig.login(user=userlog, passwd=pswd)
            acc = entry_acc.get()
            entry_acc.delete(0, 'end')
            entry_acc.insert(0, 'Enter Instagram ID')
            entry_acc.config(fg='grey')
            ig.download_profile(acc)
            entry_acc.delete(0, 'end')
            entry_acc.insert(0, 'Enter Instagram ID')
            entry_acc.config(fg='grey')
            messagebox.showinfo("Status", "Full Profile Downloaded Successfully")
            
        def clear_widget(event):
 
            # will clear out any entry boxes defined below when the user shifts
            # focus to the widgets defined below
            if entry_user == self.focus_get() and entry_user.get() == 'Enter Username':
                entry_user.delete(0, 'end')
                entry_user.config(fg='black')
            elif entry_pass == entry_pass.focus_get() and entry_pass.get() == '******':
                entry_pass.delete(0, 'end')
                entry_pass.config(fg='black')
            elif entry_acc == entry_acc.focus_get() and entry_acc.get() == 'Enter Instagram ID':
                entry_acc.delete(0, 'end')
                entry_acc.config(fg='black')
                
        def repopulate_defaults(event):
            
            # will repopulate the default text previously inside the entry boxes defined below if
            # the user does not put anything in while focused and changes focus to another widget
            
            if entry_user != self.focus_get() and entry_user.get() == '':
                entry_user.insert(0, 'Enter Username')
                entry_user.config(fg='grey')
            elif entry_pass != self.focus_get() and entry_pass.get() == '':
                entry_pass.insert(0, '******')
                entry_pass.config(fg='grey')
            elif entry_acc != self.focus_get() and entry_acc.get() == '':
                entry_acc.insert(0, 'Enter Instagram ID')
                entry_acc.config(fg='grey')
                
        user = tk.Label(self, text="Enter Your Account: ", font=("Arial", 10,))
        user.pack()
        
        entry_user = tk.Entry(self, width=40, fg='grey')
        entry_user.insert(0, 'Enter Username')
        entry_user.bind('<FocusIn>', clear_widget)
        entry_user.bind('<FocusOut>', repopulate_defaults)
        entry_user.pack()
        
        password = tk.Label(self, text="Enter Your Password: ", font=("Arial", 10,))
        password.pack()
        
        entry_pass = tk.Entry(self, width=40, show='*', fg='grey')
        entry_pass.insert(0, '******')
        entry_pass.bind('<FocusIn>', clear_widget)
        entry_pass.bind('<FocusOut>', repopulate_defaults)
        entry_pass.pack()
        
        acc_target = tk.Label(self, text="Enter Instagram ID: ", font=("Arial", 10,))
        acc_target.pack()
        
        entry_acc = tk.Entry(self, width=40, fg='grey')
        entry_acc.insert(0, 'Enter Instagram ID')
        entry_acc.bind('<FocusIn>', clear_widget)
        entry_acc.bind('<FocusOut>', repopulate_defaults)
        entry_acc.pack()
        
        btn_acc = ttk.Button(self, text="Download", command=accDownload, width = 20)
        btn_acc.pack()       
        
        button1 = ttk.Button(self, text="View More >",
                            command=lambda: controller.show_frame(PageOne), width = 20)
        #button1.place(relx=0.5, rely=0.5, anchor='center')
        button1.pack()

class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="What Do You Want To Do?", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        
        button2 = ttk.Button(self, text="Profile Picture Downloader", 
                            command=lambda: controller.show_frame(ProfPic), width = 20)
        button2.pack()
        button3 = ttk.Button(self, text="Stories Downloader", 
                            command=lambda: controller.show_frame(Stories), width = 20)
        button3.pack()
        button4 = ttk.Button(self, text="Photo Video Downloader", 
                            command=lambda: controller.show_frame(Photo), width = 20)
        button4.pack()
        button5 = ttk.Button(self, text="Highlight Downloader", 
                            command=lambda: controller.show_frame(Highlight), width = 20)
        button5.pack()
        button6 = ttk.Button(self, text="Back to Home", 
                            command=lambda: controller.show_frame(StartPage), width = 20)
        button6.pack()
        
class ProfPic(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Profile Picture Downloader", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        
        def imgDownload():
            ig = instaloader.Instaloader()
            profile = entry_target.get()
            entry_target.delete(0, 'end')
            entry_target.insert(0, 'Enter Instagram ID')
            entry_target.config(fg='grey')
            ig.download_profile(profile, profile_pic_only = True)
            messagebox.showinfo("Status", "Image Downloaded Successfully")
           
        def clear_widget1(event):
 
            # will clear out any entry boxes defined below when the user shifts
            # focus to the widgets defined below
            if entry_target == self.focus_get() and entry_target.get() == 'Enter Instagram ID':
                entry_target.delete(0, 'end')
                entry_target.config(fg='black')
                
        def repopulate_defaults1(event):
 
            # will repopulate the default text previously inside the entry boxes defined below if
            # the user does not put anything in while focused and changes focus to another widget
            if entry_target != self.focus_get() and entry_target.get() == '':
                entry_target.insert(0, 'Enter Instagram ID')
                entry_target.config(fg='grey')
                
        Target = tk.Label(self, text="Enter Instagram ID: ", font=("Arial", 10,))
        Target.pack()
        
        entry_target = tk.Entry(self, width=40, fg='grey')
        entry_target.insert(0, 'Enter Instagram ID')
        entry_target.bind('<FocusIn>', clear_widget1)
        entry_target.bind('<FocusOut>', repopulate_defaults1)
        entry_target.pack()
        
        btn = ttk.Button(self, text="Download", command=imgDownload, width = 20)
        btn.pack()
        
        button1 = ttk.Button(self, text="Home", 
                            command=lambda: controller.show_frame(PageOne), width = 20)
        button1.pack()
        
class Stories(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Stories Downloader", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        
        def stoDownload():
            instance = instaloader.Instaloader()
            userlog = entry_user.get()
            pswd = entry_pass.get()
            entry_user.delete(0, 'end')
            entry_pass.delete(0, 'end')
            entry_user.insert(0, 'Enter Username')
            entry_user.config(fg='grey')
            entry_pass.insert(0, '******')
            entry_pass.config(fg='grey')
            instance.login(user=userlog, passwd=pswd)
            name = entry_name.get()
            profile = Profile.from_username(instance.context, username=name)
            instance.download_stories(userids=[profile.userid], filename_target='{}/stories'.format(profile.username))
            entry_name.delete(0, 'end')
            entry_name.insert(0, 'Enter Target Username')
            entry_name.config(fg='grey')
            messagebox.showinfo("Status", "Stories Downloaded Successfully")
           
        def clear_widget(event):
 
            # will clear out any entry boxes defined below when the user shifts
            # focus to the widgets defined below
            if entry_user == self.focus_get() and entry_user.get() == 'Enter Username':
                entry_user.delete(0, 'end')
                entry_user.config(fg='black')
            elif entry_pass == entry_pass.focus_get() and entry_pass.get() == '******':
                entry_pass.delete(0, 'end')
                entry_pass.config(fg='black')
            elif entry_name == entry_name.focus_get() and entry_name.get() == 'Enter Target Username':
                entry_name.delete(0, 'end')
                entry_name.config(fg='black')
                
        def repopulate_defaults(event):
 
            # will repopulate the default text previously inside the entry boxes defined below if
            # the user does not put anything in while focused and changes focus to another widget
            if entry_user != self.focus_get() and entry_user.get() == '':
                entry_user.insert(0, 'Enter Username')
                entry_user.config(fg='grey')
            elif entry_pass != self.focus_get() and entry_pass.get() == '':
                entry_pass.insert(0, '******')
                entry_pass.config(fg='grey')
            elif entry_name != self.focus_get() and entry_name.get() == '':
                entry_name.insert(0, 'Enter Target Username')
                entry_name.config(fg='grey')
                
        user = tk.Label(self, text="Enter Your Account: ", font=("Arial", 10,))
        user.pack()
        
        entry_user = tk.Entry(self, width=40, fg='grey')
        entry_user.insert(0, 'Enter Username')
        entry_user.bind('<FocusIn>', clear_widget)
        entry_user.bind('<FocusOut>', repopulate_defaults)
        entry_user.pack()
        
        password = tk.Label(self, text="Enter Your Password: ", font=("Arial", 10,))
        password.pack()
        
        entry_pass = tk.Entry(self, width=40, show='*', fg='grey')
        entry_pass.insert(0, '******')
        entry_pass.bind('<FocusIn>', clear_widget)
        entry_pass.bind('<FocusOut>', repopulate_defaults)
        entry_pass.pack()
        
        name = tk.Label(self, text="Enter Target Username: ", font=("Arial", 10,))
        name.pack()
        
        entry_name = tk.Entry(self, width=40, fg='grey')
        entry_name.insert(0, 'Enter Target Username')
        entry_name.bind('<FocusIn>', clear_widget)
        entry_name.bind('<FocusOut>', repopulate_defaults)
        entry_name.pack()
        
        btn2 = ttk.Button(self, text="Login and Download", command=stoDownload, width = 20)
        btn2.pack()
        
        button1 = ttk.Button(self, text="Main Menu", 
                            command=lambda: controller.show_frame(PageOne), width = 20)
        button1.pack()
        
class Photo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Photo & Video Downloader", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        
        def phoDownload(*event):
            instance = instaloader.Instaloader()
            userlog = entry_user.get()
            pswd = entry_pass.get()
            entry_user.delete(0, 'end')
            entry_pass.delete(0, 'end')
            entry_user.insert(0, 'Enter Username')
            entry_user.config(fg='grey')
            entry_pass.insert(0, '******')
            entry_pass.config(fg='grey')
            instance.login(user=userlog, passwd=pswd)
            short = entry_code.get()
            post = Post.from_shortcode(instance.context, short)
            instance.download_post(post, target="{}/photo")
            entry_code.delete(0, 'end')
            entry_code.insert(0, 'Enter Shortcode')
            entry_code.config(fg='grey')
            messagebox.showinfo("Status", "Photo Downloaded Successfully")
            
        def clear_widget(event):
 
            # will clear out any entry boxes defined below when the user shifts
            # focus to the widgets defined below
            if entry_user == self.focus_get() and entry_user.get() == 'Enter Username':
                entry_user.delete(0, 'end')
                entry_user.config(fg='black')
            elif entry_pass == entry_pass.focus_get() and entry_pass.get() == '******':
                entry_pass.delete(0, 'end')
                entry_pass.config(fg='black')
            elif entry_code == entry_code.focus_get() and entry_code.get() == 'Enter Shortcode':
                entry_code.delete(0, 'end')
                entry_code.config(fg='black')
                
        def repopulate_defaults(event):
 
            # will repopulate the default text previously inside the entry boxes defined below if
            # the user does not put anything in while focused and changes focus to another widget
            if entry_user != self.focus_get() and entry_user.get() == '':
                entry_user.insert(0, 'Enter Username')
                entry_user.config(fg='grey')
            elif entry_pass != self.focus_get() and entry_pass.get() == '':
                entry_pass.insert(0, '******')
                entry_pass.config(fg='grey')
            elif entry_code != self.focus_get() and entry_code.get() == '':
                entry_code.insert(0, 'Enter Shortcode')
                entry_code.config(fg='grey')
            
        user = tk.Label(self, text="Enter Your Account: ", font=("Arial", 10,))
        user.pack()
        
        entry_user = tk.Entry(self, width=40, fg='grey')
        entry_user.insert(0, 'Enter Username')
        entry_user.bind('<FocusIn>', clear_widget)
        entry_user.bind('<FocusOut>', repopulate_defaults)
        entry_user.pack()
        
        password = tk.Label(self, text="Enter Your Password: ", font=("Arial", 10,))
        password.pack()
        
        entry_pass = tk.Entry(self, width=40, show='*', fg='grey')
        entry_pass.insert(0, '******')
        entry_pass.bind('<FocusIn>', clear_widget)
        entry_pass.bind('<FocusOut>', repopulate_defaults)
        entry_pass.pack()
            
        code = tk.Label(self, text="Enter Shortcode: ", font=("Arial", 10,))
        code.pack()
        
        entry_code = tk.Entry(self, width=40, fg='grey')
        entry_code.insert(0, 'Enter Shortcode')
        entry_code.bind('<FocusIn>', clear_widget)
        entry_code.bind('<FocusOut>', repopulate_defaults)
        entry_code.pack()
        
        btn3 = ttk.Button(self, text="Login and Download", command=phoDownload, width = 20)
        btn3.pack()
        
        button1 = ttk.Button(self, text="Main Menu", 
                            command=lambda: controller.show_frame(PageOne), width = 20)
        button1.pack()
        
class Highlight(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Highlight Downloader", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        
        def HiDownload():
            instance = instaloader.Instaloader()
            userlog = entry_user.get()
            pswd = entry_pass.get()
            entry_user.delete(0, 'end')
            entry_pass.delete(0, 'end')
            entry_user.insert(0, 'Enter Username')
            entry_user.config(fg='grey')
            entry_pass.insert(0, '******')
            entry_pass.config(fg='grey')
            instance.login(user=userlog, passwd=pswd)
            users1 = entry_users.get()
            profile = Profile.from_username(instance.context, username=users1)
            for highlight in instance.get_highlights(user=profile):
                # highlight is a Highlight object
                for item in highlight.get_items():
                    # item is a StoryItem object
                    instance.download_storyitem(item, '{}/{}'.format(highlight.owner_username, highlight.title))
            entry_users.delete(0, 'end')
            entry_users.insert(0, 'Enter Target Username')
            entry_users.config(fg='grey')
            messagebox.showinfo("Status", "Highlight Downloaded Successfully")
            
        def clear_widget(event):
 
            # will clear out any entry boxes defined below when the user shifts
            # focus to the widgets defined below
            if entry_user == self.focus_get() and entry_user.get() == 'Enter Username':
                entry_user.delete(0, 'end')
                entry_user.config(fg='black')
            elif entry_pass == entry_pass.focus_get() and entry_pass.get() == '******':
                entry_pass.delete(0, 'end')
                entry_pass.config(fg='black')
            elif entry_users == entry_users.focus_get() and entry_users.get() == 'Enter Target Username':
                entry_users.delete(0, 'end')
                entry_users.config(fg='black')
                
        def repopulate_defaults(event):
 
            # will repopulate the default text previously inside the entry boxes defined below if
            # the user does not put anything in while focused and changes focus to another widget
            if entry_user != self.focus_get() and entry_user.get() == '':
                entry_user.insert(0, 'Enter Username')
                entry_user.config(fg='grey')
            elif entry_pass != self.focus_get() and entry_pass.get() == '':
                entry_pass.insert(0, '******')
                entry_pass.config(fg='grey')
            elif entry_users != self.focus_get() and entry_users.get() == '':
                entry_users.insert(0, 'Enter Target Username')
                entry_users.config(fg='grey')
                
        user = tk.Label(self, text="Enter Your Account: ", font=("Arial", 10,))
        user.pack()
        
        entry_user = tk.Entry(self, width=40, fg='grey')
        entry_user.insert(0, 'Enter Username')
        entry_user.bind('<FocusIn>', clear_widget)
        entry_user.bind('<FocusOut>', repopulate_defaults)
        entry_user.pack()
        
        password = tk.Label(self, text="Enter Your Password: ", font=("Arial", 10,))
        password.pack()
        
        entry_pass = tk.Entry(self, width=40, show='*', fg='grey')
        entry_pass.insert(0, '******')
        entry_pass.bind('<FocusIn>', clear_widget)
        entry_pass.bind('<FocusOut>', repopulate_defaults)
        entry_pass.pack()
        
        users = tk.Label(self, text="Enter Target Username: ", font=("Arial", 10,))
        users.pack()
        
        entry_users = tk.Entry(self, width=40, fg='grey')
        entry_users.insert(0, 'Enter Target Username')
        entry_users.bind('<FocusIn>', clear_widget)
        entry_users.bind('<FocusOut>', repopulate_defaults)
        entry_users.pack()
        
        btn4 = ttk.Button(self, text="Login and Download", command=HiDownload, width = 20)
        btn4.pack()
        
        button1 = ttk.Button(self, text="Main Menu", 
                            command=lambda: controller.show_frame(PageOne), width = 20)
        button1.pack()
        
app = IGDownloader()
app.mainloop()

