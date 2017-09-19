import csv
import json
from shutil import copyfile

csvfile = open('numbers.csv', 'r')
csvreader = csv.reader(csvfile, delimiter=';', quotechar='\n')
for row in csvreader:
	jsonfilename1 = "examplerequest1_"+str(row[0])+".json"
	jsonfilename2 = "examplerequest2_"+str(row[1])+".json"
	jsonfilename3 = "examplerequest3_"+str(row[2])+".json"
	jsonfilename4 = "examplerequest4_"+str(row[3])+".json"
	jsonfilename5 = "examplerequest5_"+str(row[4])+".json"
	
	jsonfile1 = open(jsonfilename1, 'w')
	jsonfile2 = open(jsonfilename2, 'w')
	jsonfile3 = open(jsonfilename3, 'w')
	jsonfile4 = open(jsonfilename4, 'w')
	jsonfile5 = open(jsonfilename5, 'w')
	
	ojsonfile1 = open('examplerequest1.json', 'r')
	ojsonfile2 = open('examplerequest2.json', 'r')
	ojsonfile3 = open('examplerequest3.json', 'r')
	ojsonfile4 = open('examplerequest4.json', 'r')
	ojsonfile5 = open('examplerequest5.json', 'r')
	
	data1 = json.load(ojsonfile1)
	data2 = json.load(ojsonfile2)
	data3 = json.load(ojsonfile3)
	data4 = json.load(ojsonfile4)
	data5 = json.load(ojsonfile5)
	
	data1['Parcel']['PSM']['TrackingId'] = 'J18CBEZ903N0303'+str(row[0])+'N'
	data2['Parcel']['PSM']['TrackingId'] = 'J18CBEZ903N0303'+str(row[1])+'N'
	data3['Parcel']['PSM']['TrackingId'] = 'J18CBEZ903N0303'+str(row[2])+'N'
	data4['Parcel']['PSM']['TrackingId'] = 'J18CBEZ903N0303'+str(row[3])+'N'
	data5['Parcel']['PSM']['TrackingId'] = 'J18CBEZ903N0303'+str(row[4])+'N'
	
	json.dump(data1, jsonfile1, indent=4)
	json.dump(data2, jsonfile2, indent=4)
	json.dump(data3, jsonfile3, indent=4)
	json.dump(data4, jsonfile4, indent=4)
	json.dump(data5, jsonfile5, indent=4)
	
	jsonfile1.close()
	jsonfile2.close()
	jsonfile3.close()
	jsonfile4.close()
	jsonfile5.close()
	ojsonfile1.close()
	ojsonfile2.close()
	ojsonfile3.close()
	ojsonfile4.close()
	ojsonfile5.close()