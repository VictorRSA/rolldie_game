# Created:ON:29 -October-2020
# Created by:Victo Nkuna
# E-mail:victor.nkuna@yahoo.com


""""In a typical uinversity ,courses are measured in terms of credit hours ...
...and grade point averages are calculated on a 4 point scale,
where an "A" is 4 points,a "B" ,is a 3 point scale etc,
Grade point averages are generally computed using  kwality points,if a clss is worth 3 credit hours and the student gets an "A"
  then he or she earns 3(4)=12 kwality points,to compute GPA,we devide the total kwality points by the number of credits completed
  """
from nltk import infile

""""suppose we have a data file that contains student grade information
Each line of the file consits of a student's name,credit hours,and kwality points,these three values are separated by a Tab character
example:
Adams,Henry  127  228
Computewell,Susan  100  400
DibbleBit Denny 18 41.5
Jones Jim 48.5   155
Smith , Frank 37 125.33

Task our job is to write a program that reads through the file to find the student with best GPA and print out his/her name
credit hours ,and GPA
"""


class Student:
    def __init__(self, name, hours, quality_points):
        self.name = name
        self.hours = hours
        self.quality_points = quality_points

    """"These three methods will allows us to get the information about the class,Student"""

    def get_name(self):
        return self.name

    def get_hours(self):
        return self.hours

    def get_points(self):
        return self.quality_points

    def gpa(self):
        """"these method compute the gpa"""
        return self.quality_points / self.hours


("\n"
 "   After creating the  method of  finding the gpa,one can now attach the problem of finding the best students\n"
 "   look throught the student data file one by one and keep tracking the best student seen o far\n"
 "   ")


def make_student_info(info_storage, self=None):
    """
    make_student_info is a tab-separated line :name,hours,self.kwality points
    :param info_storage:
    :return:
    :return a corresponding student object
    """
    self.name, self.hours, self.quality_points = info_storage.split("\t")
    return Student(self.name, self.hours, self.quality_points)

    def main():
        filename = input("Enter the name of the grade fle: ")
        infile = open(filename, "r")
        best = make_student_info(infile.readline())

    for line in infile:
        s = make_student_info(line)
        if s.gpa() > best.gpa():
            best = s
            infile.close()
            print("The best student is:", best.get_name)
            print("hours:", best.get_hours)
            print("GPA:", best.gpa)
    main()
    # if __name__ == '__main__':
    #     main()

#
# if __name__ == "__main__":
#     main()

# astudent = Student("Adams Henry",127,128)
# print(astudent.get_hours())
