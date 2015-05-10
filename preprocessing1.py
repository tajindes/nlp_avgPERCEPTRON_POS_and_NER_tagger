import sys;
import glob;
import os;
import re;

outputfile = sys.argv[2];
file2 = open(outputfile, "w");
#fileNames =  glob.glob(sys.argv[1]+'/*');
pathvar = sys.argv[1];
dirs = os.listdir( pathvar )

#fileNames.sort();

#for name in fileNames:
for current_file in dirs:
	name = os.path.join(pathvar, current_file);
#	print ("name is :", name);
	path = re.search('/(.+?).[0-9]+.txt', name).group(1);
#	print("path is :" , path);
	index = path.rfind('/');
	index = index+1;

	file1 = open(name, 'r', errors='ignore')
	lines  = file1.readlines()
	str_temp = ' '.join([line.strip() for line in lines]);

	str_temp = re.sub('[^A-Za-z0-9\@\$_\s-]+','',str_temp);		
#	str_temp = str_temp.lower();

	file1.close();

#	print ("name is :",path, "index is:", found,"done");
#	print ("substring is :", path[index:]);
	if (index != 0):
		file2.write(path[index:] + " " + str_temp +"\n");
#	else:
#		file2.write("TEST " + str_temp + "\n");
file2.close();
