import datetime
import argparse
import json
#############################################################
class switch():
	def __init__(self,plist):
		time_format = "%Y-%m-%d %H:%M:%S.%f"
		self.ip 		= plist[0]
		self.port 		= plist[1]
		self.name		= plist[2]
		self.type		= plist[3]
		self.interval	= datetime.timedelta(seconds=plist[4])
		self.duration	= datetime.timedelta(seconds=plist[5])
		self.starting	= datetime.datetime.strptime(plist[6],time_format)
		self.stopping	= datetime.datetime.strptime(plist[7],time_format)
		self.power		= plist[8]
		self.opened_at	= datetime.datetime.strptime("1970-01-01 00:00:00.000000",time_format)
		self.closed_at	= datetime.datetime.strptime("1970-01-01 00:00:10.000000",time_format)
		self.status 	= False 
	def Close(self):
		if (self.status == True):
			print("Put here the Code to close switch:", self.name)
			closed_at = datetime.datetime.now()
			self.status = False
		
	def Open(self):
		if (self.status == False):
			print("Put here the Code to open switch:", self.name)
			opened_at = datetime.datetime.now()
			self.status = True
		
#############################################################
def get_time():
	time = datetime.datetime.now()
	return time

def build_switch_list():
	switches_file = open('hk_switches.txt', 'r')
	swfile = switches_file.read()
	switches = json.loads(swfile)
	switches_file.close()
	switch_list = []
	for entry in switches:
		switch_list.append(switch (entry))
	return switch_list
	


def start_gui():
	print ('The GUI should be loaded here')
        
if (__name__ == "__main__"):

	parser = argparse.ArgumentParser( description='Perform Housekeeping tasks');
	
	parser.add_argument('--time', action='store_true',	help = 'get the actual time')
	parser.add_argument('--gui', action='store_true',	help = 'start GUI')
	parser.add_argument('--list', action='store_true',	help = 'list switches table')
	parser.add_argument('--stop', action='store_true',	help = 'opens all the switches')
	
	args = parser.parse_args()
	
	######################
	switches_list = build_switch_list()
	######################

	if (args.time == True):
		print (get_time())
		
	if (args.list == True):
		for switch in switches_list:
			print (switch)
	
	if (args.gui == True):
		start_gui()
	
	######################
	while (True):
		now = get_time()
		for switch in switches_list:
			if (switch.starting < now and now < switch.stopping):
				if ((now - switch.opened_at) > switch.interval and (now - switch.opened_at)%switch.interval < switch.duration):
					switch.Open()
				else:
					switch.Close()
			else:
				switch.Close()
		
	
	
	