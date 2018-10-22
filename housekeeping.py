import datetime
import argparse
import json

def get_time():
	time = datetime.datetime.now()
	return time

def list_entries():
	switches_file = open('hk_switches.txt', 'r')
	entry = switches_file.read()
	switch = json.loads(entry)
	switches_file.close()
	return switch

def start_gui():
	print ('The GUI should be loaded here')
        
if (__name__ == "__main__"):

	parser = argparse.ArgumentParser( description='Perform Housekeeping tasks');
	
	parser.add_argument('--time', action='store_true',	help = 'get the actual time')
	parser.add_argument('--gui', action='store_true',	help = 'start GUI')
	parser.add_argument('--list', action='store_true',	help = 'list switches table')
	
	args = parser.parse_args()

	if (args.time == True):
		print (get_time())
		
	if (args.list == True):
            list = list_entries()
            for switch in list:
               print (switch)
	
	if (args.gui == True):
		start_gui()
	
	