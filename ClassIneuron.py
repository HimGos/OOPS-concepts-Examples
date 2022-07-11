class Ineuron:

    def about(self):
        """ Details of Company """
        self.ceo = 'Mr. Sudhanshu Kumar'
        self.email = 'contact@ineuron.ai'
        self.hq = "Bridge Signature Towers, Bengaluru"
        self.web = "www.ineuron.ai"
        print(f'Headquarter - {self.hq} | CEO - {self.ceo}  |' \
               f' Email - {self.email} | Website - {self.web}')

    def course_categories(self):
        """ Types of courses provided by Ineuron """
        self.ds = "Data Science"
        self.prog = "Programming"
        self.dev = "Development"
        self.cloud = "Cloud"
        self.mkt = "Marketing"
        print(f'Course Categories in Ineuron:- {self.ds}, {self.prog},' \
               f' {self.dev}, {self.cloud}, {self.mkt}')

    def course_packages(self):
        """ Course packages provided by Ineuron """
        self.one_neuron = "One Neuron Package"
        self.kid_neuron = "Kid Neuron Package"
        print(f"There are two packages:- \n{self.one_neuron} with 249 Courses & \n{self.kid_neuron} with 39 Courses")

    def bootcamps(self):
        """ Bootcamps provided by Ineuron """
        print("Ongoing Bootcamps:- C++, Big Data, FSDS, Digital Marketing")

    def mentors(self):
        """ Some highly qualified mentors of Ineuron """
        print('Ineuron Mentors:- Hitesh Choudhary, Sudhanshu Kumar, Kiran Sahu, Sunny Bhaveen, Navin Reddy, Krish Naik')

    def services(self):
        """ Types of services provided by Ineuron beside courses. """
        self.aff = "Affiliate Marketing"
        self.int = "Internship"
        self.job = "Job Program"
        print(f"Services offered by Ineuron -> {self.aff}, {self.int}, {self.job}")

    def hall_of_fame(self):
        """ Details regarding Hall of Fame """
        self.hof = 182
        print(f"There are a total of {self.hof} achievers in Hall of Fame")

    def events(self):
        """ Regular events conducted by Ineuron """
        print("Ineuron Conducts Job-a-Thon and Hack-a-Thon")

    def internship(self):
        """ Info on internship provided by Ineuron. """
        self.proj = 50
        print(f"Ineuron offers internship with {self.proj} projects while maintaining industry standards.")

    def finances(self):
        """ Info on turnover of ineuron """
        print("\nAnnual revenue of company: $6.4M per year")