import sys;
import ast;
from sys import stdin;
import codecs;
try:
    import cPickle as pickle
except:
    import pickle


modelfile = sys.argv[1];
file1 = open(modelfile, "rb");
weight_dict = pickle.load(file1);
file1.close();
class_set = set();
percepclassify_inputlist = list();

for item_key in weight_dict:
	class_set.add(item_key);

stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore');

line = stdin.readline();
while(line):
	line = line.strip();
	line = "sword/stag/ " + line + " eword/etag/";
	dummy_string = "";
	temp_list = line.split();
	prev_ner_tag = "";
	dummy_str = "";
	for i in range(1, len(temp_list)-1):		
		curr_pos_index = temp_list[i].rfind("/");
		prev_pos_index = temp_list[i-1].rfind("/");
		next_pos_index = temp_list[i+1].rfind("/");
		dummy_str = "pn_" + prev_ner_tag + " " + "pp_" + str((temp_list[i-1])[prev_pos_index+1:]) + " "  + "cp_" + str((temp_list[i])[curr_pos_index+1:]) + " " + "prev_" + str((temp_list[i-1])[:prev_pos_index]) + " " + str((temp_list[i])[:curr_pos_index]) + " " + "next_" + str((temp_list[i+1])[:next_pos_index])+" " + "s2_" + str((temp_list[i])[-2:]);	
		dummy_list = dummy_str.split();

		eachline_dict = { };

		for item_key in class_set:
			eachline_dict[item_key] = 0;

		for temp_word in dummy_list:
			for temp_class in class_set:
				if(temp_word in weight_dict[temp_class]):
					eachline_dict[temp_class] = eachline_dict[temp_class] + (weight_dict[temp_class])[temp_word];

		expected_class = max(eachline_dict, key=eachline_dict.get);
		prev_ner_tag = expected_class;
		dummy_string = dummy_string + str(temp_list[i]) +"/" + str(expected_class) + " ";

	del percepclassify_inputlist[:];
	sys.stdout.write(dummy_string + "\n");
	line = stdin.readline();
