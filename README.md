# ML_CS_project2

We have 5 different folders : 

data : 	In this folder we have the initial data and the preprocessed data. 
	We also have the different embedded matrix (the one obtained with the method in class and the one obtain using glove dataset. 

pre-processing : 	In this folder we have all the jupyter file to pre-processed the data and get our training features. 
			clean_text : we pre-process the text to get simpler sentence (remove punctuation, stop word, lower case, lemmatization)
			tokenizer_embedding: we create the embedding matrix and the tokenizer (convert word to int) 

model : folder where we save all our model compute 
	model_LSTM should be run on google colab so that we can use the GPU and compute our model faster, the cvs file is directly created at the end

run : file where we can run our linear model to obtain the .cvs file with our prediction. run.py will reproduce the best performing model(cardiff roBERTa base). If you wish to test another BERT model we used, please see the "for BERT" section below

BERTfinetunedmodels: Jupyter notebooks of BERT models and variants. The code for the "compute_metrics" function was curtosy of a class taught by James Henderson (IDIAP). 
how to run LSTM and linear model : 

Put the train and test set in data/not_preprocessed. 

In preprocessing : Run clean_text to prerocess the data 

FOR LSTM : ----------------------------------------------------------------------------------------

Download the pre-trained word vectors https://github.com/stanfordnlp/GloVe

In preprocessing folder : Run tokenizer_embedding to get the embedding matrix (build embedding matrix using glove method) and the tokenizer

In model folder: Go in google colab and use the GPU to run 'model_LSTM' (get the best performance using "glove.twitter.27B.200d" and the pre_processed dataset. 

---------------------------------------------------------------------------------------------------

FOR linear model : --------------------------------------------------------------------------------
 
compute the embedded matrix using the method given in the assignement (build vocab, cut_vocab, ... glove_template) and put the embedding matrix and vocab 
in 'data/not_preprocessed' or 'data/preprocessed' depending on if you have used the initial dataset or the preprocessed dataset. 

In model folder : Run model_linear to build a model (you can modify which model you want a build LinearRegression, LinearSVM... ) 

In run folder : Run 'run_linear' to get the csv file for our prediction

---------------------------------------------------------------------------------------------------


FOR BERT models : --------------------------------------------------------------------------------


They are meant to be run on google TPUs- in order to run on CPU or GPU they code will need to be modified a little bit. Checkpoints happen a little under 10K steps. The data and checkpoints need to be saved on google drive.

Both the classify.ipynb and run.py will reproduce BERT sumbissions. The fine-tuned BERT models have all been uploaded to my huggingface account (mollypak) and are publically available. In order to test the different modes, the path must be changed in the "pipeline" function. The four paths are:

a)mollypak/cardiff-num (the best one and default), Cardiff roBERTa base (LABEL_0,LABEL_2)

b)mollypak/cardiff-xlm-roberta-base - Cardiff XLM roBERTa (LABEL_0,LABEL_2)

c)mollypak/roberta-base (LABEL_0,LABEL_2)

d)mollypak/bert-multilingual-base (LABEL_0,LABEL_1)

The number at the end are the labels neeed for classification

Please not you will need the newest version of the "transformers" package to run the run.py file. A jupyter notebook was also included to run on google colab if your pc is having troubles with the transformers version

Special thanks to the following tutorial for how to parallelize data on TPUs
https://colab.research.google.com/drive/1dVEfoxGvMAKd0GLnrUJSHZycGtyKt9mr#scrollTo=FyTR9V5jJWcS

Thanks to Dr. James Henderson at IDIAP whose course introduced me to pretraining huggingface models and helped. with the code (and provided the  "compute metrics" function
