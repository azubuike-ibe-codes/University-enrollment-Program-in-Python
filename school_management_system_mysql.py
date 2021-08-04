from tkinter import*
from tkcalendar import*
import pymysql
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
import tkinter.ttk as tkrtk
import tkinter as tkr

class studentRecords:

      def __init__(self, root):
            self.root = root
            self.root.title("Student Record System")
            self.root.geometry("1350x800+0+0")

            notebook = ttk.Notebook(self.root)
            self.TabControl1 = ttk.Frame (notebook)
            self.TabControl2 = ttk.Frame (notebook)
            notebook.add(self.TabControl1, text='School System')
            notebook.add(self.TabControl2, text='Student Details')

            notebook.grid()

            #=============== VARIABLES ===============#
            
            self.StudentID = StringVar ()
            self.Firstname =StringVar()
            self.Surname =StringVar()
            self.Address =StringVar()
            self.PostCode =StringVar()
            self.Gender =StringVar()
            self.DOB =StringVar()
            self.Mobile =StringVar()
            self.Email =StringVar()
            
            self.ParentGuidian =StringVar()
            self.pgFirstname =StringVar()
            self.pgSurname =StringVar()
            self.pgAddress =StringVar()
            self.pgWorkPhone =StringVar()
            self.pgMobile =StringVar()
            self.pgEmail =StringVar()

            self.Course =StringVar()
            self.CourseCode =StringVar()
            self.Faculty =StringVar()
            self.Dean =StringVar()
            self.Head_of_School =StringVar()
            self.ProgramLeader =StringVar()
            self.CourseTutor =StringVar()
            self.Building =StringVar()
            
            self.HomeStudent =StringVar()
            self.Oversea =StringVar()
            self.Accomodation =StringVar()
            self.ExchangeProg =StringVar()
            self.Scholarship=StringVar()

            self.BA =StringVar()
            self.Bsc =StringVar()
            self.MA =StringVar()
            self.Msc =StringVar()
            self.Phd =StringVar()

            self.DataScience =StringVar()
            self.EventDrivenPro =StringVar()
            self.ObjectOriented =StringVar()
            self.Spreadsheet =StringVar()
            self.SystemAnalytics =StringVar()
            self.InfoTech =StringVar()
            self.DigitalGraphics =StringVar()

            self.English =StringVar()
            self.Games =StringVar()
            self.Animation =StringVar()
            self.Database =StringVar()
            self.Maths =StringVar()
            self.AddMaths =StringVar()
            self.Physics =StringVar()
            self.Media =StringVar()
            self.Graphics =StringVar()

            self.ScoreMaths =StringVar()
            self.ScoreEnglish =StringVar()
            self.ScoreBiology =StringVar()
            self.ScoreComputing =StringVar()
            self.ExamNo =StringVar()
            self.ScoreChemistry =StringVar()
            self.ScorePhysics =StringVar()
            self.ScoreAddMaths =StringVar()
            self.ScoreBusiness =StringVar()
            self.TotalScore =StringVar()
            self.Average =StringVar()
            self.Ranking =StringVar()
            self.TaxPeriod =StringVar()
            self.iDate =StringVar()

            self.Module1 =StringVar()
            self.Module2 =StringVar()
            self.Module3 =StringVar()
            self.Module4 =StringVar()
            self.Module5 =StringVar()
            self.Module6 =StringVar()
            self.Module7 =StringVar()
            self.Module8 = StringVar()
            self.Ranking =StringVar()
            self.TotalScore =StringVar()
            self.ResultDate =StringVar()

            self.Subject1 = StringVar ()
            self.Subject2 = StringVar ()
            self.Subject3 = StringVar ()
            self.Subject4 = StringVar ()
            self.Subject5 = StringVar ()
            self.Subject6 = StringVar ()
            self.Subject7 = StringVar ()
            self.Subject8 = StringVar ()

            #=============== bUTTON EXIT ===============#
            def iExit():
                  iExit = tkinter.messagebox.askyesno("Student Management System", "Want to Exit? Confirm!")
                  if iExit > 0:
                        root.destroy()
                        return
            #=============== BUTTON RESET ===============#
            def Reset():
                  self.StudentID.set("")
                  self.Firstname.set("")
                  self.Surname.set("")
                  self.Address.set("")
                  self.PostCode.set("")
                  self.Gender.set("Select Gender")
                  self.DOB.set("")
                  self.Mobile.set("")
                  self.Email.set("")
                  
                  self.ParentGuidian.set("Select")
                  self.pgFirstname.set("")
                  self.pgSurname.set("")
                  self.pgAddress.set("")
                  self.pgWorkPhone.set("")
                  self.pgMobile.set("")
                  self.pgEmail.set("")
                  self.HomeStudent.set("No")
                  self.Oversea.set("No")
                  self.Accomodation.set("No")
                  self.ExchangeProg.set("No")
                  self.Scholarship.set("No")

                  self.Course.set("Select")
                  self.CourseCode.set("")
                  self.Faculty.set("")
                  self.Dean.set("")
                  self.Head_of_School.set("")
                  self.ProgramLeader.set("")
                  self.CourseTutor.set("")
                  self.Building.set("")

                  self.BA.set("0")
                  self.Bsc.set("0")
                  self.MA.set("0")
                  self.Msc.set("0")
                  self.Phd.set("0")

                  self.DataScience.set("No")
                  self.EventDrivenPro.set("No")
                  self.ObjectOriented.set("No")
                  self.Spreadsheet.set("No")
                  self.SystemAnalytics.set("No")
                  self.InfoTech.set("No")
                  self.DigitalGraphics.set("No")

                  self.English.set("No")
                  self.Games.set("No")
                  self.Animation.set("No")
                  self.Database.set("No")
                  self.Maths.set("No")
                  self.AddMaths.set("No")
                  self.Physics.set("No")
                  self.Media.set("No")
                  self.Graphics.set("No")

                  self.TotalScore.set("")
                  self.Average.set("")
                  self.Ranking.set("")
                  self.TaxPeriod.set("")
                  self.iDate.set("")
                  self.Module1.set("")
                  self.Module2.set("")
                  self.Module3.set("")
                  self.Module4.set("")
                  self.Module5.set("")
                  self.Module6.set("")
                  self.Module7.set("")
                  self.Module8.set("")
                  self.Ranking.set("")
                  self.TotalScore.set("")
                  self.ResultDate.set("")

                  self.Subject1.set("")
                  self.Subject2.set("")
                  self.Subject3.set("")
                  self.Subject4.set("")
                  self.Subject5.set("")
                  self.Subject6.set("")
                  self.Subject7.set("")
                  self.Subject8.set("")

                   #=============== FRAMES ===============#

            def setSubject(event):
                  if self.Subject1.get() == 'Event Driven Pro':
                        self.EventDrivenPro.set("Core Unit")
                        self.txt1.configure(state = NORMAL)
                        self.txt1.focus_set()
                  elif self.Subject1.get() == '':
                        self.EventDrivenPro.set("No")
                        self.txt1.configure(state = DISABLED)
                        self.Module1.set("")

                  if self.Subject2.get() == 'Object Oriented':
                        self.ObjectOriented.set("Completed")
                        self.Spreadsheet.set("No")
                        self.txt2.configure(state = NORMAL)
                        self.txt2.focus_set()
                  if self.Subject2.get() == 'Spreadsheet':
                        self.Spreadsheet.set("Unit Core")
                        self.ObjectOriented.set("No")
                        self.txt2.configure(state = NORMAL)
                        self.txt2.focus_set()
                  elif self.Subject2.get() == '':
                        self.Spreadsheet.set("No")
                        self.ObjectOriented.set("No")
                        self.txt2.configure(state = DISABLED)
                        self.Module2.set("")

                  if self.Subject3.get() == 'System Analytics':
                        self.SystemAnalytics.set("Core Unit")
                        self.Spreadsheet.set("No")
                        self.txt3.configure(state = NORMAL)
                        self.txt3.focus_set()
                  if self.Subject3.get() == 'Info Tech':
                        self.InfoTech.set("Core Unit")
                        self.SystemAnalytics.set("No")
                        self.txt3.configure(state = NORMAL)
                        self.Module3.set("")
                  elif  self.Subject3.get() == '':
                        self.InfoTech.set("No")
                        self.SystemAnalytics.set("No")
                        self.txt3.configure(state = DISABLED)
                        self.Module3.set("")

                  if self.Subject4.get() == 'Digital Graphics':
                        self.ObjectOriented.set("Completed")
                        self.English.set("No")
                        self.txt4.configure(state = NORMAL)
                        self.txt4.focus_set()
                  if self.Subject4.get() == 'English':
                        self.English.set("Unit Core")
                        self.ObjectOriented.set("No")
                        self.txt4.configure(state = NORMAL)
                        self.txt4.focus_set()
                  elif self.Subject4.get() == '':
                        self.English.set("No")
                        self.DigitalGraphics.set("No")
                        self.txt4.configure(state = DISABLED)
                        self.Module4.set("")

                  if self.Subject5.get() == 'Games':
                        self.Games.set("Completed")
                        self.Animation.set("No")
                        self.txt5.configure(state = NORMAL)
                        self.txt5.focus_set()
                  if self.Subject5.get() == 'Animation':
                        self.Animation.set("Unit Core")
                        self.Games.set("No")
                        self.txt5.configure(state = NORMAL)
                        self.txt5.focus_set()
                  elif self.Subject5.get() == '':
                        self.Animation.set("No")
                        self.Games.set("No")
                        self.txt5.configure(state = DISABLED)
                        self.Module5.set("") 

                  if self.Subject6.get() == 'Database':
                        self.Database.set("Completed")
                        self.Maths.set("No")
                        self.txt6.configure(state = NORMAL)
                        self.txt6.focus_set()
                  if self.Subject6.get() == 'Maths':
                        self.Maths.set("Unit Core")
                        self.Game6.set("No")
                        self.txt6.configure(state = NORMAL)
                        self.txt6.focus_set()
                  elif self.Subject6.get() == '':
                        self.Database.set("No")
                        self.Maths.set("No")
                        self.txt6.configure(state = DISABLED)
                        self.Module6.set("") 

                  if self.Subject7.get() == 'Add Maths':
                        self.AddMaths.set("Complete")
                        self.Physics.set("No")
                        self.txt7.configure(state = NORMAL)
                        self.txt7.focus_set()
                  if self.Subject7.get() == 'Physics':
                        self.Physics.set("Core Unit")
                        self.AddMaths.set("No")
                        self.txt7.configure(state = NORMAL)
                        self.txt7.focus_set()
                  elif  self.Subject7.get() == '':
                        self.Physics.set("No")
                        self.AddMaths.set("No")
                        self.txt7.configure(state = DISABLED)
                        self.Module7.set("")

                  if self.Subject8.get() == 'Data Science':
                        self.Physics.set("Core Unit")
                        self.txt8.configure(state = NORMAL)
                        self.txt8.focus_set()

                  elif self.Subject8.get() == '':
                        self.DataScience.set("No")
                        self.txt8.configure(state = DISABLED)
                        self.Module8.set("")

            #================================================= FRAMES ===========================================================#

                  #=============== BSC SERIOUS GAMES ===============#
            def CourseData(event):
                  if self.Course.get() == 'Bsc Serious Game':
                        self.CourseCode.set("BScGS354")
                        self.Faculty.set("School of Computer Science")
                        self.Dean.set("Prof. Folake Tomilola")
                        self.Head_of_School.set("Dunny Tony Jonathan")
                        self.ProgramLeader.set("Dr. Peter Stone")
                        self.CourseTutor.set("Rose Royce")
                        self.Building.set("Kelly's House")

                  #=============== BSC COMPUTER GAMES ===============#
                  if self.Course.get() == 'Bsc Computer Games':
                        self.CourseCode.set("BScCG261")
                        self.Faculty.set("School of Computer Science")
                        self.Dean.set("Prof. Azubuike Ibe")
                        self.Head_of_School.set("KK Iwuala")
                        self.ProgramLeader.set("Michael Chidi")
                        self.CourseTutor.set("Anthony Keke")
                        self.Building.set("Mgbeahuruike House")
            
            #=============== BSC COMPUTER ANIMATION ===============#
                  if self.Course.get() == 'Bsc Computer ANIMATION':
                        self.CourseCode.set("BScCA409")
                        self.Faculty.set("School of Computer Science")
                        self.Dean.set("Prof. Ethelbert Nwamadi")
                        self.Head_of_School.set("Arthur Ibeawuchi")
                        self.ProgramLeader.set("Clement Erondu")
                        self.CourseTutor.set("Amajuoyi John")
                        self.Building.set("Freedom building")

            #=============== BA ANIMATION ===============#
                  if self.Course.get() == 'BA ANIMATION':
                        self.CourseCode.set("BAAN589")
                        self.Faculty.set("School of Computer Science")
                        self.Dean.set("Kelechukwu Diala PhD")
                        self.Head_of_School.set("Martin Osuala")
                        self.ProgramLeader.set("Ikenna Nwagboso")
                        self.CourseTutor.set("Emebiri Emilia")
                        self.Building.set("Ibe House")
            
            #=============== BSC COMPUTING ===================#
                  if self.Course.get() == 'Bsc Computing':
                        self.CourseCode.set("BScC893")
                        self.Faculty.set("School of Computer Science")
                        self.Dean.set("Prof. Charly Maguire")
                        self.Head_of_School.set("Kazim M")
                        self.ProgramLeader.set("Caritas Ujunwa")
                        self.CourseTutor.set("Paul Eluwa")
                        self.Building.set("Catoon Building")

            #=============== BSC INFORMATION SYSTEMS===============#
                  if self.Course.get() == 'Bsc Information Systems':
                        self.CourseCode.set("BScIS833")
                        self.Faculty.set("School of Computer Science")
                        self.Dean.set("Prof. Merlin MacMahon")
                        self.Head_of_School.set("Andrew McCarthy")
                        self.ProgramLeader.set("Julian Pat")
                        self.CourseTutor.set("Kish Hood")
                        self.Building.set("Mercy Building")

            #================================================= ADD MODULES ===========================================================#

            def AddModuleScore ():

                  if self.Module1.get() == "":
                        self.Module1.set("0")
                  if self.Module2.get() == "":
                        self.Module2.set("0")
                  if self.Module3.get() == "":
                        self.Module3.set("0")
                  if self.Module4.get() == "":
                        self.Module4.set("0")
                  if self.Module5.get() == "":
                        self.Module5.set("0")
                  if self.Module6.get() == "":
                        self.Module6.set("0")
                  if self.Module7.get() == "":
                        self.Module7.set("0")
                  if self.Module8.get() == "":
                        self.Module8.set("0")
                  
                  Unit1 = float(self.Module1.get())
                  Unit2 = float(self.Module2.get())
                  Unit3 = float(self.Module3.get())
                  Unit4 = float(self.Module4.get())
                  Unit5 = float(self.Module5.get())
                  Unit6 = float(self.Module6.get())
                  Unit7 = float(self.Module7.get())
                  Unit8 = float(self.Module8.get())

                  UnitTotal = (Unit1 + Unit2 + Unit2 + Unit4 + Unit5 + Unit6 + Unit7 + Unit8)
                  self.TotalScore.set(int(UnitTotal))
            
                  if (UnitTotal >= 700):
                        self.Ranking.set("1st Class")
                  elif (UnitTotal >= 600):
                        self.Ranking.set("2.1 Upper")
                  elif (UnitTotal >= 500):
                        self.Ranking.set("2.ii Lower")
                  elif (UnitTotal >= 400):
                        self.Ranking.set("3rd Class")
                  elif (UnitTotal <= 400):
                        self.Ranking.set("Fail")
                  
                  

            #=================================================== MYSQL DATA CONNECTIVITY =======================================================#

            def addData():
                  if self.StudentID.get() =="" or self.Firstname.get() =="" or self.Surname.get() =="":
                        tkinter.messagebox.showerror("Error correct member details")
                  else:
                        sqlCon = pymysql.connect(host = "localhost", user = "root", password = "00000000#", database ="studentranking")
                        cur = sqlCon.cursor()
                        cur.execute("insert into studentranking values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                        ,(

                        self.StudentID.get(),
                        self.Firstname.get(),
                        self.Surname.get(),
                        self.Address.get(),
                        self.PostCode.get(),
                        self.Gender.get(),
                        self.DOB.get(),
                        self.Mobile.get(),
                        self.Email.get(),
                        
                        self.ParentGuidian.get(),
                        self.pgFirstname.get(),
                        self.pgSurname.get(),
                        self.pgAddress.get(),
                        self.pgWorkPhone.get(),
                        self.pgMobile.get(),
                        self.pgEmail.get(),

                        self.Course.get(),
                        self.CourseCode.get(),
                        self.Faculty.get(),
                        self.Dean.get(),
                        self.Head_of_School.get(),
                        self.ProgramLeader.get(),
                        self.CourseTutor.get(),
                        self.Building.get(),
                        
                        self.HomeStudent.get(),
                        self.Oversea.get(),
                        self.Accomodation.get(),
                        self.ExchangeProg.get(),
                        self.Scholarship.get(),

                        self.BA.get(),
                        self.Bsc.get(),
                        self.MA.get(),
                        self.Msc.get(),
                        self.Phd.get(),

                        self.DataScience.get(),
                        self.EventDrivenPro.get(),
                        self.ObjectOriented.get(),
                        self.Spreadsheet.get(),
                        self.SystemAnalytics.get(),
                        self.InfoTech.get(),
                        self.DigitalGraphics.get(),

                        self.English.get(),
                        self.Games.get(),
                        self.Animation.get(),
                        self.Database.get(),
                        self.Maths.get(),
                        self.AddMaths.get(),
                        self.Physics.get(),
                        self.Media.get(),
                        self.Graphics.get(),

                        self.Module1.get(),
                        self.Module2.get(),
                        self.Module3.get(),
                        self.Module4.get(),
                        self.Module5.get(),
                        self.Module6.get(),
                        self.Module7.get(),
                        self.Module8.get(),
                        self.Ranking.get(),
                        self.TotalScore.get(),
                        self.ResultDate.get(),
                        
                        ))

                        sqlCon.commit()
                        sqlCon.close()
                        tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

            #=================================================== DATA UPDATES =======================================================#

            def update():

                  sqlCon = pymysql.connect(host = "localhost", user = "root", password = "00000000#", database ="studentranking")
                  cur = sqlCon.cursor()
                  cur.execute("update studentranking set firstname=%s, surname=%s, address=%s, \
                              postcode=%s, gender=%s, dob=%s, mobile=%s, email=%s, parent=%s, pfirstname=%s, psurname=%s, \
                              paddress=%s, pworkphone=%s, pmobile=%s, pemail=%s, course=%s, coursecode=%s,  faculty=%s, deanoffc=%s, \
                              hos=%s, proleader=%s, coursetutor=%s, building=%s, homestd=%s, overseastd=%s, accomod=%s, exchangestd=%s, \
                              scholarship=%s, ba=%s, bsc=%s, ma=%s, msc=%s, phd=%s, datasci=%s, eventdriprog=%s, objectori=%s, \
                              spreadsheet=%s, systemanalytics=%s, infotech=%s, digitalgrap=%s, english=%s, games=%s, animation=%s, \
                              database=%s, maths=%s, addmath=%s, physics=%s, media=%s, graphicdesign=%S, module1=%s, \
                              module2=%s, module3=%s, module4=%s, module5=%s, module6=%s, module7=%s, module8=%s, totalscore=%s, \
                              ranking=%s, dateofrank=%s where studentid=%s" ,(

                  self.StudentID.get(),
                  self.Firstname.get(),
                  self.Surname.get(),
                  self.Address.get(),
                  self.PostCode.get(),
                  self.Gender.get(),
                  self.DOB.get(),
                  self.Mobile.get(),
                  self.Email.get(),
                        
                  self.ParentGuidian.get(),
                  self.pgFirstname.get(),
                  self.pgSurname.get(),
                  self.pgAddress.get(),
                  self.pgWorkPhone.get(),
                  self.pgMobile.get(),
                  self.pgEmail.get(),

                  self.Course.get(),
                  self.CourseCode.get(),
                  self.Faculty.get(),
                  self.Dean.get(),
                  self.Head_of_School.get(),
                  self.ProgramLeader.get(),
                  self.CourseTutor.get(),
                  self.Building.get(),
                  
                  self.HomeStudent.get(),
                  self.Oversea.get(),
                  self.Accomodation.get(),
                  self.ExchangeProg.get(),
                  self.Scholarship.get(),

                  self.BA.get(),
                  self.Bsc.get(),
                  self.MA.get(),
                  self.Msc.get(),
                  self.Phd.get(),

                  self.DataScience.get(),
                  self.EventDrivenPro.get(),
                  self.ObjectOriented.get(),
                  self.Spreadsheet.get(),
                  self.SystemAnalytics.get(),
                  self.InfoTech.get(),
                  self.DigitalGraphics.get(),

                  self.English.get(),
                  self.Games.get(),
                  self.Animation.get(),
                  self.Database.get(),
                  self.Maths.get(),
                  self.AddMaths.get(),
                  self.Physics.get(),
                  self.Media.get(),
                  self.Graphics.get(),

                  self.Module1.get(),
                  self.Module2.get(),
                  self.Module3.get(),
                  self.Module4.get(),
                  self.Module5.get(),
                  self.Module6.get(),
                  self.Module7.get(),
                  self.Module8.get(),
                  self.Ranking.get(),
                  self.TotalScore.get(),
                  self.ResultDate.get()

                        ))

                  sqlCon.commit()
                  sqlCon.close()
                  tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Updated")

            #=================================================== DELETE DB ==============================================================#

            def deletedb():
                  sqlCon = pymysql.connect(host="localhost", user="root", password="00000000#", database="studentranking")
                  cur =sqlCon.cursor()
                  cur.execute("delete from studentranking where studentid=%s", self.StudentID)
                  sqlCon.commit()
                  sqlCon.close()
                  tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")

            #=================================================== DISPLAY DB ==============================================================#

            def DisplayData():
                  sqlCon = pymysql.connect(host = "localhost", user = "root", password = "00000000#", database ="studentranking")
                  cur = sqlCon.cursor()
                  cur.execute("select * from studentranking")
                  result = cur.fetchall()
                  if len(result) !=0:
                        self.Student_Record.delete(*self.Student_Record.get_children())
                        for row in result:
                              self.Student_Record.insert('', END, values=row)
                        sqlCon.commit()
                  sqlCon.close()
            
            #=================================================== STUDENT INFO ==============================================================#

            def stuInfo(event):
                  viewInfor = self.Student_Record.focus()
                  learnerData = self.Student_Record.item(viewInfo)
                  row = learnerData ['values']

                  self.StudentID.set(row[0])
                  self.Firstname.set(row[1])
                  self.Surname.set(row[2])
                  self.Address.set(row[3])
                  self.PostCode.set(row[4])
                  self.Gender.set(row[5])
                  self.DOB.set(row[6])
                  self.Mobile.set(row[7])
                  self.Email.set(row[8])
                        
                  self.ParentGuidian.set(row[9])
                  self.pgFirstname.set(row[10])
                  self.pgSurname.set(row[11])
                  self.pgAddress.set(row[12])
                  self.pgWorkPhone.set(row[13])
                  self.pgMobile.set(row[14])
                  self.pgEmail.set(row[15])

                  self.Course.set(row[16])
                  self.CourseCode.set(row[17])
                  self.Faculty.set(row[18])
                  self.Dean.set(row[19])
                  self.Head_of_School.set(row[20])
                  self.ProgramLeader.set(row[21])
                  self.CourseTutor.set(row[22])
                  self.Building.set(row[23])
                  
                  self.HomeStudent.set(row[24])
                  self.Oversea.set(row[25])
                  self.Accomodation.set(row[26])###
                  self.ExchangeProg.set(row[27])
                  self.Scholarship.set(row[28])

                  self.BA.set(row[29])
                  self.Bsc.set(row[31])
                  self.MA.set(row[32])
                  self.Msc.set(row[33])
                  self.Phd.set(row[34])

                  self.DataScience.set(row[35])
                  self.EventDrivenPro.set(row[36])
                  self.ObjectOriented.set(row[37])
                  self.Spreadsheet.set(row[38])
                  self.SystemAnalytics.set(row[39])
                  self.InfoTech.set(row[40])
                  self.DigitalGraphics.set(row[41])

                  self.English.set(row[42])
                  self.Games.set(row[43])
                  self.Animation.set(row[44])
                  self.Database.set(row[45])
                  self.Maths.set(row[45])
                  self.AddMaths.set(row[46])
                  self.Physics.set(row[47])
                  self.Media.set(row[48])
                  self.Graphics.set(row[49])

                  self.Module1.set(row[50])
                  self.Module2.set(row[51])
                  self.Module3.set(row[52])
                  self.Module4.set(row[53])
                  self.Module5.set(row[54])
                  self.Module6.set(row[55])
                  self.Module7.set(row[56])
                  self.Module8.set(row[57])

                  self.Ranking.set(row[58])
                  self.TotalScore.set(row[59])
                  self.ResultDateset.set(row[60])


            #=================================================== FRAMES ==============================================================#
            
            MainFrame = Frame (self.TabControl1, bd=10, width=1350, height=700, relief=RIDGE)
            MainFrame.grid(padx=5, pady=10)

            Tab2Frame = Frame (self.TabControl2, bd=10, width=1350, height=700, relief=RIDGE)
            Tab2Frame.grid (padx=10)

            TopFrame3 = Frame (MainFrame, bd=10, width=1340, height=500, relief=RIDGE)
            TopFrame3.grid ()

            RightFrame1 = Frame (TopFrame3, bd=5, width=320, height=400, padx=2, bg="cadetblue", relief=RIDGE)
            RightFrame1.pack (side=RIGHT, pady=1)

            InnerRightFrame = Frame (RightFrame1, bd=5, width=310, height=300, padx=2, relief=RIDGE)
            InnerRightFrame.pack (side=TOP, pady=2)

            CalendarFrame = Frame (InnerRightFrame, bd=5, width=310, height=300, padx=2, relief=RIDGE)
            CalendarFrame .pack (side=TOP, pady=1)

            UnitsFrame = Frame (InnerRightFrame, bd=5, width=310, height=300, padx=2, relief=RIDGE)
            UnitsFrame.pack (side=TOP, pady=1)

            ResultsFrame = Frame (InnerRightFrame, bd=5, width=330, height=50, padx=2, relief=RIDGE)
            ResultsFrame.pack (side=TOP, pady=1)

            ResultsFrameLeft = Frame (ResultsFrame, bd=0, width=310, height=50, padx=2, relief=RIDGE)
            ResultsFrameLeft.grid( row=0, column=0, pady=1)

            UnitNo = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, relief=RIDGE)
            UnitNo.grid (row=0, column=0, pady=2)

            UnitSubject = Frame(UnitsFrame, bd=1, width=210, height=300, padx=2, pady=4)
            UnitSubject.grid (row=0, column=1, pady=2)

            UnitScore = Frame(UnitsFrame, bd=0, width=50, height=300, padx=2, pady=3, relief=RIDGE)
            UnitScore.grid (row=0, column=2, pady=1)

            #================ LEFT =================#

            LeftFrame = Frame (TopFrame3, bd=5, width=1340, height=400, padx=2, bg="cadetblue", relief=RIDGE)
            LeftFrame.pack (side=RIGHT, pady=0)

            CourseFrame = Frame (LeftFrame, bd=5, width=600, height=180, padx=4,  relief=RIDGE)
            CourseFrame.pack (side=TOP, pady=2)

            LeftFrame2 = Frame (LeftFrame, bd=5, width=600, height=180, padx=2, bg="cadetblue", relief=RIDGE)
            LeftFrame2.pack (side=TOP)
            
            StudentStatusFrame = Frame (LeftFrame2, bd=5, width=300, height=170, padx=2,  relief=RIDGE)
            StudentStatusFrame.pack (side=LEFT)

            DegreeFrame = Frame (LeftFrame2, bd=5, width=300, height=170, padx=2,  relief=RIDGE)
            DegreeFrame.pack (side=RIGHT)

            ButtonFrame = Frame (LeftFrame, bd=5, width=320, height=50, padx=3,  relief=RIDGE)
            ButtonFrame.pack (side=LEFT, pady=3)

            #================= RIGHT ===================#

            RightFrame2 = Frame (TopFrame3, width=300, height=400, padx=2, bg="cadetblue", relief=RIDGE)
            RightFrame2.pack (side=LEFT, pady=5)

            StudentFrame = Frame (RightFrame2, bd=5, width=280, height=50, padx=2,  relief=RIDGE)
            StudentFrame.pack (side=TOP, pady=3)

            ParentFrame = Frame (RightFrame2, bd=5, width=280, height=50, padx=3,  relief=RIDGE)
            ParentFrame.pack (side=TOP)

            #================= TOP ==========================#

            TopFrame11 = Frame (Tab2Frame, bd=10, width=1340, height=60, relief=RIDGE)
            TopFrame11.grid( row=0, column=0)

            TopFrame12 = Frame (Tab2Frame, bd=10, width=1340, height=100, relief=RIDGE)
            TopFrame12.grid( row=1, column=0)

            TopFrame12a = Frame (TopFrame12, bd=10, width=1000, height=100, relief=RIDGE)
            TopFrame12a.grid( row=1, column=1)

            TopFrame12b = Frame (TopFrame12, bd=10, width=340, height=100, relief=RIDGE)
            TopFrame12b.grid( row=1, column=0)

            #=============== STUDENT ID ================#

            self.lblStudentID = Label (StudentFrame, font =('arial', 12, 'bold'), text='Student ID', bd=7, anchor='w', justify=LEFT)
            self.lblStudentID.grid( row=0, column=0, sticky= W, padx=5, pady=2)
            self.txtStudentID = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.StudentID)
            self.txtStudentID.grid( row=0, column=1)

            self.lblFirstname = Label (StudentFrame, font =('arial', 12, 'bold'), text='Firstname', bd =7, justify=LEFT)
            self.lblFirstname.grid( row=1, column=0, sticky= W, padx=5)
            self.txtFirstname = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.Firstname)
            self.txtFirstname.grid( row=1, column=1)

            self.lblSurname = Label (StudentFrame, font =('arial', 12, 'bold'), text='Surname', bd =7, justify=LEFT)
            self.lblSurname.grid( row=2, column=0, sticky= W, padx=5)
            self.txtSurname = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.Surname)
            self.txtSurname.grid( row=2, column=1)

            self.lblAddress = Label (StudentFrame, font =('arial', 12, 'bold'), text='Address', bd =7, justify=LEFT)
            self.lblAddress.grid( row=3, column=0, sticky= W, padx=5)
            self.txtAddress = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.Address)
            self.txtAddress.grid( row=3, column=1)

            self.lblPostCode = Label (StudentFrame, font =('arial', 12, 'bold'), text='PostCode', bd =7, justify=LEFT)
            self.lblPostCode.grid( row=4, column=0, sticky= W, padx=5)
            self.txtPostCode = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.PostCode)
            self.txtPostCode.grid( row=4, column=1)

            self.lblGender = Label (StudentFrame, font =('arial', 12, 'bold'), text='Gender', bd =7, justify=LEFT)
            self.lblGender.grid( row=5, column=0, sticky= W, padx=5)
            self.cboGender = ttk.Combobox (StudentFrame, textvariable = self.Gender, width= 28,
                                           font =('arial', 12, 'bold' ), state='randomly')
            self.cboGender['value' ] = (' Select Gender', 'Female', 'Male', 'Haemphrodite')
            self.cboGender.current (0)
            self.cboGender.grid (row=5, column=1)

            self.lblDOB = Label (StudentFrame, font =('arial', 12, 'bold'), text='DOB', bd =7, justify=LEFT)
            self.lblDOB.grid( row=6, column=0, sticky= W, padx=5)
            self.txtDOB = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.DOB)
            self.txtDOB.grid( row=6, column=1)

            self.lblMobile = Label (StudentFrame, font =('arial', 12, 'bold'), text='Mobile', bd =7, justify=LEFT)
            self.lblMobile.grid( row=7, column=0, sticky= W, padx=5)
            self.txtMobile = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.Mobile)
            self.txtMobile.grid( row=7, column=1)

            self.lblEmail = Label (StudentFrame, font =('arial', 12, 'bold'), text='Email', bd =7, justify=LEFT)
            self.lblEmail.grid( row=8, column=0, sticky= W, padx=5)
            self.txtEmail = Entry (StudentFrame, font =('arial', 12, 'bold'), width=30, justify ='left', textvariable = self.Email)
            self.txtEmail.grid( row=8, column=1)

            #================ PARENT GUIDIAN =================#

            self.lblParentGuidian = Label (ParentFrame, font =('arial', 12, 'bold'), text='Parent/Guidian', bd =7, justify=LEFT)
            self.lblParentGuidian.grid( row=0, column=0, sticky= W, padx=5)
            self.cboParentGuidian = ttk.Combobox (ParentFrame, textvariable = self.ParentGuidian, width= 24,
                                           font =('arial', 12, 'bold' ), state='randomly')
            self.cboParentGuidian['value' ] = ('Select', 'Parent', 'Guidian')
            self.cboParentGuidian.current (0)
            self.cboParentGuidian.grid (row=0, column=1)

            self.lblFirstname = Label (ParentFrame, font =('arial', 12, 'bold'), text='Firstname', bd =7, justify=LEFT)
            self.lblFirstname.grid( row=1, column=0, sticky= W, padx=5)
            self.txtFirstname = Entry (ParentFrame, font =('arial', 12, 'bold'), width=26, justify ='left', textvariable = self.pgFirstname)
            self.txtFirstname.grid( row=1, column=1)

            self.lblSurname = Label (ParentFrame, font =('arial', 12, 'bold'), text='Surname', bd =7, justify=LEFT)
            self.lblSurname.grid( row=2, column=0, sticky= W, padx=5)
            self.txtSurname = Entry (ParentFrame, font =('arial', 12, 'bold'), width=26, justify ='left', textvariable = self.pgSurname)
            self.txtSurname.grid( row=2, column=1)

            self.lblAddress = Label (ParentFrame, font =('arial', 12, 'bold'), text='Address', bd =7, justify=LEFT)
            self.lblAddress.grid( row=3, column=0, sticky= W, padx=5)
            self.txtAddress = Entry (ParentFrame, font =('arial', 12, 'bold'), width=26, justify ='left', textvariable = self.pgAddress)
            self.txtAddress.grid( row=3, column=1)

            self.lblWorkPhone = Label (ParentFrame, font =('arial', 12, 'bold'), text='WorkPhone', bd =7, justify=LEFT)
            self.lblWorkPhone.grid( row=4, column=0, sticky= W, padx=5)
            self.txtWorkPhone = Entry (ParentFrame, font =('arial', 12, 'bold'), width=26, justify ='left', textvariable = self.pgWorkPhone)
            self.txtWorkPhone.grid( row=4, column=1)

            self.lblMobile = Label (ParentFrame, font =('arial', 12, 'bold'), text='Mobile', bd =7, justify=LEFT)
            self.lblMobile.grid( row=5, column=0, sticky= W, padx=5)
            self.txtMobile = Entry (ParentFrame, font =('arial', 12, 'bold'), width=26, justify ='left', textvariable = self.pgMobile)
            self.txtMobile.grid( row=5, column=1)

            self.lblEmail = Label (ParentFrame, font =('arial', 12, 'bold'), text='Email', bd =7, justify=LEFT)
            self.lblEmail.grid( row=6, column=0, sticky= W, padx=5)
            self.txtEmail = Entry (ParentFrame, font =('arial', 12, 'bold'), width=26, justify ='left', textvariable = self.pgEmail)
            self.txtEmail.grid( row=6, column=1)

      
            #================ COURSE =================#

            self.Course.set ("Course Selector")
            self.lblCourse= Label (CourseFrame, font =('arial', 12, 'bold'), text='Course', bd =6, justify=LEFT)
            self.lblCourse.grid( row=0, column=0, sticky= W)

            self.cboCourse = ttk.Combobox (CourseFrame, textvariable = self.Course, width= 41, font =('arial', 12, 'bold' ), state='randomly')
            self.cboCourse['value' ] = ('Select', 'Bsc Serious Game', 'Bsc Computer Games', 'Bsc Computer Animation', 'BA Animation', 'Bsc Computing', 'Bsc Information Systems')
            self.cboCourse.current (0)
            self.cboCourse.grid (row=0, column=1)
            self.cboCourse.bind('<<ComboboxSelected>>', CourseData)

            self.lblCourseCode= Label (CourseFrame, font =('arial', 12, 'bold'), text='Course Code', bd =6, justify=LEFT)
            self.lblCourseCode.grid( row=1, column=0, sticky= W)
            self.txtCourseCode = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.CourseCode)
            self.txtCourseCode.grid( row=1, column=1)

            self.lblFaculty= Label (CourseFrame, font =('arial', 12, 'bold'), text='Faculty', bd =6, justify=LEFT)
            self.lblFaculty.grid( row=2, column=0, sticky= W)
            self.txtFaculty = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.Faculty)
            self.txtFaculty.grid( row=2, column=1)

            self.lblDean= Label (CourseFrame, font =('arial', 12, 'bold'), text='Dean', bd =6, justify=LEFT)
            self.lblDean.grid( row=3, column=0, sticky= W)
            self.txtDean = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.Dean)
            self.txtDean.grid( row=3, column=1)

            self.lblHead_of_School= Label (CourseFrame, font =('arial', 12, 'bold'), text='Head of School', bd =6, justify=LEFT)
            self.lblHead_of_School.grid( row=4, column=0, sticky= W)
            self.txtHead_of_School = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.Head_of_School)
            self.txtHead_of_School.grid( row=4, column=1)

            self.lblProgramLeader= Label (CourseFrame, font =('arial', 12, 'bold'), text='Program Leader', bd =6, justify=LEFT)
            self.lblProgramLeader.grid( row=5, column=0, sticky= W)
            self.txtProgramLeader = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.ProgramLeader)
            self.txtProgramLeader.grid( row=5, column=1)

            self.lblCourseTutor= Label (CourseFrame, font =('arial', 12, 'bold'), text='Course Tutor', bd =6, justify=LEFT)
            self.lblCourseTutor.grid( row=6, column=0, sticky= W)
            self.txtCourseTutor = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.CourseTutor)
            self.txtCourseTutor.grid( row=6, column=1)

            self.lblBuilding= Label (CourseFrame, font =('arial', 12, 'bold'), text='Building', bd =6, justify=LEFT)
            self.lblBuilding.grid( row=7, column=0, sticky= W)
            self.txtBuilding = Entry (CourseFrame, font =('arial', 12, 'bold'), width=43, justify ='left', textvariable = self.Building)
            self.txtBuilding.grid( row=7, column=1)


            #================ STUDENT STATUS =================#

            self.lblHomeStudent= Label (StudentStatusFrame, font =('arial', 12, 'bold'), text='Home Student', bd =6, justify=LEFT)
            self.lblHomeStudent.grid( row=0, column=0, sticky= W)
            self.cboHomeStudent = ttk.Combobox (StudentStatusFrame, textvariable = self.HomeStudent, width= 10, font =('arial', 12, 'bold' ), state='randomly')
            self.cboHomeStudent['value' ] = ('No','Yes')
            self.cboHomeStudent.current (0)
            self.cboHomeStudent.grid (row=0, column=1, pady=8)

            self.lblOversea= Label (StudentStatusFrame, font =('arial', 12, 'bold'), text='Oversea', bd =6, justify=LEFT)
            self.lblOversea.grid( row=1, column=0, sticky= W)
            self.cboOversea = ttk.Combobox (StudentStatusFrame, textvariable = self.Oversea, width= 10,
                                           font =('arial', 12, 'bold' ), state='randomly')
            self.cboOversea['value' ] = ('No','Yes')
            self.cboOversea.current (0)
            self.cboOversea.grid (row=1, column=1, pady=8)

            self.lblAccomodation= Label (StudentStatusFrame, font =('arial', 12, 'bold'), text='Accomodation', bd =6, justify=LEFT)
            self.lblAccomodation.grid( row=2, column=0, sticky= W)
            self.cboAccomodation = ttk.Combobox (StudentStatusFrame, textvariable = self.Accomodation, width= 10,
                                           font =('arial', 12, 'bold' ), state='randomly')
            self.cboAccomodation['value' ] = ('No','Yes')
            self.cboAccomodation.current (0)
            self.cboAccomodation.grid (row=2, column=1, pady=8)

            self.lblExchangeProg= Label (StudentStatusFrame, font =('arial', 12, 'bold'), text='ExchangeProg', bd =6, justify=LEFT)
            self.lblExchangeProg.grid( row=3, column=0, sticky= W)
            self.cboExchangeProg = ttk.Combobox (StudentStatusFrame, textvariable = self.ExchangeProg, width= 10,
                                           font =('arial', 12, 'bold' ), state='randomly')
            self.cboExchangeProg['value' ] = ('No','Yes')
            self.cboExchangeProg.current (0)
            self.cboExchangeProg.grid (row=3, column=1, pady=8)

            self.lblScholarship= Label (StudentStatusFrame, font =('arial', 12, 'bold'), text='Scholarship', bd =6, justify=LEFT)
            self.lblScholarship.grid( row=4, column=0, sticky= W)
            self.cboScholarship = ttk.Combobox (StudentStatusFrame, textvariable = self.Scholarship, width= 10,
                                           font =('arial', 12, 'bold' ), state='randomly')
            self.cboScholarship['value' ] = ('No','Yes')
            self.cboScholarship.current (0)
            self.cboScholarship.grid (row=4, column=1, pady=8)

            #================ DEGREE FRAME =================#

            self.lblBA= Label (DegreeFrame, font =('arial', 12, 'bold'), text='Bachelor of Arts', bd =6, justify=LEFT)
            self.lblBA.grid( row=0, column=0, sticky= W)
            self.SpBA = Spinbox (DegreeFrame, from_ =0, to =20, textvariable = self.BA, width= 8, font =('arial', 12, 'bold' ))
            self.SpBA.grid (row=0, column=1, pady=9)

            self.lblBsc= Label (DegreeFrame, font =('arial', 12, 'bold'), text='Bachelor of Science', bd =6, justify=LEFT)
            self.lblBsc.grid( row=1, column=0, sticky= W)
            self.SpBsc = Spinbox (DegreeFrame, from_ =0, to =20, textvariable = self.Bsc, width= 8, font =('arial', 12, 'bold' ))
            self.SpBsc.grid (row=1, column=1, pady=9)

            self.lblMA= Label (DegreeFrame, font =('arial', 12, 'bold'), text='Master of Arts', bd =6, justify=LEFT)
            self.lblMA.grid( row=2, column=0, sticky= W)
            self.SpMA = Spinbox (DegreeFrame, from_ =0, to =20, textvariable = self.MA, width= 8, font =('arial', 12, 'bold' ))
            self.SpMA.grid (row=2, column=1, pady=9)

            self.lblMsc= Label (DegreeFrame, font =('arial', 12, 'bold'), text='Master of Science', bd =6, justify=LEFT)
            self.lblMsc.grid( row=3, column=0, sticky= W)
            self.SpMsc = Spinbox (DegreeFrame, from_ =0, to =20, textvariable = self.Msc, width= 8, font =('arial', 12, 'bold' ))
            self.SpMsc.grid (row=3, column=1, pady=9)

            self.lblPhd= Label (DegreeFrame, font =('arial', 12, 'bold'), text='Doctor of Philosophy', bd =6, justify=LEFT)
            self.lblPhd.grid( row=4, column=0, sticky= W)
            self.SpPhd = Spinbox (DegreeFrame, from_ =0, to =20, textvariable = self.Phd, width= 8, font =('arial', 12, 'bold' ))
            self.SpPhd.grid (row=4, column=1, pady=9)

            #================ CALENDAR =================#
            def getSelectedDate():
                  nowDate = cal.get_date()
                  self.ResultDate.set(nowDate)
                  AddModuleScore()

            cal = Calendar(CalendarFrame, selectmode ="day", date_pattern = 'dd-mm-yyyy', font=('arial',12, 'bold'), padx=10)
            cal.grid(row=0, column=0)

            #================ UNIT-NO =================#

            self.lblNo= Label (UnitNo, font =('arial', 12, 'bold'), text='No', padx=2, pady=4)
            self.lblNo.grid( row=0, column=0, sticky= W)

            self.lbl1= Label (UnitNo, font =('arial', 12, 'bold'), text='1', padx=2, pady=2)
            self.lbl1.grid( row=1, column=0, sticky= W)

            self.lbl2= Label (UnitNo, font =('arial', 12, 'bold'), text='2', padx=2, pady=2)
            self.lbl2.grid( row=2, column=0, sticky= W)

            self.lbl3= Label (UnitNo, font =('arial', 12, 'bold'), text='3', padx=2, pady=2)
            self.lbl3.grid( row=3, column=0, sticky= W)

            self.lbl4= Label (UnitNo, font =('arial', 12, 'bold'), text='4', padx=2, pady=2)
            self.lbl4.grid( row=4, column=0, sticky= W)

            self.lbl5= Label (UnitNo, font =('arial', 12, 'bold'), text='5', padx=2, pady=2)
            self.lbl5.grid( row=5, column=0, sticky= W)

            self.lbl6= Label (UnitNo, font =('arial', 12, 'bold'), text='6', padx=2, pady=2)
            self.lbl6.grid( row=6, column=0, sticky= W)

            self.lbl7= Label (UnitNo, font =('arial', 12, 'bold'), text='7', padx=2, pady=2)
            self.lbl7.grid( row=7, column=0, sticky= W)

            self.lbl8= Label (UnitNo, font =('arial', 12, 'bold'), text='8', padx=2, pady=3)
            self.lbl8.grid( row=8, column=0, sticky= W)

            #================ UNIT SUBJECT FRAME =================#

            self.lblSelectUnit= Label (UnitSubject, font =('arial', 12, 'bold'), text='Select Subject', padx=2, pady=0)
            self.lblSelectUnit.grid( row=0, column=0, sticky= W)

            self.cboSubject1 = ttk.Combobox (UnitSubject, textvariable = self.Subject1, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject1['value' ] = ('','Event Driven Pro')
            self.cboSubject1.current (0)
            self.cboSubject1.grid (row=1, column=0, padx=2, pady=1)
            self.cboSubject1.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject2 = ttk.Combobox (UnitSubject, textvariable = self.Subject2, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject2['value' ] = ('','Object Oriented', 'Spreadsheet')
            self.cboSubject2.current (0)
            self.cboSubject2.grid (row=2, column=0, padx=2, pady=1)
            self.cboSubject2.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject3 = ttk.Combobox (UnitSubject, textvariable = self.Subject3, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject3['value' ] = ('','System Analytics', 'Info Tech')
            self.cboSubject3.current (0)
            self.cboSubject3.grid (row=3, column=0, padx=2, pady=1)
            self.cboSubject3.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject4 = ttk.Combobox (UnitSubject, textvariable = self.Subject4, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject4['value' ] = ('','Digital Graphics', 'English')
            self.cboSubject4.current (0)
            self.cboSubject4.grid (row=4, column=0, padx=2, pady=1)
            self.cboSubject4.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject5 = ttk.Combobox (UnitSubject, textvariable = self.Subject5, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject5['value' ] = ('','Games', 'Animation')
            self.cboSubject5.current (0)
            self.cboSubject5.grid (row=5, column=0, padx=2, pady=1)
            self.cboSubject5.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject6 = ttk.Combobox (UnitSubject, textvariable = self.Subject6, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject6['value' ] = ('','Database', 'Maths')
            self.cboSubject6.current (0)
            self.cboSubject6.grid (row=6, column=0, padx=2, pady=1)
            self.cboSubject6.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject7 = ttk.Combobox (UnitSubject, textvariable = self.Subject7, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject7['value' ] = ('','Add Maths', 'Physics')
            self.cboSubject7.current (0)
            self.cboSubject7.grid (row=7, column=0, padx=2, pady=1)
            self.cboSubject7.bind('<<ComboboxSelected>>', setSubject)

            self.cboSubject8 = ttk.Combobox (UnitSubject, textvariable = self.Subject8, width= 20, font =('arial', 12, 'bold' ),state='randomly', justify=LEFT)
            self.cboSubject8['value' ] = ('', 'Data Science')
            self.cboSubject8.current (0)
            self.cboSubject8.grid (row=8, column=0, padx=2, pady=1)
            self.cboSubject8.bind('<<ComboboxSelected>>', setSubject)

            


            #================ UNIT SCORE FRAME =================#

            self.lblSUnit= Label (UnitScore, font =('arial', 12, 'bold'), text='Score', padx=2)
            self.lblSUnit.grid( row=0, column=0, sticky= W)

            self.txt1 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module1, state=DISABLED)
            self.txt1.grid( row=1, column=0, padx=2, pady=2)

            self.txt2 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module2, state=DISABLED)
            self.txt2.grid( row=2, column=0, padx=2, pady=2)

            self.txt3 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module3, state=DISABLED)
            self.txt3.grid( row=3, column=0, padx=2, pady=2)

            self.txt4 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module4, state=DISABLED)
            self.txt4.grid( row=4, column=0, padx=2, pady=2)

            self.txt5 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module5, state=DISABLED)
            self.txt5.grid( row=5, column=0, padx=2, pady=2)

            self.txt6 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module6, state=DISABLED)
            self.txt6.grid( row=6, column=0, padx=2, pady=2)

            self.txt7 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module7, state=DISABLED)
            self.txt7.grid( row=7, column=0, padx=2, pady=2)

            self.txt8 = Entry (UnitScore, font =('arial', 12, 'bold'), bd=1, width=5, textvariable = self.Module8, state=DISABLED)
            self.txt8.grid( row=8, column=0, padx=2, pady=2)

            #================ TOTAL-SCORE =================#

            self.lblTotalScore = Label (ResultsFrameLeft, font =('arial', 12, 'bold'), text='Total Score', justify=LEFT)
            self.lblTotalScore.grid( row=0, column=0, sticky= W)
            self.txtTotalScore = Entry (ResultsFrameLeft, font =('arial', 12, 'bold'), width=23, textvariable = self.TotalScore)
            self.txtTotalScore.grid( row=0, column=1)

            self.lblRanking = Label (ResultsFrameLeft, font =('arial', 12, 'bold'), text='Ranking', justify=LEFT)
            self.lblRanking.grid( row=1, column=0, sticky= W)
            self.txtRanking = Entry (ResultsFrameLeft, font =('arial', 12, 'bold'), width=23, textvariable = self.Ranking)
            self.txtRanking.grid( row=1, column=1)

            self.lblDateRanked = Label (ResultsFrameLeft, font =('arial', 12, 'bold'), text='Date', justify=LEFT)
            self.lblDateRanked.grid( row=2, column=0, sticky= W)
            self.txtDateRanked = Entry (ResultsFrameLeft, font =('arial', 12, 'bold'), width=23, textvariable = self.ResultDate)
            self.txtDateRanked.grid( row=2, column=1)

            #================ SUBJECTS =================#
            
            self.lblDataScience= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Data Science', bd=7)
            self.lblDataScience.grid( row=0, column=0, sticky= W)
            self.cboDataScience = ttk.Combobox (TopFrame12b, textvariable = self.DataScience, font =('arial', 12, 'bold' ),state='randomly')
            self.cboDataScience['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboDataScience.current (0)
            self.cboDataScience.grid (row=0, column=1)

            self.lblEventDrivenPro= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Event Driven Pro', bd=7)
            self.lblEventDrivenPro.grid( row=1, column=0, sticky= W)
            self.cboEventDrivenPro = ttk.Combobox (TopFrame12b, textvariable = self.EventDrivenPro, font =('arial', 12, 'bold' ),state='randomly')
            self.cboEventDrivenPro['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboEventDrivenPro.current (0)
            self.cboEventDrivenPro.grid (row=1, column=1)

            self.lblObjectOriented= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Object Oriented P', bd=7)
            self.lblObjectOriented.grid( row=2, column=0, sticky= W)
            self.cboObjectOriented = ttk.Combobox (TopFrame12b, textvariable = self.ObjectOriented, font =('arial', 12, 'bold' ),state='randomly')
            self.cboObjectOriented['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboObjectOriented.current (0)
            self.cboObjectOriented.grid (row=2, column=1)

            self.lblSpreadsheet= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Spread Sheet', bd=7)
            self.lblSpreadsheet.grid( row=3, column=0, sticky= W)
            self.cboSpreadsheet = ttk.Combobox (TopFrame12b, textvariable = self.Spreadsheet, font =('arial', 12, 'bold' ),state='randomly')
            self.cboSpreadsheet['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboSpreadsheet.current (0)
            self.cboSpreadsheet.grid (row=3, column=1)

            self.lblSystemAnalytics= Label (TopFrame12b, font =('arial', 12, 'bold'), text='System Analytics', bd=7)
            self.lblSystemAnalytics.grid( row=4, column=0, sticky= W)
            self.cboSystemAnalytics = ttk.Combobox (TopFrame12b, textvariable = self.SystemAnalytics, font =('arial', 12, 'bold' ),state='randomly')
            self.cboSystemAnalytics['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboSystemAnalytics.current (0)
            self.cboSystemAnalytics.grid (row=4, column=1)

            self.lblInfoTech= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Info Tech', bd=7)
            self.lblInfoTech.grid( row=5, column=0, sticky= W)
            self.cboInfoTech = ttk.Combobox (TopFrame12b, textvariable = self.InfoTech, font =('arial', 12, 'bold'),state='randomly')
            self.cboInfoTech['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboInfoTech.current (0)
            self.cboInfoTech.grid (row=5, column=1)

            self.lblDigitalGraphics= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Digital Graphics', bd=7)
            self.lblDigitalGraphics.grid( row=6, column=0, sticky= W)
            self.cboDigitalGraphics = ttk.Combobox (TopFrame12b, textvariable = self.DigitalGraphics, font =('arial', 12, 'bold'),state='randomly')
            self.cboDigitalGraphics['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboDigitalGraphics.current (0)
            self.cboDigitalGraphics.grid (row=6, column=1)

            self.lblEnglish= Label (TopFrame12b, font =('arial', 12, 'bold'), text='English', bd=7)
            self.lblEnglish.grid( row=7, column=0, sticky= W)
            self.cboEnglish = ttk.Combobox (TopFrame12b, textvariable = self.English, font =('arial', 12, 'bold'),state='randomly')
            self.cboEnglish['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboEnglish.current (0)
            self.cboEnglish.grid (row=7, column=1)

            self.lblGames= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Games', bd=7)
            self.lblGames.grid( row=8, column=0, sticky= W)
            self.cboGames = ttk.Combobox (TopFrame12b, textvariable = self.Games, font =('arial', 12, 'bold'),state='randomly')
            self.cboGames['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboGames.current (0)
            self.cboGames.grid (row=8, column=1)

            self.lblAnimation= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Animation', bd=7)
            self.lblAnimation.grid( row=9, column=0, sticky= W)
            self.cboAnimation = ttk.Combobox (TopFrame12b, textvariable = self.Animation, font =('arial', 12, 'bold'),state='randomly')
            self.cboAnimation['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboAnimation.current (0)
            self.cboAnimation.grid (row=9, column=1)

            self.lblDatabase= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Database', bd=7)
            self.lblDatabase.grid( row=10, column=0, sticky= W)
            self.cboDatabase = ttk.Combobox (TopFrame12b, textvariable = self.Database, font =('arial', 12, 'bold'),state='randomly')
            self.cboDatabase['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboDatabase.current (0)
            self.cboDatabase.grid (row=10, column=1)

            self.lblMaths= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Maths', bd=7)
            self.lblMaths.grid( row=11, column=0, sticky= W)
            self.cboMaths = ttk.Combobox (TopFrame12b, textvariable = self.Maths, font =('arial', 12, 'bold'),state='randomly')
            self.cboMaths['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboMaths.current (0)
            self.cboMaths.grid (row=11, column=1)

            self.lblAddMaths= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Add Maths', bd=7)
            self.lblAddMaths.grid( row=12, column=0, sticky= W)
            self.cboAddMaths = ttk.Combobox (TopFrame12b, textvariable = self.AddMaths, font =('arial', 12, 'bold'),state='randomly')
            self.cboAddMaths['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboAddMaths.current (0)
            self.cboAddMaths.grid (row=12, column=1)

            self.lblPhysics= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Physics', bd=7)
            self.lblPhysics.grid( row=13, column=0, sticky= W)
            self.cboPhysics = ttk.Combobox (TopFrame12b, textvariable = self.Physics, font =('arial', 12, 'bold'),state='randomly')
            self.cboPhysics['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboPhysics.current (0)
            self.cboPhysics.grid (row=13, column=1)

            """ self.lblMedia= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Media', bd=7)
            self.lblMedia.grid( row=14, column=0, sticky= W)
            self.cboMedia = ttk.Combobox (TopFrame12b, textvariable = self.Media, font =('arial', 12, 'bold'),state='randomly')
            self.cboMedia['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboMedia.current (0)
            self.cboMedia.grid (row=14, column=1)

            self.lblGraphics= Label (TopFrame12b, font =('arial', 12, 'bold'), text='Graphics', bd=7)
            self.lblGraphics.grid( row=15, column=0, sticky= W)
            self.cboGraphics = ttk.Combobox (TopFrame12b, textvariable = self.Graphics, font =('arial', 12, 'bold'),state='randomly')
            self.cboGraphics['value' ] = ('No','Core Unit', 'Yes', 'Complete')
            self.cboGraphics.current (0)
            self.cboGraphics.grid (row=15, column=1) """

            #================ TITLE =================#

            self.lblTitle= Label (TopFrame11, font =('arial', 40, 'bold'), text='STUDENT DETAILS MANAGEMENT SYSTEM', bd=5, justify=CENTER)
            self.lblTitle.grid( row=0, column=0, padx=73)

            #================ SCROLL-BAR =================#
            scroll_x = Scrollbar(TopFrame12a, orient=HORIZONTAL)
            scroll_y = Scrollbar(TopFrame12a, orient=VERTICAL)
            
            self.Student_Record = ttk.Treeview(TopFrame12a, height=22, columns=("studentid", "firstname", "surname" , "address", "postcode", "gender", "dob", "mobile", "email", "parent"), xscrollcommand = scroll_x.set,  yscrollcommand = scroll_y.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

             #================ HEADINGS-TREEVIEW =================#

            self.Student_Record.heading("studentid", text = "Student ID")
            self.Student_Record.heading("firstname", text = "Firstname")
            self.Student_Record.heading("surname", text = "Surname")
            self.Student_Record.heading("address", text = "Address")
            self.Student_Record.heading("postcode", text = "Postcode")
            self.Student_Record.heading("gender", text = "Gender")
            self.Student_Record.heading("dob", text = "DOB")
            self.Student_Record.heading("mobile", text = "Mobile")
            self.Student_Record.heading("email", text = "Email")
            self.Student_Record.heading("parent", text = "Parent/Guidian")

            self.Student_Record['show'] ='headings'

            self.Student_Record.column("studentid", width=90)
            self.Student_Record.column("firstname", width=90)
            self.Student_Record.column("surname", width=70)
            self.Student_Record.column("address", width=200)
            self.Student_Record.column("postcode", width=70)
            self.Student_Record.column("gender", width=70)
            self.Student_Record.column("dob", width=70)
            self.Student_Record.column("mobile", width=70)
            self.Student_Record.column("email", width=70)
            self.Student_Record.column("parent", width=70)

            self.Student_Record.pack(fill = BOTH, expand =1)
            self.Student_Record.bind("<ButtonRelease-1>", stuInfo)
            DisplayData()

            


            #================ BUTTON FRAME =================#

            self.btnAddNewsStudent = Button (ButtonFrame, pady=1, padx=1, font=('arial', 12, 'bold'), bg= "cadetblue", width=8, text="ADDNEW", command = addData) .grid(row=0, column=1, padx=1, pady=19)

            self.btnAddUpdate = Button (ButtonFrame, pady=1,  padx=1, font=('arial', 12, 'bold'), bg= "cadetblue", width=8, text="UPDATE", command=update) .grid(row=0, column=2, padx=1,  pady=19)

            self.btnAddDelete = Button (ButtonFrame, pady=1, padx=1, font=('arial', 12, 'bold'), bg= "cadetblue", width=8, text="DELETE", command=deletedb) .grid(row=0, column=3, padx=1, pady=19)

            self.btnReset = Button (ButtonFrame, pady=1,  padx=1, font=('arial', 12, 'bold'), bg= "cadetblue", width=8, text="RESET", command=Reset) .grid(row=0, column=4, padx=1, pady=19)

            self.btnResult = Button (ButtonFrame, pady=1, padx=1, font=('arial', 12, 'bold'), bg= "cadetblue", width=8, text="RESULT", command=getSelectedDate) .grid(row=0, column=5, padx=2, pady=19)

            self.btnExit = Button (ButtonFrame, pady=1, padx=1,  font=('arial', 12, 'bold'), bg= "cadetblue", width=8, text="EXIT", command=iExit) .grid(row=0, column=6, padx=1, pady=19) 
      






























            

            


if  __name__== '__main__':
      root =Tk ()
      application = studentRecords( root )
      root.mainloop()






      
      


            
