from ClassIneuron import Ineuron
import logging as lg

lg.basicConfig(filename="methodoverr.log", level=lg.INFO, format="%(levelname)s %(asctime)s %(message)s")


# Example 1   ->    Using 1:1 Inheritance & calling parent

class IneuronHQ1:

    def __init__(self):
        """Constructor"""
        print("HQ1 of Ineuron is in Bengaluru.")

    def location(self):
        print("Address: 17 A, Bridge Signature Towers")


class IneuronHQ2(IneuronHQ1):

    def __init__(self):
        """Constructor"""
        print("HQ2 of Ineuron is in Delhi.")

    def location(self):
        print("Address: J-11, Connaught Place")
        super().__init__()

try:
    obj_1 = IneuronHQ2()
    obj_1.location()
    lg.info("Successful Execution of Example 1")

except Exception as e:
    lg.error(e)



# Example 2   ->    Using 1:1 Inheritance

class IneuronCourses(Ineuron):

    def __init__(self):
        """Constructor"""
        print("\nHere we get to know about courses in Ineuron")

    def course_categories(self):
        print("Ineuron has over 300 courses in various categories")

    def packages(self):
        print("Ineuron only has OneNeuron Package")

try:
    obj_2 = IneuronCourses()
    obj_2.course_categories()
    lg.info("Successful Execution of Example 2")

except Exception as e:
    lg.error(e)



# Example 3   ->    Using Multi-Level Inheritance

class IneuronPackage(IneuronCourses):

    def packages(self):
        print("Ineuron has OneNeuron and Kids Neuron as well.\n")

try:
    obj_3 = IneuronPackage()
    obj_3.course_packages()
    obj_3.packages()
    lg.info("Successful Execution of Example 3")

except Exception as e:
    lg.error(e)



# Example 4   ->    Using Multi-Level Inheritance & calling super classes

class IneuronMentors:

    def __init__(self):
        """Constructor"""
        print("Init of grandparent class")

    def totalmentors(self):
        print("There are overall 25 mentors in Ineuron.")


class OneNeuronMentors(IneuronMentors):

    def __init__(self):
        """Constructor"""
        print("Init of Parent class.")
        super().__init__()

    def totalmentors(self):
        print("There are 17 mentors for OneNeuron")


class KidsNeuronMentors(OneNeuronMentors):

    def __init__(self):
        """Constructor"""
        print("Init of Child Class")

    def totalmentors(self):
        print("Kids Neuron has 8 mentors.")
        super().__init__()

try:
    obj_4 = KidsNeuronMentors()
    obj_4.totalmentors()
    lg.info("Successful Execution of Example 4")

except Exception as e:
    lg.error(e)



# Example 5   ->    Using Multi-Level Inheritance

class AffiliateMarketing:

    def intro(self):
        print("\nWelcome to Affiliate Marketing")

    def commission(self):
        print("Physical product commission is less than 10%")


class OnlineMarketing(AffiliateMarketing):

    def commission(self):
        print("Digital product commission is more than 10%")


class IneuronAff(OnlineMarketing):

    def commission(self):
        print("Ineuron provides 20% commission on each sale!")

try:
    obj_5 = IneuronAff()
    obj_5.intro()
    obj_5.commission()
    lg.info("Successful Execution of Example 5")

except Exception as e:
    lg.error(e)



# Example 6   ->   Using Multiple Inheritance

class Jobs:

    def intro(self):
        print("There are thousands of types of jobs in the world")


class OnlineJobs:

    def onlinejob(self):
        print("\nOnline jobs are at boom currently!")


class IneuronJobs(Jobs,OnlineJobs):

    def intro(self):
        print("Ineuron has Job Guarantee Program\n")

try:
    obj_6 = IneuronJobs()
    obj_6.onlinejob()
    obj_6.intro()
    lg.info("Successful Execution of Example 6")

except Exception as e:
    lg.error(e)



# Example 7   ->   Using Multiple Inheritance & calling Grandparent class

class Internship:

    def __init__(self):
        """Constructor"""
        print("Internship is very important for a fresher.")

    def intern(self):
        print("There are two types of internships, Paid and Unpaid")


class FreeCodeCamp:

    def __init__(self):
        """Constructor"""
        print("Free Code Camp provides unpaid internship")

    def duration(self):
        print("Duration of internship in FCC is 6 months")


class IneuronIntern(Internship,FreeCodeCamp):

    def duration(self):
        print("Duration of internship in Ineuron is 8 months")
        super().__init__()

try:
    obj_7 = IneuronIntern()
    obj_7.intern()
    obj_7.duration()
    lg.info("Successful Execution of Example 7")

except Exception as e:
    lg.error(e)



# Example 8   ->    using Multiple Inheritance & calling init of parent & Grandparent class

class FinanceDept:

    def __init__(self):
        """Constructor"""
        print("India's Finance Department has budget in Billions.")

    def budget(self):
        print("National education budget is 367cr.")


class IneuronFinance:

    def __init__(self):
        """Constructor"""
        print("Ineuron has overall budget in millions.")
        super().__init__()

    def finance(self):
        print("Ineuron spends $100K every year on technology")


class IneuronKidsSection(IneuronFinance,FinanceDept):

    def budget(self):
        print("Inueron has a budget of $200K for Kids Neuron.")
        super().__init__()

try:
    print()
    obj_8 = IneuronKidsSection()
    obj_8.budget()
    obj_8.finance()
    lg.info("Successful Execution of Example 8")

except Exception as e:
    lg.error(e)



# Example 9   ->    using Multiple Inheritance & calling multiple classes at once

class IneuronEducation:

    def __init__(self):
        """Constructor"""
        print("Ineuron provides over 300 courses including bootcamps\n")
        super().__init__()

    def education(self):
        print("Motto of Ineuron: Make Education Affordable & Accessible to everyone")


class CoursesIneuron:

    def __init__(self):
        """Constructor"""
        print("There is a wide range & categories of courses in Ineuron.")
        super().__init__()

    def fsdsbootcamp(self):
        print("There is no fsds bootcamp in ineuron")


class BootcampsIneuron:

    def __init__(self):
        """Constructor"""
        print("There are currently 4 ongoing bootcamps in Ineuron")
        super().__init__()

    def fsdsbootcamp(self):
        print("This bootcamp will start in september")


class FsdsIneuron(BootcampsIneuron,CoursesIneuron,IneuronEducation):

    def fsdsbootcamp(self):
        print("FSDS Bootcamp started on 7th May by Mr. Sudhanshu Kumar")
        super().__init__()

try:
    print()
    obj_9 = FsdsIneuron()
    obj_9.education()
    obj_9.fsdsbootcamp()
    lg.info("Successful Execution of Example 9")

except Exception as e:
    lg.error(e)



# Example 10   ->    using Multiple Inheritance

class HofIneuron:

    def __init__(self):
        """Constructor"""
        self.__hof = 182
        super().__init__()

    def halloffame(self):
        print(f"There a total of {self.__hof} achievers in hall of fame!")


class JobGuaranteeProg:

    def __init__(self):
        """Constructor"""
        print("Ineuron has Job Guarantee Program but there is a criteria.")

    def hired(self):
        print("Every years many people get hired via Ineuron")


class Hired(HofIneuron,JobGuaranteeProg):

    def hired(self):
        print("Himanshu got hired in Microsoft!! Thanks to Ineuron")
        self._HofIneuron__hof += 1

try:
    obj_10 = Hired()
    obj_10.halloffame()
    obj_10.hired()
    obj_10.halloffame()
    lg.info("Successful Execution of Example 10")

except Exception as e:
    lg.error(e)


lg.shutdown()