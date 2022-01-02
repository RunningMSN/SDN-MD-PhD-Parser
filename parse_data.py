from cycle import *
from os import listdir

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
    if month == "1":
        return "January"
    elif month == "2":
        return "February"
    elif month == "3":
        return "March"
    elif month == "4":
        return "April"
    elif month == "5":
        return "May"
    elif month == "6":
        return "June"
    elif month == "7":
        return "July"
    elif month == "8":
        return "August"
    elif month == "9":
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
            # School name
            school = line.split(": ", 1)[0]
            # List of applicants and their data to that school
            applicants = []

            # Applicant data for that school
            data = line.split(": ", 1)[1].strip()

            # Obtain each student individually
            cont_reading = True
            while cont_reading:
                # Obtain the student data
                split_data = data.split(", ", 2)
                applicant_data = ", ".join(split_data[0:2])
                name = applicant_data.split(" ", 1)[0]
                dates = applicant_data.split(" ", 1)[1]
                complete = dates[dates.find("C:") + len("C:"):dates.find(", ")].strip()
                interview = dates[dates.find("II:") + len("II:"):dates.find(")")].strip()

                # Add the data into the cycle
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_complete(school, complete)
                curr_cycle.get_applicant(name).add_interview_received(school, interview)

                if (len(split_data) > 2):
                    data = split_data[2]
                else:
                    cont_reading = False

# Parse Acceptance Data
for cycle_file in listdir('data/acceptances'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/acceptances/" + cycle_file) as data:
        for line in data:
            # School name
            school = line.split(": ", 1)[0]
            # List of applicants and their data to that school
            applicants = []

            # Applicant data for that school
            data = line.split(": ", 1)[1].strip()

            # Obtain each student individually
            cont_reading = True
            while cont_reading:
                # Obtain the student data
                split_data = data.split(", ", 2)
                applicant_data = ", ".join(split_data[0:2])
                name = applicant_data.split(" ", 1)[0]
                dates = applicant_data.split(" ", 1)[1]
                interview_date = dates[dates.find("I:") + len("I:"):dates.find(", ")].strip()
                acceptance = dates[dates.find("A:") + len("A:"):dates.find(")")].strip()

                # Add the data into the cycle
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_interview_date(school, interview_date)
                curr_cycle.get_applicant(name).add_acceptance(school, acceptance)
                if (len(split_data) > 2):
                    data = split_data[2]
                else:
                    cont_reading = False

# Parse Pre-Interview Rejection Data
for cycle_file in listdir('data/pre_int_rejections'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/pre_int_rejections/" + cycle_file) as data:
        for line in data:
            # School name
            school = line.split(": ", 1)[0]
            # List of applicants and their data to that school
            applicants = []

            # Applicant data for that school
            data = line.split(": ", 1)[1].strip()

            # Obtain each student individually
            cont_reading = True
            while cont_reading:
                # Obtain the student data
                split_data = data.split(", ", 2)
                applicant_data = ", ".join(split_data[0:2])
                name = applicant_data.split(" ", 1)[0]
                dates = applicant_data.split(" ", 1)[1]
                complete = dates[dates.find("C:") + len("C:"):dates.find(", ")].strip()
                rejection = dates[dates.find("R:") + len("R:"):dates.find(")")].strip()

                # Add the data into the cycle
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_complete(school, complete)
                curr_cycle.get_applicant(name).add_pre_int_rejection(school, rejection)
                if (len(split_data) > 2):
                    data = split_data[2]
                else:
                    cont_reading = False

# Parse Post-Interview Rejection Data
for cycle_file in listdir('data/post_int_rejections'):
    curr_cycle = get_cycle(cycle_file.strip(".txt"))
    with open("data/post_int_rejections/" + cycle_file) as data:
        for line in data:
            # School name
            school = line.split(": ", 1)[0]
            # List of applicants and their data to that school
            applicants = []

            # Applicant data for that school
            data = line.split(": ", 1)[1].strip()

            # Obtain each student individually
            cont_reading = True
            while cont_reading:
                # Obtain the student data
                split_data = data.split(", ", 2)
                applicant_data = ", ".join(split_data[0:2])
                name = applicant_data.split(" ", 1)[0]
                dates = applicant_data.split(" ", 1)[1]
                interview = dates[dates.find("I:") + len("I:"):dates.find(", ")].strip()
                rejection = dates[dates.find("R:") + len("R:"):dates.find(")")].strip()

                # Add the data into the cycle
                if not curr_cycle.get_applicant(name).schools.__contains__(school):
                    curr_cycle.get_applicant(name).schools.append(school)
                curr_cycle.get_applicant(name).add_interview_date(school, interview)
                curr_cycle.get_applicant(name).add_post_int_rejection(school, rejection)
                if (len(split_data) > 2):
                    data = split_data[2]
                else:
                    cont_reading = False

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