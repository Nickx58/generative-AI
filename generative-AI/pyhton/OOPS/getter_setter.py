class Student:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self,new_name):
        self._name = new_name


student = Student("NIck")
print(student.name)
student.name = "Nikhil"
print(student.name)
