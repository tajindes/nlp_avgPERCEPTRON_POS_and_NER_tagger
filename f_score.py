import sys;
import glob;
import os;
import re;

outputfile = sys.argv[2];
file2 = open(outputfile, "r");
fileNames =  glob.glob(sys.argv[1]+'/*');
fileNames.sort();
#print("filenames are: " , str(fileNames));

p_correct_predicted = { };
p_tot_predicted = {};
r_correct_predicted = {};
r_tot_predicted = {};
class_set = set();
counter = 0;
line = file2.readline();

for name in fileNames:
	path = re.search('/(.+?).[0-9]+.txt', name).group(1);
	index = path.rfind('/');
	index = index+1;

	class_set.add(path[index:]);

	line = line.strip();
	
	if(line not in p_correct_predicted):
		p_correct_predicted[line] = 0;
	if(line not in p_tot_predicted):
		p_tot_predicted[line] = 0;

	if(path[index:] not in p_correct_predicted):
		p_correct_predicted[path[index:]] = 0;
	if(path[index:] not in p_tot_predicted):
		p_tot_predicted[path[index:]] = 0;

	if(line not in r_correct_predicted):
		r_correct_predicted[line] = 0;
	if(line not in r_tot_predicted):
		r_tot_predicted[line] = 0;

	if(path[index:] not in r_correct_predicted):
		r_correct_predicted[path[index:]] = 0;
	if(path[index:] not in r_tot_predicted):
		r_tot_predicted[path[index:]] = 0;
		
	if(counter < 5):
		print("line is:", line, "path[index:] is:", path[index:]);
		counter = counter + 1;

	if(line == path[index:]):
#		print ("hello");
		p_correct_predicted[line] =  p_correct_predicted[line] + 1;
		p_tot_predicted[line] = p_tot_predicted[line] +1;
		r_correct_predicted[line] = r_correct_predicted[line] + 1;
		r_tot_predicted[path[index:]] = r_tot_predicted[path[index:]] + 1;
	else:
		p_tot_predicted[line] = p_tot_predicted[line] +1;
		r_tot_predicted[path[index:]] = r_tot_predicted[path[index:]] + 1;

	line= file2.readline();


file2.close();

#print ("classes are", class_set);
temp_list = list(class_set);
for item in temp_list:
#	print("item is:", item);
	if(p_tot_predicted[item] ==0):
		p_tot_predicted[item] = 1;

	if(r_tot_predicted[item] ==0):
		r_tot_predicted[item] = 1;

	print("precision for class", item, " is:", p_correct_predicted[item]/p_tot_predicted[item]);
	print("recall for class", item, " is:", r_correct_predicted[item]/r_tot_predicted[item]);

	numerator = 2.0 * (p_correct_predicted[item]/p_tot_predicted[item])*(r_correct_predicted[item]/r_tot_predicted[item]);	
	denominator =  (p_correct_predicted[item]/p_tot_predicted[item]) + (r_correct_predicted[item]/r_tot_predicted[item]);	
#	if(denominator == 0):
#		denominator = 1;
	f_score = numerator/denominator;
	print("F-SCORE for class", item, " is:",f_score); 
	

''' 
	print ("new class is :", item);
	print ("p_tot_predicted", p_tot_predicted[item]);
	print ("p_correct_predicted", p_correct_predicted[item]);
	print ("r_tot_predicted", r_tot_predicted[item]);
	print ("r_correct_predicted", r_correct_predicted[item]);
'''
	
