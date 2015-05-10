import sys;
import subprocess;

inputfile = sys.argv[1];
file1 = open(inputfile, "r",errors='ignore');
file2 = open("nertempfile.txt", "w");
outputfile = sys.argv[2];
line = file1.readline();
perceplearn_inputlist = list();

while(line):
	line = line.strip();
	line = "startstart/ " + line + " endend/";

	temp_list = line.split();

	for i in range(1, len(temp_list)-1):
		current_ner_index = temp_list[i].rfind("/");
		current_pos_index = temp_list[i].rfind("/", 0, current_ner_index);
		
		prev_ner_index = temp_list[i-1].rfind("/");
		prev_pos_index = temp_list[i-1].rfind("/", 0, prev_ner_index);		
		
		next_ner_index = temp_list[i+1].rfind("/");
		next_pos_index = temp_list[i+1].rfind("/", 0, next_ner_index);
		
		file2.write(str((temp_list[i])[current_ner_index+1:]) + " " + "pn_" + str((temp_list[i-1])[prev_ner_index+1:]) + " " + "pp_" + str((temp_list[i-1])[prev_pos_index+1:prev_ner_index]) + " " + 
			"cp_" + str((temp_list[i])[current_pos_index+1:current_ner_index]) + " " +  "prev_" + str((temp_list[i-1])[:prev_pos_index]) + " " + str((temp_list[i])[:current_pos_index]) + " " + "next_" + 
			str((temp_list[i+1])[:next_pos_index]) + "\n");

	line = file1.readline();	


file1.close();
file2.close();

sts = subprocess.call(["python3","../perceplearn.py", "nertempfile.txt", str(outputfile)]);



