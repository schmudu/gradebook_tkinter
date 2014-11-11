import tkinter as Tk
from src.view.custom_dialog import CustomDialog

class NewCourseDialog(CustomDialog):
  ENTRY_COURSE_NAME_DEFAULT = "<Enter Course Name>"

  def body(self, master):
    label_course_name = Tk.Label(master, text="Course Name")
    label_course_name.grid(row=0, column=0)

    self.course_name_var = Tk.StringVar()
    entry_course_name = Tk.Entry(master, textvariable=self.course_name_var)
    entry_course_name.grid(row=0, column=1)
    self.course_name_var.set(NewCourseDialog.ENTRY_COURSE_NAME_DEFAULT)
