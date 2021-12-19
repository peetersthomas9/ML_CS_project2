# ML_CS_project2

We have r different folders : 

data : 	In this folder we have the initial data and the preprocessed data. 
	We also have the different embedded matrix (the one obtained with the method in class and the one obtain using glove dataset. 

pre-processing : 	In this folder we have all the jupyter file to pre-processed the data and get our training features. 
			clean_text : we pre-process the text to get simpler sentence (remove punctuation, stop word, lower case, lemmatization)
			tokenizer_embedding: we create the embedding matrix and the tokenizer (convert word to int) 

model : folder where we save all our model compute 
	model_LSTM should be run on google colab so that we can use the GPU and compute our model faster, the cvs file is directly created at the end

run : file where we can run our linear model to obtain the .cvs file with our prediction. 

BERTfinetunedmodels: Jupyter notebooks of BERT models and variants. They are meant to be run on google TPUs- in order to run on CPU or GPU they code will need to be modified a little bit. Checkpoints happen a little under 10K steps.

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
