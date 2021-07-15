import os
import msvcrt as m


class SignInPage:
    userchoice = 1
    admin_name = "0"
    admin_pass = "0"
    Logged = False

    def login(self):
        print(
            "\t\t\tWelcome to \u001b[1;31mSUNUDSS KA BANK! HAHAHA MERA BANK\u001b[1;0m"
        )
        print("\t\t\t1 \u001b[1;31m-->\u001b[1;0m Sign in as admin")
        print("\t\t\t2 \u001b[1;31m-->\u001b[1;0m Sign in as user")
        print("\t\t\t3 \u001b[1;31m-->\u001b[1;0m Create a New Account")
        print("\t\t\t4 \u001b[1;31m-->\u001b[1;0m Exit")
        self.user_choice = int(input("\t\t\tEnter: "))
        if self.user_choice == 0 or self.user_choice > 4:
            while self.user_choice == 0 or self.user_choice > 4:
                os.system("cls||clear")
                print("\t\t\tYou've Entered Incorrect Statement.")
                self.user_choice = input("\t\t\tEnter Again: ")
                self.user_choice = int(self.user_choice)
        return self.user_choice

    def adminlogin(self):
        os.system("cls||clear")
        self.admin_name = input("\t\t\tEnter \u001b[1;31mUsername\u001b[1;0m: ")
        self.admin_pass = input("\t\t\tEnter \u001b[1;31mPassword\u001b[1;0m: ")
        if self.admin_name == "admin" and self.admin_pass == "admin":
            os.system("cls||clear")
            print("\n\t\t\tYou've Successfully logged in as an administrator...")
            SignInPage.Logged = True
        else:
            os.system("cls||clear")
            print(
                "\t\t\t\u001b[1;31mNOTE:\u001b[1;0m You've entered incorrect \u001b[1;31mCredentials\u001b[1;0m"
            )
            print("\t\t\tForcing session \u001b[1;31m(logged out)\u001b[1;0m\n")
            print("\t\t\tPress Any Key to continue...")
            m.getch()
            SignInPage.Logged = False


class NewUser:
    new_user_name = "0"
    new_user_pass = "0"
    new_user_Account_Type = "0"
    new_user_BankBal = "0"
    new_user_Account_ID = "0"

    def new_user_createaccount(self):
        os.system("cls||clear")
        with open("usernames.txt", "a") as file:
            self.new_user_name = input(
                "\t\t\tEnter\u001b[1;31m Name\u001b[1;0m For User: "
            )
            file.write(self.new_user_name)
            file.write("\n")
        with open("passwords.txt", "a") as file:
            self.new_user_pass = input(
                "\t\t\tEnter\u001b[1;31m Password\u001b[1;0m For User: "
            )
            file.write(self.new_user_pass)
            file.write("\n")
        with open("Account_Type.txt", "a") as file:
            self.new_user_Account_Type = input(
                "\t\t\tEnter\u001b[1;31m Account_Type\u001b[1;0m For User: "
            )
            file.write(self.new_user_Account_Type)
            file.write("\n")
        with open("BankBal.txt", "a") as file:
            self.new_user_Account_Type = input(
                "\t\t\tEnter\u001b[1;31m InitialDeposit\u001b[1;0m For User: "
            )
            file.write(self.new_user_BankBal)
            file.write("\n")
        with open("Account_ID.txt", "a") as file:
            self.new_user_Account_ID = input(
                "\t\t\tEnter\u001b[1;31m Account_ID\u001b[1;0m For User: "
            )
            file.write(self.new_user_Account_ID)
            file.write("\n")
        print(
            "\t\t\tAccount \u001b[1;31mSuccessfully Created\u001b[1;0m\n\t\t\tPress Any Key to continue"
        )
        m.getch()


class Admin(SignInPage, NewUser):
    username = "0"
    password = "0"
    admin_choice = 0
    admin_log = True
    signin = SignInPage()

    def adminmenu(self):
        end = "y"
        while end == "y":
            os.system("cls||clear")
            print("\t\t\t1. Delete Account")  # Allows admin to delete an account
            # Allows admin to view) all the list
            print("\t\t\t2. Accounts lists")
            # Allows admin to view specific account's detials.
            print("\t\t\t3. Specific Accounts Details")
            # Allows admin to modify an account
            print("\t\t\t4. Modify an Account")
            print("\t\t\t5. Logout")  # Logs out
            print("\t\t\t6. Turn Off Program")  # Exits
            self.admin_choice = int(
                input("\u001b[1;31m\t\t\tEnter <1-7>: \u001b[1;0m: ")
            )
            if self.admin_choice == 0 or self.admin_choice > 7:
                while self.admin_choice == 0 or self.admin_choice > 7:
                    os.system("cls||clear")
                    self.admin_choice = int(
                        input("\u001b[1;31m\t\t\tEnter <1-7>: \u001b[1;0m: ")
                    )
            if self.admin_choice == 1:
                Admin.case1_delete_account()
                end = "y"
            elif self.admin_choice == 2:
                Admin.case2_display_all_accounts()
                end = "y"
            elif self.admin_choice == 3:
                g = 0
            elif self.admin_choice == 4:
                c = 0
            elif self.admin_choice == 5:
                os.system("cls||clear")
                break
            elif self.admin_choice == 6:
                quit()

    def case1_delete_account():
        os.system("cls||clear")
        deleted = False
        delaccount = input(
            "\t\t\tEnter the \u001b[1;31mdesired account\u001b[1;0m you want to \u001b[1;31mdelete\u001b[1;0m: "
        )
        with open("usernames.txt", "r") as file:
            with open("tempusers.txt", "w") as tempfile:
                for line in file:
                    if line.strip() != delaccount:
                        tempfile.write(line)
                        deleted = False
                    elif line.strip() == delaccount:
                        deleted = True

        os.remove("usernames.txt")
        os.rename("tempusers.txt", "usernames.txt")
        if deleted == True:
            print(
                "\t\t\tAccount \u001b[1;31mdeleted Successfully\u001b[1;0m\n\t\t\tPress Any \u001b[1;31mKey\u001b[1;0m to continue..."
            )
            m.getch()
        else:
            print("\t\t\t\u001b[1;31mNo Such\u001b[1;0m Username found!\n")
            print("\t\t\tPress any \u001b[1;31mkey\u001b[1;0m to continue...")
            m.getch()

    def case2_display_all_accounts():
        os.system("cls||clear")
        totalaccounts = 0
        counter = 0
        print("\t\t\tHere's the \u001b[1;31mlist of all\u001b[1;0m the accounts below:")
        with open("usernames.txt", "r") as file:
            for lines in file:
                totalaccounts = totalaccounts + 1
                counter = counter + 1
                print("\t\t\t", counter, ".", lines)
        print(
            "\t\t\tThere are total of\u001b[1;31m",
            totalaccounts,
            "\u001b[1;0maccounts present currently\n\t\t\tPress any \u001b[1;31mkey\u001b[1;0m to continue...",
        )
        m.getch()


def main():
    end = "y"
    while end == "y":
        Signin = SignInPage()
        Admins = Admin()
        newuser = NewUser()
        os.system("cls||clear")
        Signin.login()
        if Signin.user_choice == 1:
            Signin.adminlogin()
            if SignInPage.Logged == True:
                Admins.adminmenu()
                if Admins.admin_log == False:
                    continue
            else:
                continue
        elif Signin.user_choice == 3:
            newuser.new_user_createaccount()
        elif Signin.user_choice == 4:
            quit()
    return 0


main()
