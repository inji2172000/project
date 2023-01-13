from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recgonition System")

        #first image
        img=Image.open(r"D:\project\images\1.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"D:\project\images\2.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)  

        #third image
        img2=Image.open(r"D:\project\images\3.jpg")
        img2=img2.resize((575,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=575,height=130)

        
        #bg image
        img3=Image.open(r"D:\project\images\4.jpg")
        img3=img3.resize((1545,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1545,height=710)

        tiltle_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        tiltle_lbl.place(x=0,y=0,width=1545,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1515,height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",18,"bold"))
        Left_frame.place(x=10,y=10,width=700,height=580)

        img_left=Image.open(r"D:\project\images\3.jpg")
        img_left=img_left.resize((685,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=685,height=130)


        #current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",18,"bold"))
        Current_course_frame.place(x=10,y=135,width=680,height=150)
         
        
        #Department
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",18,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","BCA","BBA","B.COM")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)
        
        
        #Course
        Course_label=Label(Current_course_frame,text="Course",font=("times new roman",18,"bold"),bg="white")
        Course_label.grid(row=0,column=0,padx=10,sticky=W)

        Course_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        Course_combo["values"]=("Select Department","BCA","BBA","B.COM")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=1,padx=2,pady=10)


        #Year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",18,"bold"),bg="white")
        year_label.grid(row=0,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Department","BCA","BBA","B.COM")
        year_combo.current(0)
        year_combo.grid(row=0,column=1,padx=2,pady=10)

        
        #Semester
        sem_label=Label(Current_course_frame,text="Semester",font=("times new roman",18,"bold"),bg="white")
        sem_label.grid(row=0,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"]=("Select Department","BCA","BBA","B.COM")
        sem_combo.current(0)
        sem_combo.grid(row=0,column=1,padx=2,pady=10)


        
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",18,"bold"))
        Right_frame.place(x=780,y=10,width=700,height=580)





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()