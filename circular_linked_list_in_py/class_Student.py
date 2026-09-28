array_std  = [ ]

class Student_class:
    def __init__(self,fullname,course,pointer_left,pointer_right):
        self.fullname = fullname
        self.course = course
        self.pointer_left = pointer_left if pointer_left is not None else None
        self.pointer_right = pointer_right if pointer_right is not None else None
    # def set_student(self):
    #     array_std.append(self.fullname)

    # def __str__(self):
    #     return f"student name is"
    # # def is_Print():
    # #     if 
        
        
        