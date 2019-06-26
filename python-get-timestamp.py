from datetime import datetime as datettimestamp

def get_time_stamp():
  DATEFORMAT = '%Y%m%d:%H:%M:%S'
  dtstamp = datettimestamp.now().strftime(DATEFORMAT)
  return dtstamp

dst = get_time_stamp()
print (dst)