
from flask import Flask, render_template, request, url_for, redirect
import argsParser, autoGrader
import os
import summarizerApp
import json
import time


app = Flask(__name__)

@app.route('/')
def textToSummarize():
   ratio="20"
   return render_template('original.html', ratio=ratio)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
      instructor=dict()
      student = dict()

      originalText = request.form['text']

      choice = request.form['add']
      ratio = request.form['ratio']
      print(request.form)
      formattedText: str = summarizerApp.textFormatter(originalText)
      # text_to_save = open("PreSumm/raw_data/temp.raw_src", "w")
      #
      #
      # originalText=" ".join([ll.rstrip() for ll in originalText.splitlines() if ll.strip()])
      # #print(f'$$$${r}')
      # args = argsParser.parse_args(int(len(originalText) * int(ratio) / 100) )
      # text_to_save.write(originalText)
      # text_to_save.close()
      start = time.time()
      # test_text_abs(args)
      #
      # summary = open("PreSumm/results/cnndm.-1.candidate", "rt")
      result: str = summarizerApp.createSummary(formattedText, int(ratio)/100)

      end = time.time()

      elapsedTime="Total Time cost:" + str(round(end-start,2)) + "s"

      if(choice == "Add To Instructor"):

          instructor["Instructor"] = result
          with open('Instructor.json', 'w') as json_file:
              json.dump(instructor, json_file)

      elif(choice == "Add To Student"):

          with open('Student.json', 'r+') as json_file:
              if not json_file.read(1):
                  student["Student"] = [result]
                  json.dump(student, json_file)

              else:
                  with open('Student.json', 'r') as json_file1:
                      data = json.load(json_file1)
                      data["Student"].append(result)
                  with open('Student.json', 'w') as json_file1:
                      json.dump(data, json_file1)

      return render_template("original.html",summaryText = result, originalText = originalText, elapsedTime=elapsedTime, ratio=ratio)

@app.route('/reset',methods = ['POST', 'GET'])
def reset():

    autoGrader.reset()
    return redirect("/")


@app.route('/grade',methods = ['POST', 'GET'])
def grade():
    (result, instructor, percentile) = autoGrader.Grader()

    return render_template("grade.html",grade = result, instructor=instructor, percentile = percentile)
if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)
