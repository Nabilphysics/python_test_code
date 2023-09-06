

class testClass():
    abc = "abc"
    def function1(self, str):
        self.function2(str)
    def function2(self, printArgument):
        self.print = printArgument
        self.function3(self.print)

    def function3(self, printArgument):
        print("Print From Function3: ",printArgument)
        print(self.print)
        


def main():
    c = testClass()
    c.function1("F2")
    print(testClass.abc)



if __name__ == "__main__":
    main()