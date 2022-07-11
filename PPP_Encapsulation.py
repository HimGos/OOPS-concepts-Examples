import logging as lg
lg.basicConfig(filename="encapsulation.log", level=lg.INFO, format="%(levelname)s %(asctime)s %(message)s")


# Example 1

class IneuronDetails1:

    def __init__(self):
        """Constructor"""
        self.__ceo = 'Mr. Sudhanshu Kumar'                    # Private
        self._email = 'contact@ineuron.ai'                    # Protected
        self.hq = "Bridge Signature Towers, Bengaluru"        # Public
        self.__web = "www.ineuron.ai"

    def admin(self):
        """This function changes class variables"""
        print(f"Changing HQ of Ineuron to {self.hq}")
        print(f"Changing Website of Ineuron to {self.__web}")
        print(f"Changing email of Ineuron to {self._email}\n")

try:
    obj_1 = IneuronDetails1()
    obj_1.hq = "Connaught Place, Delhi"
    obj_1._email = 'official@ineuron.ai'
    obj_1.__web = "www.ineurology.ai"
    obj_1.admin()
    lg.info("Successful Execution of Example 1, able to change Public & Protected variables but not Private one")


except Exception as e:
    lg.error(e)


# Example 2

class IneuronDetails2:

    def __init__(self):
        """Constructor"""
        self.__ceo = 'Mr. Sudhanshu Kumar'
        self._email = 'contact@ineuron.ai'
        self.hq = "Bridge Signature Towers, Bengaluru"
        self.__web = "www.ineuron.ai"

try:
    obj_2 = IneuronDetails2()
    print(obj_2.hq)
    print(obj_2.__email)
    lg.info("Successful Execution of Example 2")

except Exception as e:
    lg.error(e)
    print("Can't access Private Variable Without calling class first\n")


# Example 3

class IneuronDetails3:

    def __init__(self):
        """Constructor"""
        self.__ceo = 'Mr. Sudhanshu Kumar'

try:
    obj_3 = IneuronDetails3()
    print(obj_3._IneuronDetails3__ceo)
    print("Now we are able to print the PRIVATE variable\n")
    lg.info("Successful Execution of Example 3")

except Exception as e:
    lg.error(e)
    print("Can't access Private Variable Without calling class first")


# Example 4

class NewMentor:

    def __init__(self,name,subject):
        """Constructor"""
        self.__name = name
        self.__subject = subject
        print(f"Ineuron's new mentor: {self.__name}, will teach {self.__subject}")

    def modify(self,newsub):
        """This function prints the modified name and subject"""
        self.__subject = newsub
        print(f"Now {self.__name} will teach {self.__subject}\n")

try:
    obj_4 = NewMentor('Himanshu Goswami','Python')
    obj_4.modify('Deep Learning')
    lg.info("Successful Execution of Example 4")

except Exception as e:
    lg.error(e)


# Example 5

class NewMentor2:

    def __init__(self, name, subject):
        """Constructor"""
        self.__name = name
        self.__subject = subject
        print(f"Ineuron's new mentor: {self.__name}, will teach {self.__subject}")

    def modify(self):
        """This function prints the modified name and subject"""
        print(f"Now {self.__name} will teach {self.__subject}\n")


try:
    obj_5 = NewMentor2('Himanshu Goswami', 'Python')
    obj_5._NewMentor2__subject = 'Computer Vision'
    obj_5.modify()
    lg.info("Successful Execution of Example 5")

except Exception as e:
    lg.error(e)


# Example 6

class Affiliate:

    def __init__(self):
        """Constructor"""
        self.__name = "Himanshu Goswami"
        self._traffic = "Facebook"
        self.__commission = '20%'
        print(f"Commission for Ineuron courses sale: {self.__commission}")

    def fsds_course(self):
        """This course is to set commission for fsds"""
        self.__commission = '25%'
        print(f"Commission for FSDS Course sale: {self.__commission}")

    def custom(self,mycomm):
        """This function allows to set custom commission rate"""
        self.__commission = mycomm
        print(f"I, {self.__name}, bring traffic from {self._traffic} and want {self.__commission}% commission.")

try:
    obj_6 = Affiliate()
    obj_6.fsds_course()
    obj_6.custom(30)
    lg.info("Successful execution of example 6")

except Exception as e:
    lg.error(e)


# Example 7   ->  Calling using Child CLass

class Courses:

    def __init__(self):
        """Constructor"""
        self.__ds = 'Data Science'
        self._fsds = 'Full Stack Data Science'
        self.__js = 'Java Script'
        self._fsjs = 'Full Stack Java Script'

class Bootcamp(Courses):

    def our_bootcamps(self):
        """This function shows bootcamp courses"""
        print(f"\n{self._fsds} & {self._fsjs}")

    def courses(self):
        """This function shows courses"""
        print(f"\n{self.__ds} & {self.__js}")

try:
    obj_7 = Bootcamp()
    obj_7.our_bootcamps()
    obj_7.courses()
    lg.info("Successful Execution of Example 7")

except Exception as e:
    lg.error(e)
    print("Can't call in child class without mentioning parent class")


# Example 8   ->  Calling inside Child Class

class Courses2:

    def __init__(self):
        """Constructor"""
        self.__ds = 'Data Science'
        self.__js = 'Java Script'

class Bootcamp2(Courses2):

    def courses(self):
        """This function shows courses"""
        print(f"\n{self._Courses2__ds} & {self._Courses2__js}\n")

try:
    obj_8 = Bootcamp2()
    obj_8.courses()
    lg.info("Successful Execution of Example 8")

except Exception as e:
    lg.error(e)


# Example 9

class HallOfFame:

    def __init__(self):
        """Constructor"""
        self.__achievers = 182

    def total_achievers(self):
        """Shows Total achievers of Hall of Fame"""
        print(f"There are a total of {self.__achievers} achievers in Ineuron's Hall of Fame!")

    def new_hof(self,name):
        """New Hall of Famer function """
        print(f"New guy in Hall of Fame list: {name}")

try:
    obj_9 = HallOfFame()
    obj_9.total_achievers()
    obj_9.new_hof('Himanshu Goswami')
    obj_9._HallOfFame__achievers = 183
    obj_9.total_achievers()
    print()
    lg.info("Successful Execution of Example 9")

except Exception as e:
    lg.error(e)


# Example 10

class IneuronOnline:

    def __init__(self):
        """Constructor"""
        self.__a_level = 'Microsoft'
        self.__b_level = 'Binance'

    def candidate(self,name,age):
        """Candidate function helps in assigning company for candidate"""
        if age > 25 and age <30:
            print(f"Candidate {name} got selected in {self.__a_level}")
        elif age >30 and age<40:
            print(f"Candidate {name} for selected in {self.__b_level}")

class IneuronWalkIn(IneuronOnline):

    def __init__(self):
        """Constructor"""
        self._IneuronOnline__a_level = 'Apple'
        self._IneuronOnline__b_level = 'Tesla'

try:
    obj_10 = IneuronOnline()
    obj_10.candidate('Himanshu Goswami', 26)
    obj_11 = IneuronWalkIn()
    obj_11.candidate('Himanshu Goswami',26)
    lg.info("Successful Execution of Example 10")

except Exception as e:
    lg.error(e)


lg.shutdown()