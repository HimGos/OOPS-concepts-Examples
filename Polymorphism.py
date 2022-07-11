from ClassIneuron import Ineuron
import logging as lg

lg.basicConfig(filename="Polymorphism.log", level=lg.INFO, format="%(levelname)s %(asctime)s %(message)s")


# Example 1  ->  Polymorphism using Function

class Telusko:

    def course_categories(self):
        """ Tells about course categories in Telusko class"""
        print("Course categories in Telusko:- Java, Python & C++")

def course_cat(cour):
    """ Function to perform Polymorphism """
    cour.course_categories()

try:
    cc1 = Telusko()
    cc2 = Ineuron()
    course_cat(cc1)
    course_cat(cc2)
    lg.info("Successfully executed Example 1")

except Exception as e:
    lg.error(e)


# Example 2  ->  Polymorphism using Function

class CodingNinja:

    def services(self):
        """ Tells about services within CodingNinja"""
        print("\nServices offered by Coding Ninja -> Jobs")

    def events(self):
        """ Tells about events within CodingNinja"""
        print("Coding Ninja conducts Hack-A-Thon")

    def internship(self):
        """ Tells about internship within CodingNinja"""
        print("Coding Ninja provides internship.")

def serv_events(se):
    """ Function to perform Polymorphism """
    se.services()
    se.events()

try:
    se1 = CodingNinja()
    se2 = Ineuron()
    serv_events(se1)
    serv_events(se2)
    lg.info("Successfully executed Example 2")

except Exception as e:
    lg.error(e)


# Example 3  ->  Polymorphism using Function

class FreeCodeCamp:

    def internship(self):
        """ Tells about Internship within Freecodecamp"""
        print("\nFree Code Camp doesn't provide professional intership")

def intern(inp):
    """ Function to perform Polymorphism """
    inp.internship()

try:
    in1 = FreeCodeCamp()
    in2 = Ineuron()
    in3 = CodingNinja()
    intern(in1)
    intern(in2)
    intern(in3)
    lg.info("Successfully executed Example 3")

except Exception as e:
    lg.error(e)


# Example 4  ->  Polymorphism using Class Method

class Edyoda:

    def internship(self):
        """ Tells about Internship within Edyoda"""
        print("\nEdyoda provides internship",end="")

try:
    ed_obj = Edyoda()
    fc_obj = FreeCodeCamp()
    for i in (ed_obj,fc_obj):
        i.internship()
    lg.info("Successfully executed Example 4")

except Exception as e:
    lg.error(e)


# Example 5  ->  Polymorphism using Class Method

class LCO:

    def about(self):
        """ Tells about the LCO within LCO Class"""
        print("\nHeadquarter: Jaipur, Rajasthan | CEO: Mr. Hitesh Choudhary |"
              " Email: team@learncodeonline.in | website: learncodeonline.in")

    def events(self):
        """ Tells about events within LCO"""
        print("LCO currently conducts events on YouTube")

try:
    lco_obj = LCO()
    ine_obj = Ineuron()
    for i in (lco_obj,ine_obj):
        i.about()
        i.events()
    print()
    lg.info("Successfully executed Example 5")

except Exception as e:
    lg.error(e)


# Example 6  ->  Polymorphism using Class Method

class YouTubeChannel:

    def bootcamps(self):
        """ Tells about bootcamps within YouTubeChannel"""
        print("This channel provides 2 bootcamps")

try:
    yt_obj = YouTubeChannel()
    ineu_obj = Ineuron()
    for i in (ineu_obj,yt_obj):
        i.bootcamps()
        i.events()
    lg.info("Successfully executed Example 6")

except Exception as e:
    lg.error(e)


# Example 7  ->  Polymorphism using Inheritance

class IneuronKids(Ineuron):

    def mentors(self):
        """ Tells about mentors within IneuronKids"""
        print("Ineuron Kids Pack Mentors:- Shubham Sharma, Shivan Kumar, Sunny Bhaveen")

    def finances(self):
        """ Tells about finances within IneuronKids"""
        print("Budget is Rs.15Lacs")

try:
    obj_ineuron = Ineuron()
    obj_ineukids = IneuronKids()
    print()
    obj_ineukids.about()
    obj_ineukids.mentors()
    print()
    lg.info("Successfully executed Example 7")

except Exception as e:
    lg.error(e)


# Example 8  ->  Polymorphism using Multi-Level Inheritance

class IneuronFinances(IneuronKids):

    def finances(self):
        """ Tells about finances within IneuronFinances"""
        print("New budget for kids pack with mentors -> 20Lacs")

try:
    obj_infin = IneuronFinances()
    obj_inkid = IneuronKids()
    obj_infin.about()
    obj_infin.mentors()
    obj_infin.finances()
    lg.info("Successfully executed Example 8")

except Exception as e:
    lg.error(e)


# Example 9  ->  Polymorphism using Multiple Inheritance

class IneuronMembers:

    def staff(self):
        """ Tells about staff within IneuronMembers"""
        print("\nThere are a total of 200 staff members")

    def finances(self):
        """ Tells about finances within IneuronMembers"""
        print("All employees costs $1M per year")

class IneuStaff(Ineuron,IneuronMembers):

    def staff(self):
        """ Tells about staff within IneuronStaff"""
        print("New total of staff member is 250+")

try:
    obj_ine_staff = IneuStaff()
    obj_ineuron = Ineuron()
    obj_ine_mem = IneuronMembers()
    obj_ine_staff.finances()
    obj_ine_staff.staff()
    print()
    lg.info("Successfully executed Example 9")

except Exception as e:
    lg.error(e)


# Example 10  ->  Polymorphism using Multiple Inheritance

class Coursera:

    def about(self):
        """ Tells about Coursera within Coursera"""
        print("\nCoursera has international base.")

    def cost(self):
        """ Tells about cost within Coursera"""
        print("\nCourses are generally expensive in Coursera")

class OneNeuron(Ineuron,Coursera):

    def cost(self):
        """ Tells about cost within OneNeuron"""
        print("Affordable education via OneNeuron")

try:
    oneneuron = OneNeuron()
    obj_coursera = Coursera()
    obj_in_euron = Ineuron()
    oneneuron.about()
    oneneuron.cost()
    lg.info("Successfully executed Example 10")

except Exception as e:
    lg.error(e)


lg.shutdown()