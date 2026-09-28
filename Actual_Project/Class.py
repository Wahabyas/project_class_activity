
class Student:
    def __init__(self,Std_id,Fullname,Course):
        self.Std_id = Std_id
        self.Fullname = Fullname
        self.Course = Course

    # Getter
    def get_Std_info(self):
        return f"Student ID  is {self.Std_id} \n  Fullname is {self.Fullname} \n Course is {self.Course}"
    # Setter
    def set_Student_info(self,Std_id,Fullname,Course):
        self.Std_id = Std_id
        self.Fullname = Fullname
        self.Course = Course
        return self