

def ar_data_split(nmea):
	UTMLat=0
	UTMLon=0
	bearing=0
	nmea = nmea.split(",")
	#TODO: would be better to use regex instead of split for error handling
	if len(nmea)<3:
		print "error invalid input"
		#if unknown return lat,lon as 0,0 which is a valid cordinate but you will notice the error unless you are in Grewnich
		return 0,0,0
	if len(nmea)==3 and nmea[0]:
	 
	 UTMLats,UTMLons,bearings = nmea[0:3]
      
	 #if type is GPRMC calculate lat,lon
	
	 UTMLat=float(UTMLats)
	 UTMLon=float(UTMLons)
	 bearing=int(bearings)
	return UTMLat,UTMLon,bearing
