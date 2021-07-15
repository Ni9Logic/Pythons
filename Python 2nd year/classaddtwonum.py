class addition:
    num1 = 0.0
    num2 = 0.0

    def addition(self):
        self.num1 = int(input("Enter Num1: "))
        self.num2 = int(input("Enter Num2: "))
        self.additions = self.num1 + self.num2
        self.additions = int(self.additions)
        print("Addition of two Numbers are:", self.additions)
        return self.additions

object = addition()
object.addition()