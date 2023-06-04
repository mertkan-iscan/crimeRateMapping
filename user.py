class User:
    def __init__(self, user_id, name, surname, password):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.password = password

        #add user to user array


    def display(self):
        print(f"Title: {self.user_id}")
        print(f"Author: {self.name}")
        print(f"Content: {self.surname}")
        print(f"Type: {self.password}")


    #def check_user():
    

#class AdminUser(User):
#
#    def create_report():
#
#    def delete_report():
#
#    def create_report():
#
#
#class DepartmentUser(User):
#
#
#
#class DefaultUser(User):
#
#    def create_report():
