Name: Tajinder Singh

# Steps for Perceptron:
	1. Use preprocessing1.py to convert TRAINING_DATA to TRAINING_FILE (spam_training.txt)

					python3 preprocessing1.py SPAM_TRAINING_PATH spam_training.txt

	2. Use preprocessing2.py to convert TEST_DATA to TEST_FILE (spam_test.txt)

					python3 preprocessing2.py SPAM_TEST_PATH spam_test.txt

	3. Then execute perceplearn.py to create MODEL_FILE (spam.nb) from TRAINING_FILE (spam_training.txt)

					python3 perceplearn.py spam_training.txt spam.nb

	4. Then execute percepclassify.py to create OUTPUT_FILE (spam.out) using TEST_FILE (spam_test.txt) and MODEL_FILE (spam.nb) 

					python3 percepclassify.py spam.nb < spam_test.txt > spam.out

	5. The final output file is spam.out

# Steps for POS Tagger:
	1. Run postrain.py script to create MODEL_FILE (pos.model) from TRAINING_FILE (train.pos)

					python3 postrain.py TRAININGFILE MODEL

	2. Run postag.py script to tag testdata using MODEL_FILE (pos.model) 
		
					python3 postag.py pos.model < pos.blind.test > pos.test.out

	3. The final output file is pos.test.out


# Steps for NER Tagger:
	1. Run nelearn.py script to create MODEL_FILE (ner.model) from TRAINING_FILE (ner.esp.train)

					python3 nelearn.py ner.esp.train ner.model

	2. Run netag.py script to tag TEST_DATA (ner.esp.blind.test) using MODEL_FILE (ner.model) 
		
					python3 netag.py ner.model < ner.esp.blind.test > ner.esp.test.out

	3. The final output file is pos.test.out


# Accuracy of your part-of-speech tagger:
		
			Accuracy: 94.810		


# Precision, recall and F-score for each of the named entity types for the named entity recognizer, and the overall F-score:
				
				Overall Accuracy: 92.02
				
				LOC : 
				Precision: 0.7423
				Recall: 0.6382
				F-Score: 70.1


				PER: 
				Precision: 0.8225
				Recall: 0.6563
				F-Score: 74.5


				ORG:
				Precision: 0.820
				Recall: 0.62
				F-Score: 71.75

				MISC:
				Precision: 0.66
				Recall: 0.4879
				F-Score: 58.4

				Overall F-score: 68.68

				