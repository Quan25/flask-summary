import summarizerApp
import argparse

def check_ratio(value):
    ivalue = int(value)
    if ivalue < 0 or ivalue > 100:
        raise argparse.ArgumentTypeError("%s is an invalid ratio value" % value)
    return ivalue

# Create the parser and add arguments
parser = argparse.ArgumentParser()

parser.add_argument('--infile', help="Read input text file", type=argparse.FileType('r'))
parser.add_argument('--ratio', help="Ratio for the generated summary, from 1 to 100", type=check_ratio)
# Parse and print the results
args = parser.parse_args()

# calculate and generate the summary
originalText: str = ""
with args.infile as infile:
    for line in infile:
        originalText += line
formattedText: str = summarizerApp.textFormatter(originalText)
result :str = summarizerApp.createSummary(formattedText, int(args.ratio)/100)
print(f'Summary from given text at ratio {args.ratio}%: ')
print(result)
