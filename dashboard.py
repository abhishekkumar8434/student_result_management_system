from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass

class rms:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        # Icons
        try:
            self.logo_dash = ImageTk.PhotoImage(file=r"D:\projects\rms\images\logo_p.png")
        except FileNotFoundError:
            print("Logo image not found!")

        # Title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT,
                      image=self.logo_dash, font=("Goudy Old Style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        
        # Menu
        M_Frame = LabelFrame(self.root, text="Menus", font=("Times New Roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)
        
        btn_course = Button(M_Frame, text="Course", font=("Goudy Old Style", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=200, height=40)
        
        btn_student = Button(M_Frame, text="Student", font=("Goudy Old Style", 15, "bold"), bg="#0b5377",
                             fg="white", cursor="hand2")
        btn_student.place(x=240, y=5, width=200, height=40)
        
        btn_result = Button(M_Frame, text="Result", font=("Goudy Old Style", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2")
        btn_result.place(x=460, y=5, width=200, height=40)
        
        btn_view = Button(M_Frame, text="View Student Result", font=("Goudy Old Style", 15, "bold"), bg="#0b5377",
                          fg="white", cursor="hand2")
        btn_view.place(x=680, y=5, width=200, height=40)
        
        btn_logout = Button(M_Frame, text="Logout", font=("Goudy Old Style", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2")
        btn_logout.place(x=900, y=5, width=200, height=40)
        
        btn_exit = Button(M_Frame, text="Exit", font=("Goudy Old Style", 15, "bold"), bg="#0b5377",
                          fg="white", cursor="hand2", command=self.root.quit)
        btn_exit.place(x=1120, y=5, width=200, height=40)

        # Content Window
        try:
            self.bg_img = Image.open(r"D:\projects\rms\images\img1.png")
            self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_img)
        except FileNotFoundError:
            print("Background image not found!")

        self.lb1_bg = Label(self.root, image=self.bg_img).place(x=400, y=180, width=920, height=350)

        # Update Details
        self.lb1_course = Label(self.root, text="Total Courses\n[0]", font=("Goudy Old Style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lb1_course.place(x=400, y=530, width=300, height=100)
        
        self.lb1_student = Label(self.root, text="Total Students\n[0]", font=("Goudy Old Style", 20), bd=10, relief=RIDGE, bg="blue", fg="white")
        self.lb1_student.place(x=710, y=530, width=300, height=100)
       
        self.lb1_result = Label(self.root, text="Total Results\n[0]", font=("Goudy Old Style", 20), bd=10, relief=RIDGE, bg="green", fg="white")
        self.lb1_result.place(x=1020, y=530, width=300, height=100)

        # Footer
        footer = Label(self.root, text="SRMS-Student Result Management System\nThis site is Owned by Mr.Abhay Sharma",
                       font=("Goudy Old Style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = rms(root)
    root.mainloop()
