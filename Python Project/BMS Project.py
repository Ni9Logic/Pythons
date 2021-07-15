class SignInPage:
    userchoice = 1

    def login(self):
        print("\t\t\tWelcome to SUNUDSS KA BANK! HAHAHA MERA BANK")
        print("\t\t\t1 --> Sign in as admin")
        print("\t\t\t2 --> Sign in as user")
        print("\t\t\t3 --> Create a New Account")
        self.user_choice = int(input("\t\t\tEnter: "))
        if self.user_choice == 0 or self.user_choice > 3:
            while self.user_choice == 0 or self.user_choice > 3:
                print("\t\t\tYou've Entered Incorrect Statement.")
                self.user_choice = input("\t\t\tEnter Again: ")
                self.user_choice = int(self.user_choice)
        return self.user_choice


class Admin(SignInPage):
    username = "0"
    password = "0"
    flag = False
    signin = SignInPage()

    def adminlogin(username, password):
        username = input("\t\t\tEnter Username: ")
        password = input("\t\t\tEnter Password: ")
        if username == "admin" and password == "admin":
            print("\t\t\tLOGGED")
            flag = True
        else:
            print("\t\t\tYou've entered incorrect Credentionals")
            print("\t\t\tForcing session (logged out)")
            flag = False

    def adminmenu(self):
        print("Hello")


def main():
    end = 'y'
    while end == 'y':
        object = Admin()
        object.login()
        if object.user_choice == 1:
            username = "0"
            password = "0"
            Admin.adminlogin(username, password)
            if Admin.flag == True:
                Admin.adminmenu()
            else:
                continue
    return 0


main()
