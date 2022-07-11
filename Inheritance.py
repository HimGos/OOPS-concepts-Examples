from ClassIneuron import Ineuron
import logging as lg

lg.basicConfig(filename='inheritance.log', level=lg.INFO, format='%(levelname)s %(asctime)s %(message)s')


# Example 1  ->   1:1 Inheritance

class AboutIneuron(Ineuron):
    pass

try:
    abt_obj = AboutIneuron()
    abt_obj.about()
    lg.info("Successfully printed example 1")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 2  ->   1:1 Inheritance

class Bootcamp(Ineuron):
    print("\nIneuron is good at running intensive bootcamps")

try:
    bcamp_obj = Bootcamp()
    bcamp_obj.bootcamps()
    lg.info("Successfully printed Example 2")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 3  ->   1:1 Inheritance

class Teachers(Ineuron):

    def bestteacher(self):
        """ Best Teacher within Teachers class """
        print("\nIneuron has A++ league Mentors.")

try:
    teach_obj = Teachers()
    teach_obj.bestteacher()
    teach_obj.mentors()
    lg.info("Successfully printed Example 3")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 4  ->   Multi-Level Inheritance

class FsdsTeachers(Teachers):

    def fsds(self):
        """ FSDS Teachers within FsdsTeachers class """
        return 'Sudhanshu Kumar, Sunny Bhaveen, Krish Naik'

try:
    fsds_mentor_obj = FsdsTeachers()
    fsds_mentor_obj.bestteacher()
    fsds_mentor_obj.mentors()
    print(f"Data Science Mentors:- {fsds_mentor_obj.fsds()}")
    lg.info("Successfully printed Example 4")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 5  ->   Multi-Level Inheritance

class FsdsHead(FsdsTeachers):

    def head(self):
        """ Head of FSDS within FsdsHead class """
        print("Mr. Sudhanshu Kumar is the head of FSDS Batch.")

    def othermentors(self):
        """ Other Mentors within FsdsHead class """
        print("Mr. Sunny Bhavin & Mr. Krish Naik cover some topics within FSDS Batch")


try:
    fsds_head_obj = FsdsHead()
    fsds_head_obj.bestteacher()
    fsds_head_obj.mentors()
    print(f"Data Science Mentors:- {fsds_head_obj.fsds()}")
    fsds_head_obj.head()
    fsds_head_obj.othermentors()
    lg.info("Successfully printed Example 5")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 6  ->   Multi-Level Inheritance

class JavaHead(Teachers):

    def head(self):
        """ Head of FSJS within JavaHead class """
        print("Mr. Hitesh Choudhary is the head of FSJS Batch.")

    def othermentors(self):
        """ Other Mentors within JavaHead class """
        print("Mr. Surya Pal & Mr. Shubham Waje cover some topics within FSJS batch")


try:
    java_head_obj = JavaHead()
    java_head_obj.bestteacher()
    java_head_obj.mentors()
    java_head_obj.head()
    java_head_obj.othermentors()
    lg.info("Successfully printed Example 6")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 7  ->   Multiple Inheritance

class HeadMentors1(FsdsHead,JavaHead):

    def check(self):
        """ checking example of multiple inheritance within HeadMentors1 class"""
        print("\nChecking first example of Multiple Inheritance")


try:
    headmentor1_obj = HeadMentors1()
    headmentor1_obj.check()
    headmentor1_obj.head()
    headmentor1_obj.othermentors()
    lg.info("Successfully printed Example 7")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 8  ->   Multiple Inheritance

class HeadMentors2(JavaHead,FsdsHead):

    def check(self):
        """ checking example of multiple inheritance within HeadMentors2 class"""
        print("\nChecking second example of Multiple Inheritance")

try:
    headmentor2_obj = HeadMentors2()
    headmentor2_obj.check()
    headmentor2_obj.head()
    headmentor2_obj.othermentors()
    lg.info("Successfully printed Example 8")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 9   ->   Multiple Inheritance & Multi-Level Inheritance

class IneuronEvents(Ineuron):
    def welcome(self):
        """shows welcome message within IneuronEvents class"""
        print("\nWelcome to Ineuron Events")


class JobAthon1:
    def date(self):
        """prints date of Job-a-thon in JobAthon1 class"""
        print("Upcoming Job-a-Thon date: 10 August 2022")


class HackAthon1:
    def date(self):
        """prints date of Hack-a-thon in HackAthon1 class"""
        print("Upcoming Hack-a-Thon date: 25 July 2022")


class AllEvent1(JobAthon1,HackAthon1,IneuronEvents):
    pass


try:
    all_event_obj1 = AllEvent1()
    all_event_obj1.welcome()
    all_event_obj1.events()
    all_event_obj1.date()
    lg.info("Successfully printed Example 9")

except Exception as e:
    lg.error(f"Error {e} occurred")


# Example 10   ->   Multiple Inheritance & Multi-Level Inheritance

class IneuronEvents(Ineuron):

    def welcome(self):
        """shows welcome message within IneuronEvents class"""
        print("\nWelcome to Ineuron Events")


class JobAthon2:
    def date(self):
        """prints date of Job-a-thon in JobAthon2 class"""
        print("Upcoming Job-a-Thon date: 10 August 2022")


class HackAthon2:
    def date(self):
        """prints date of Hack-a-thon in HackAthon2 class"""
        print("Upcoming Hack-a-Thon date: 25 July 2022")


class AllEvent2(HackAthon2,JobAthon2,IneuronEvents):
    pass


try:
    all_event_obj2 = AllEvent2()
    all_event_obj2.welcome()
    all_event_obj2.events()
    all_event_obj2.date()
    lg.info("Successfully printed Example 10")

except Exception as e:
    lg.error(f"Error {e} occurred")


lg.shutdown()