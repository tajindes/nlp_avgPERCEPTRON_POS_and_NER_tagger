import sys;
import subprocess;

inputfile = sys.argv[1];
file1 = open(inputfile, "r",errors='ignore');
file2 = open("tempfile.txt", "w");
outputfile = sys.argv[2];
line = file1.readline();
perceplearn_inputlist = list();

while(line):
	line = line.strip();
	line = "sword/stag " + line + " eword/etag";

	temp_list = line.split();

	for i in range(1, len(temp_list)-1):
		current_index = temp_list[i].rfind("/");
		prev_index = temp_list[i-1].rfind("/");
		next_index = temp_list[i+1].rfind("/");
		tempindex = current_index;
		if(current_index -2 < 0):
			tempindex = 2;

		file2.write(str((temp_list[i])[current_index+1:]) + " " + "p_" + str((temp_list[i-1])[prev_index+1:]) + " " + "prev_" + str((temp_list[i-1])[:prev_index]) + " " + 
			str((temp_list[i])[:current_index]) + " " + "next_" + str((temp_list[i+1])[:next_index]) + " " + "s2_" + str((temp_list[i])[tempindex-2:current_index]) + "\n");	

	line = file1.readline();	

file1.close();
file2.close();

sts = subprocess.call(["python3","../perceplearn.py","tempfile.txt", str(outputfile)]);

print("done");



