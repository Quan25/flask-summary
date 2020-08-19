import argparse
import autoGrader
import json
# Create the parser and add arguments
parser = argparse.ArgumentParser()

parser.add_argument('--teacher', help="Read instructor's summary text file", type=argparse.FileType('r'))
parser.add_argument('--students', help="Read students' summary text file name", type=argparse.FileType('r'))
# Parse and print the results
args = parser.parse_args()

#read data and generate score
instructor=dict()
student_dict = dict()

#read in instructor data
instructorSummary: str = ""
with args.teacher as teacher:
    for line in teacher:
        instructorSummary += line
instructor["Instructor"] = instructorSummary
with open('Instructor.json', 'w') as json_file:
    json.dump(instructor, json_file)

#read in studnets data
studentSummary: str = ""
studentSummaryList = []
with args.students as students:
    for line in students:
        with open(line[:-1], 'r') as student:
            for line_student in student:
                studentSummary += line_student
        studentSummaryList.append(studentSummary)
        studentSummary = ""
with open('Student.json', 'r+') as json_file:

    student_dict["Student"] = studentSummaryList
    json.dump(student_dict, json_file)

(result, instructor, percentile) = autoGrader.Grader()
for each, value in percentile.items():
    print(each)
    for name in value.values():
        print(name)
