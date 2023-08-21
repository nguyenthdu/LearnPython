class Employee:
        # Khai báo properties và gán giá trị cho chúng
    def __init__(self,ID = None, salary = 0, department = None):
        self.ID = ID
        self.salary = salary
        self.department  = department


'''
# Tạo một object của class Employee với các tham số mặc định
steve = Employee()
# Tạo một object của class Employee với tham số của chúng ta
mark = Employee("3789",2500,"Project Manager")

print("Steve:\n\tID :",steve.ID)
print("Mark:\n\tID :",mark.ID)
'''
class Player:
    team_name  = 'Liverpool FC'# class variable
   # former_teams = [] # tất cả các object đều nhận được giá trị
    def __init__(self,name):
        self.name = name# instance variable
        self.former_teams = [] # mỗi object chỉ nhận được giá trị truyền vào nó
p1 = Player('Sala')
p2 = Player('Mane')
# Dùng built-in method `append` để thêm giá trị vào variable `former_teams`
p1.former_teams.append('Samthompton')
p2.former_teams.append('Leeds')
# In properties của các objects
print("Name:", p1.name)
print("Team Name:", p1.team_name)
print(p1.former_teams)
print("Name:", p2.name)
print("Team Name:", p2.team_name)
print(p2.former_teams)
# ví dụ khác
class Player1:
    team_name = 'Manchester City' # class variables
    team_members = [] # class variables

    def __init__(self, name):
        self.name = name # instance variables
        self.former_teams = [] # instance variables
        
        # sử dụng method append để mỗi lần tạo ra object Player 
        # thì sẽ tự thêm `name` của player đó vào class variable team_members 
        self.team_members.append(self.name) 


p1 = Player1('David Silva')
p2 = Player1('Yaya Toure')

print("Team Name:", p1.team_name)
print("Team Members:")
print(p1.team_members)
print("")
print("Name:", p2.name)
print("Team Members:")
print(p2.team_members)
