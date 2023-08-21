"""
Có 3 loại method trong Python:

Instance methods
Class methods
Static methods
"""
#TODO: Instance Method - self
class Employee:
    def __init__(self,ID = None, department = None):
        self.ID = ID
        self.department = department

# tao 1 employee
emp1 = Employee("Tran van A", "TTT")
#Thì Python sẽ convert giúp chúng ta thành:
#Employee.__init__(employee1, "Furaudorin", "FAA")
#Và bên trong initializer sẽ thực thi như sau:
#employee1.ID = "Furaudorin"
#employee1.department = "FAA"


#TODO: Class Method
"""
Để khai báo một class method, chúng ta sử dụng @classmethod decorator. cls parameter được sử để refer tới class cũng như chúng ta sử dụng self để refer tới object của class. Bạn cũng có thể sử dụng bất cứ tên nào để thay thế cls, nhưng vì quy ước (convention), chúng ta sẽ sử dụng cls.
"""
class Player:
    team_name = 'Manchester City'  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

    # define class method get_team_name sử dụng @classmethod decorator
    @classmethod
    def get_team_name(cls):
        return cls.team_name


print(Player.get_team_name())

#TODO: Static methods
"""
Static method là method được dùng chỉ giới hạn ở phạm vi class. Chúng không tương tác với class variable hay instance variable
Để khai báo static method, chúng ta sử dụng @staticmethod decorator. Vì nó không được sử dụng để tham chiếu đến object hay class nên chúng ta không sử dụng self hay cls argument. Static methods không biết bất cứ thứ gì về state của class.
"""
class Player:
    team_name = 'Manchester City'  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

    @staticmethod
    def demo():
        print("I am a static method.")


p1 = Player('lol')
p1.demo()
Player.demo()
# ví dụ
class BodyInfo:

    @staticmethod
    def bmi(weight, height):
        return weight / (height**2)

weight = 75
height = 1.8
print(BodyInfo.bmi(weight, height))

#TODO: Access Modifiers 
"""
Trong Python, tất cả attributes mặc định là public. Nếu chúng ta muốn chỉ định một method hay variables nào đó không nên được coi là public, chúng ta phải khai báo nó là private.
"""
# public 
class Employee:
    def __init__(self, ID, salary):
        # các properties này đều là public
        self.ID = ID
        self.salary = salary

    # method này là public
    def display_id(self):
        print("ID:", self.ID)


steve = Employee(3789, 2500)
steve.display_id()
print(steve.salary)
#private 
'''
Nhưng trong Python, không có sự tồn tại của "private". Tuy nhiên, một quy ước đang được hầu hết các developer sử dụng là chúng ta có thể tạo private attributes bằng cách sử dụng tiền tố (prefix) __.
'''
#Phân biệt giữa single leading underscore _ và double leading underscores __ trong Python
class MyClass():
    def __init__(self):
        self.__superprivate = "Hello"
        self._semiprivate = ", world!"
# truy cập private method
mc = MyClass()
print(mc._semiprivate)#->, world!
print(mc.__superprivate)#-> error, là private nên không truy cập ngoài class được

class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary là một private property

    def display_salary(self):  # display_salary là một public method
        print("Salary:", self.__salary)

    def __display_id(self):  # display_id là một private method
        print("ID:", self.ID)


steve = Employee(3789, 2500)
steve.display_salary()
steve.__display_id()  # dòng này sẽ gây lỗi
#Truy cập private attributes trong main code
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary là một private property

steve = Employee(3789, 2500)
print(steve._Employee__salary)  # truy cập private property
"""
TODO: Information Hiding trong Python
Information hiding là một khái niệm thiết yếu trong oop. Nói một cách đơn giản thì để đảm bảo rằng dữ liệu được truy cập và sử dụng đúng mục đích và an toàn (bảo mật) thì chúng ta sẽ giấu đi các hoạt động bên trong class và chỉ cung cấp một giao diện (interface) mà qua đó thế giới bên ngoài có thể tương tác với class mà không cần biết điều gì đang xảy ra bên trong.

Data hiding có thể chia làm 2 phần chính:

Encapsulation (Tính đóng gói)
Abstraction (Tính trừu tượng)
"""
#Encapsulation 
#Getter and Setters
class User:
    def __init__(self,username = None):
        self.__username = username
    
    def set_username(self, x):
        self.__username = x

    def get_username(self):
        return (self.__username)
    
steve = User("Ronaldo")
print('Before setting: ', steve.get_username())
steve.set_username('Messi')
print('After setting: ', steve.get_username())
#TODO: @property decorator
"""
Sau khi tìm hiểu cách Python sử dụng getter setter thì... quên những gì bạn vừa đọc đi, đã có nhiều thảo luận về việc dùng getter, setter trong Python và đa số người sử dụng Python đều không sử dụng nó. Tóm tắt là nó rối, nó tốn tài nguyên, và Python được sinh ra để trở thành ngôn ngữ lập trình dễ sử dụng cho con người.

Thay vào đó họ sử dụng @property decorator nếu như muốn "làm gì đó private" với attributes trong class. Trong bài học của khóa học CS50P họ cũng sử dụng decorator này.

Giờ tìm hiểu về nó nhé.
"""
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.__name = name
        self.__house = house

    def __str__(self):
        return f"{self.__name} from {self.__house}"

    # Getter cho house
    # Hãy chắc chắn rằng tên của getter và setter trùng với tên của property
    @property
    def house(self):
        return self.__house

    # Setter cho house
    # Hãy chắc chắn rằng tên của getter và setter trùng với tên của property
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.__house = house
        
    
def main():
    # Ở đây mình sẽ nhập name là Abre, house là: Hufflepuff
    student = get_student()
    print(f"Student info: {student}")
    print(student)
    # Truy cập house của student
    print(f"House of student: {student.house}")
    # Thay đổi giá trị của house của student thành Ravenclaw
    student.house = "Ravenclaw"
    # In ra thông tin student sau khi đổi
    print(f"Student info after change house: {student}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
