import sys;
import ast;
from sys import stdin;
try:
    import cPickle as pickle
except:
    import pickle



inputfile = sys.argv[1];
file1 = open(inputfile, "rb");
#weight_dict = file1.readline();
weight_dict = pickle.load(file1);

file1.close();

class_set = set();

#print ("type of weight_dict is:", type(weight_dict));

#weight_dict = ast.literal_eval(weight_dict);
for item_key in weight_dict:
	class_set.add(item_key);

line = stdin.readline();
while(line):
	line = line.strip();
	temp_list = line.split();

	eachline_dict = { };

	for item_key in class_set:
		eachline_dict[item_key] = 0;

#	print ("before procesing eachline_dict is: ", eachline_dict);


	for temp_word in temp_list:
		for temp_class in class_set:
			if(temp_word in weight_dict[temp_class]):
				eachline_dict[temp_class] = eachline_dict[temp_class] + (weight_dict[temp_class])[temp_word];

#	print ("eachline_dict is: ", eachline_dict);

	expected_class = max(eachline_dict, key=eachline_dict.get);

#	print ("expected_class is: ", expected_class);

	sys.stdout.write(str(expected_class) + "\n");

	line = stdin.readline();

