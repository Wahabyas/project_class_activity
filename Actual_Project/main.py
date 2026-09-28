import Class
import Helper
Student_Array = []




Is_ProcessStop = None
currnet_student_data = None


    
    
print("Note!!! : \n Press x if insert the data \n Press y to go to a particular Student data (By position) \n Press W to Stop the Process \n ")


while Is_ProcessStop is None:
     if len(Student_Array) == 0:
        print("No Data Yet \n")
     else:
        for i in range(len(Student_Array)):
            print(i)
        print("\n")

     Action = str(input( "What action Do you want  to commit : "))
     if Action == "w":
         Is_ProcessStop = 1
     elif Action == "x":
        action_x_is_Continune = None
        while action_x_is_Continune is None:
            print("You took the action x \n")
    
            Std_id = str(input(f"Insert the Std_id of the Std_id : "))
            student_fullname = str(input(f"Insert the Fullname of the student : "))
            Course = str(input(f"Insert the Course of the Course : "))

            newStudent = Class.Student(None,None,None)
            newStudent.set_Student_info(Std_id,student_fullname,Course)
            x_Action_continuation =  str(input("Data insert Succesfully Would You like to insert another? Y/N")).upper()
            if x_Action_continuation == "Y":
                action_x_is_Continune = 1
            elif x_Action_continuation == "N":
                action_x_is_Continune = None

            
        
     elif Action == "y":
        print("You took the action y")
     else:
         print("Out of Bound please Try again \n")

print("The Proccess has ended :)")

