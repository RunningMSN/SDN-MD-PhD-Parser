from cycle import *
from os import listdir
import re
import pandas as pd

# List of cycles
cycles = []


def get_cycle(cycle_name):
    """Gets cycle object corresponding to a particular year"""
    # Get an existing cycle
    for cycle in cycles:
        if cycle.cycle_name == cycle_name:
            return cycle
    # Add new cycle
    new_cycle = Cycle(cycle_name)
    cycles.append(new_cycle)
    return new_cycle

def assign_year(month, cycle):
    """Returns the proper year of a date given the month and cycle."""
    if int(month) >= 6:
        return str(int(cycle) - 1)
    else:
        return str(int(cycle))


def get_month_name(month):
    """Returns the name of the month."""
    if month == "1" or month == "01":
        return "January"
    elif month == "2" or month == "02":
        return "February"
    elif month == "3" or month == "03":
        return "March"
    elif month == "4" or month == "04":
        return "April"
    elif month == "5" or month == "05":
        return "May"
    elif month == "6" or month == "06":
        return "June"
    elif month == "7" or month == "07":
        return "July"
    elif month == "8" or month == "08":
        return "August"
    elif month == "9" or month == "09":
        return "September"
    elif month == "10":
        return "October"
    elif month == "11":
        return "November"
    elif month == "12":
        return "December"
    else:
        return


# Parse Interview Data
for cycle_file in listdir('data/interviews'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/interviews/" + cycle_file) as data:
        for line in data:
            school = line.split(":", 1)[0]
            pattern = "(?P<username>[\w\d ?\-#*]+)[:]{0,1}[ ]*[/(]C:[ ]{0,1}(?P<complete_date>[\w\d/]+)[ ]{0,1}, II:[ ]{0,1}(?P<interview_date>[\w\d/]+)[\)]"
            user_data_frame = pd.DataFrame(re.findall(pattern, line.split(":", 1)[1]),  columns=('Username', 'Complete', 'Interview'))
            for index,row in user_data_frame.iterrows():
                name = row['Username'].strip()
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_complete(school, row['Complete'])
                curr_cycle.get_applicant(name).add_interview_received(school, row['Interview'])

# Parse Acceptance Data
for cycle_file in listdir('data/acceptances'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/acceptances/" + cycle_file) as data:
        for line in data:
            school = line.split(":", 1)[0]
            pattern = "(?P<username>[\w\d ?\-#*]+)[:]{0,1}[ ]*[/(]I:[ ]{0,1}(?P<interview_date>[\w\d/]+)[ ]{0,1}, A:[ ]{0,1}(?P<acceptance_date>[\w\d/]+)[\)]"
            user_data_frame = pd.DataFrame(re.findall(pattern, line.split(":", 1)[1]),
                                           columns=('Username', 'Interview', 'Acceptance'))
            for index, row in user_data_frame.iterrows():
                name = row['Username'].strip()
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_interview_date(school, row['Interview'])
                curr_cycle.get_applicant(name).add_acceptance(school, row['Acceptance'])

# Parse Pre-Interview Rejection Data
for cycle_file in listdir('data/pre_int_rejections'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/pre_int_rejections/" + cycle_file) as data:
        for line in data:
            school = line.split(":", 1)[0]
            pattern = "(?P<username>[\w\d ?\-#*]+)[:]{0,1}[ ]*[/(]C:[ ]{0,1}(?P<complete_date>[\w\d/]+)[ ]{0,1}, R:[ ]{0,1}(?P<reject_date>[\w\d/]+)[\)]"
            user_data_frame = pd.DataFrame(re.findall(pattern, line.split(":", 1)[1]),
                                           columns=('Username', 'Complete', 'Reject'))
            for index, row in user_data_frame.iterrows():
                name = row['Username'].strip()
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_complete(school, row['Complete'])
                curr_cycle.get_applicant(name).add_pre_int_rejection(school, row['Reject'])

# Parse Post-Interview Rejection Data
for cycle_file in listdir('data/post_int_rejections'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/post_int_rejections/" + cycle_file) as data:
        for line in data:
            school = line.split(":", 1)[0]
            pattern = "(?P<username>[\w\d ?\-#*]+)[:]{0,1}[ ]*[/(]I:[ ]{0,1}(?P<complete_date>[\w\d/]+)[ ]{0,1}, R:[ ]{0,1}(?P<reject_date>[\w\d/]+)[\)]"
            user_data_frame = pd.DataFrame(re.findall(pattern, line.split(":", 1)[1]),
                                           columns=('Username', 'Interview', 'Reject'))
            for index, row in user_data_frame.iterrows():
                name = row['Username'].strip()
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_interview_date(school, row['Interview'])
                curr_cycle.get_applicant(name).add_post_int_rejection(school, row['Reject'])


# Print out the raw output without any modification to data
with open("outputs/raw_output.csv", "w") as file:
    file.write("cycle,applicant,school,complete,pre-II rejection,interview received,interviewed on,accepted,post-II rejection\n")
    for cycle in cycles:
        for applicant in cycle.applicants:
            for school in applicant.schools:
                file.write(cycle.cycle_name + "," + applicant.username + "," + school +",")
                if school in applicant.complete_dates:
                    file.write(applicant.complete_dates[school])
                file.write(",")
                if school in applicant.pre_int_rejections:
                    file.write(applicant.pre_int_rejections[school])
                file.write(",")
                if school in applicant.interview_received_dates:
                    file.write(applicant.interview_received_dates[school])
                file.write(",")
                if school in applicant.interview_dates:
                    file.write(applicant.interview_dates[school])
                file.write(",")
                if school in applicant.acceptances:
                    file.write(applicant.acceptances[school])
                file.write(",")
                if school in applicant.post_int_rejections:
                    file.write(applicant.post_int_rejections[school])
                file.write("\n")

# Print out cured useful data
with open("outputs/corrected_output.csv", "w") as file:
    file.write("cycle,applicant,school,complete_month,complete_date,pre-II_reject_month,pre-II_reject_date,interview_received_month,interview_received_date,interview_on_month,interview_on_date,accepted_month,accepted_date,post-II_reject_month,post-II_reject_date\n")
    for cycle in cycles:
        for applicant in cycle.applicants:
            for school in applicant.schools:
                file.write(cycle.cycle_name + "," + applicant.username + "," + school + ",")
                # App Completion
                if school in applicant.complete_dates:
                    month = applicant.complete_dates[school].split("/")[0]
                    day = applicant.complete_dates[school].split("/")[1].lower()
                    file.write(str(get_month_name(month)) + ",")
                    if not day.__contains__("x"):
                        file.write(str(month) + "/" + day + "/" + str(assign_year(month, cycle.cycle_name)))
                else:
                    file.write(",")
                file.write(",")
                # Pre-II rejection
                if school in applicant.pre_int_rejections:
                    month = applicant.pre_int_rejections[school].split("/")[0]
                    day = applicant.pre_int_rejections[school].split("/")[1].lower()
                    file.write(str(get_month_name(month)) + ",")
                    if not day.__contains__("x"):
                        file.write(str(month) + "/" + day + "/" + str(assign_year(month, cycle.cycle_name)))
                else:
                    file.write(",")
                file.write(",")
                # Interview received
                if school in applicant.interview_received_dates:
                    month = applicant.interview_received_dates[school].split("/")[0]
                    day = applicant.interview_received_dates[school].split("/")[1].lower()
                    file.write(str(get_month_name(month)) + ",")
                    if not day.__contains__("x"):
                        file.write(str(month) + "/" + day + "/" + str(assign_year(month, cycle.cycle_name)))
                else:
                    file.write(",")
                file.write(",")
                # Interviewed on
                if school in applicant.interview_dates:
                    month = applicant.interview_dates[school].split("/")[0]
                    day = applicant.interview_dates[school].split("/")[1].lower()
                    file.write(str(get_month_name(month)) + ",")
                    if not day.__contains__("x"):
                        file.write(str(month) + "/" + day + "/" + str(assign_year(month, cycle.cycle_name)))
                else:
                    file.write(",")
                file.write(",")

                # Acceptance
                if school in applicant.acceptances:
                    month = applicant.acceptances[school].split("/")[0]
                    day = applicant.acceptances[school].split("/")[1].lower()
                    file.write(str(get_month_name(month)) + ",")
                    if not day.__contains__("x"):
                        file.write(str(month) + "/" + day + "/" + str(assign_year(month, cycle.cycle_name)))
                else:
                    file.write(",")
                file.write(",")
                # Post-II Rejections
                if school in applicant.post_int_rejections:
                    month = applicant.post_int_rejections[school].split("/")[0]
                    day = applicant.post_int_rejections[school].split("/")[1].lower()
                    file.write(str(get_month_name(month)) + ",")
                    if not day.__contains__("x"):
                        file.write(str(month) + "/" + day + "/" + str(assign_year(month, cycle.cycle_name)))
                else:
                    file.write(",")
                file.write("\n")