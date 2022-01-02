from applicant import *

class Cycle(object):
    def __init__(self, cycle_name):
        self.cycle_name = cycle_name
        self.applicants = []
        return

    def get_applicant(self, username):
        # Checks for existing student
        for applicant in self.applicants:
            if applicant.username == username:
                return applicant
        # If could not find the student, add them in
        new_applicant = Applicant(username)
        self.applicants.append(new_applicant)
        return new_applicant





