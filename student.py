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
        main_frame.place(x=10,y=45,width=1515,height=610)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",18,"bold"))
        Left_frame.place(x=10,y=0,width=700,height=590)

        img_left=Image.open(r"D:\project\images\3.jpg")
        img_left=img_left.resize((685,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=685,height=120)


        #current course
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",18,"bold"))
        Current_course_frame.place(x=10,y=125,width=680,height=150)
         
        
        #Department
        dep_label=Label(Current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(Current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","Management")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        #Course
        Course_label=Label(Current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        Course_label.grid(row=0,column=2,padx=10,sticky=W)

        Course_combo=ttk.Combobox(Current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        Course_combo["values"]=("Select Course","BCA","BBA","B.COM","MBA")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,stick=W)


        #Year
        year_label=Label(Current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(Current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        
        #Semester
        sem_label=Label(Current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(Current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Semester","1","2","3","4","5","6")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,stick=W)

        
        #class student information
        Class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",18,"bold"))
        Class_student_frame.place(x=10,y=275,width=680,height=280)

        #student id
        studentId_label=Label(Class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        
        #student name
        studentName_label=Label(Class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #division
        studentId_label=Label(Class_student_frame,text="Division:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        
        #Roll No
        studentId_label=Label(Class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #Gender
        studentId_label=Label(Class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        #DOB
        studentId_label=Label(Class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #Email
        studentId_label=Label(Class_student_frame,text="Email ID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        
        #Phone No
        studentId_label=Label(Class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(Class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        
        #radio buttons
        radiobutton1=ttk.Radiobutton(Class_student_frame,text="Take a Photo Sample",value="Yes")
        radiobutton1.grid(row=4,column=0)
        
        radiobutton2=ttk.Radiobutton(Class_student_frame,text="No Photo Sample",value="Yes")
        radiobutton2.grid(row=4,column=1)


        #button frame
        btn_frame=Frame(Class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=2,y=190,width=672,height=50)


        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",18,"bold"))
        Right_frame.place(x=780,y=0,width=700,height=590)
       

       




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()