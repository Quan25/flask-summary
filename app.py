
from flask import Flask, render_template, request, url_for
import argsParser
import os
from PreSumm.src.others.logging import init_logger
from PreSumm.src.train_abstractive import test_text_abs

app = Flask(__name__)

@app.route('/')
def textToSummarize():
   return render_template('original.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      originalText = request.form['text']
      args = argsParser.parse_args()

      text_to_save = open("PreSumm/raw_data/temp.raw_src", "w")

      originalText = originalText.replace("\n", "")
      text_to_save.write(originalText)
      text_to_save.close()
      test_text_abs(args)
      summary = open("PreSumm/results/cnndm.-1.candidate", "rt")
      result=""
      for line in summary:
          result += line.replace("<q>", ". ")

      return render_template("result.html",summaryText = result)

if __name__ == '__main__':
   app.run(debug = True)
