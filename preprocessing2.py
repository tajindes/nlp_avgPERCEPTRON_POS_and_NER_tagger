import sys;
import glob;
import os;
import re;

outputfile = sys.argv[2];
file2 = open(outputfile, "w");
#fileNames =  glob.glob(sys.argv[1]+'/*');
pathvar = sys.argv[1];
dirs = sorted(os.listdir(pathvar));

#for name in fileNames:
for current_file in dirs:
	name = os.path.join(pathvar, current_file);

	file1 = open(name, 'r', errors='ignore')
	lines  = file1.readlines()
	str_temp = ' '.join([line.strip() for line in lines]);

	str_temp = re.sub('[^A-Za-z0-9\@\$_\s-]+','',str_temp);		

	file1.close();
	file2.write(str_temp +"\n");

file2.close();
