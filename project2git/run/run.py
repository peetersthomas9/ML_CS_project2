from transformers import pipeline

import re


def pre_process(text):
  text = re.sub(r"<user>", "", text)  # remove <user>
  text = re.sub(r"\n", "", text)
  others = '1234567890'  # remove these symbols
  for p in others:
    text = text.replace(p, '')
  return text


# retreive model from huggingface, change if you want a different model
pipe = pipeline("text-classification", model="mollypak/cardiff-num")

import numpy as np

# import test data
file1 = open('ML_CS_project2-main/project2git/data/not_preprocessed/test_data.txt', 'r')
Lines = file1.readlines()

guess = np.zeros((len(Lines), 2))

for i in range(0, len(Lines)):
  guess[i, 0] = i + 1

  if pipe(pre_process(Lines[i]))[0].get("label") == 'LABEL_2':
    guess[i, 1] = 1
  if pipe(pre_process(Lines[i]))[0].get("label") == 'LABEL_0':
    guess[i, 1] = -1

np.savetxt("test_FINALSUBMIT.csv", guess, delimiter=",", header="Id,Prediction", fmt="%i", comments='')