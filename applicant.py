class Applicant(object):
    def __init__(self, username):
        self.username = username
        self.schools = []
        self.interview_received_dates = {}
        self.interview_dates = {}
        self.acceptances = {}
        self.pre_int_rejections = {}
        self.post_int_rejections = {}
        self.complete_dates = {}
        return

    def add_school(self, school):
        self.schools.append(school)
        return

    def add_interview_received(self, school, date):
        self.interview_received_dates[school] = date
        return

    def add_interview_date(self, school, date):
        self.interview_dates[school] = date
        return

    def add_acceptance(self, school, date):
        self.acceptances[school] = date
        return

    def add_pre_int_rejection(self, school, date):
        self.pre_int_rejections[school] = date
        return

    def add_post_int_rejection(self, school, date):
        self.post_int_rejections[school] = date

    def add_complete(self, school, date):
        self.complete_dates[school] = date
        return
