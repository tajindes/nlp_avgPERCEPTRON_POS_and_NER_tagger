import sys;
from collections import Counter;
try:
    import cPickle as pickle
except:
    import pickle


inputfile = sys.argv[1];
file1 = open(inputfile, "r",errors='ignore');
outputfile = sys.argv[2];

#vocabulary = set();
class_set = set();
weight_dict = { };
dummy_dict = { };
average_percept_dict = { };
error_dict = { };
iterations = 20;
current_iteration = 1;
while(current_iteration <= iterations):
	print("current iteration number is:", current_iteration);
	line = file1.readline();
	current_iteration = current_iteration + 1;
	total_predictions = 0.0;
	correct_predictions = 0.0;
	linenumber = 0;
	while(line):
		linenumber = linenumber + 1;
		line = line.strip();
		temp_list = line.split();
		generic_class = temp_list[0];
		eachline_dict = {};

		if(generic_class not in class_set):
			class_set.add(generic_class);
			weight_dict[generic_class] = { };
			dummy_dict[generic_class] = { };

		for item in class_set:
			eachline_dict[item] = 0;

		for i in range(1, len(temp_list)):
			for temp_class in class_set:
				if (temp_list[i] not in weight_dict[temp_class]):
					(weight_dict[temp_class])[temp_list[i]] = 0;
					(dummy_dict[temp_class])[temp_list[i]] = 0;
				else:
					eachline_dict[temp_class] = eachline_dict[temp_class] + (weight_dict[temp_class])[temp_list[i]]

		expected_class = max(eachline_dict, key=eachline_dict.get);

		#print("part1 done");

		if(expected_class != generic_class):
			for i in range(1, len(temp_list)):
				(weight_dict[expected_class])[temp_list[i]] =  (weight_dict[expected_class])[temp_list[i]] - 1.0; 
				(weight_dict[generic_class])[temp_list[i]] =  (weight_dict[generic_class])[temp_list[i]] + 1.0; 

		line = file1.readline();

	for temp_class in class_set:
		for dict_key in weight_dict[temp_class]: # or for dict_key in dummy_dict
			(dummy_dict[temp_class])[dict_key] = (dummy_dict[temp_class])[dict_key] + (weight_dict[temp_class])[dict_key]

	file1.seek(0);

for temp_class in class_set:
	for dict_key in weight_dict[temp_class]: # or for dict_key in dummy_dict
		(dummy_dict[temp_class])[dict_key] = (dummy_dict[temp_class])[dict_key]/iterations;

file1.close();


file2  =open(outputfile, "wb");
#file2.write(str(dummy_dict));
pickle.dump(dummy_dict, file2);
file2.close();
