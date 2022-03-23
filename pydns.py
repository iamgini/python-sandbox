# Version 2.2.0 - net.gini@gmail.com
import os
import socket
import subprocess, shlex

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' #no color
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INFO='\033[0;36m'
myfilename = 'ping.txt'

def pinghost(hostname):
    command_line = "/bin/ping -c1 " + hostname
    args = shlex.split(command_line)
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pingStatus = 'ok';	
    for line in p.stdout:
        output = line.rstrip().decode('UTF-8')
        if (output.endswith('unreachable.')) :
            #No route from the local system. Packets sent were never put on the wire.
            pingStatus = 'unreacheable'
            break
        elif (output.startswith('Ping request could not find host')) :
            pingStatus = 'host_not_found'
            break
        elif ('unknown' in output ) :
            pingStatus = 'host_not_found'
            break
        elif (output.startswith('1 packets transmitted, 0 received')) :
            pingStatus = 'no'
            break
        if (output.startswith('Request timed out.')) :
            #No Echo Reply messages were received within the default time of 1 second.
            pingStatus = 'timed_out'
            break
        #end if
    #endFor
    return pingStatus
#endDef    

print (bcolors.INFO + 'DNS Test - ver 2.2.0.\n' + bcolors.ENDC)
timestart = "$(date)"
counter = 0
pingcount = 0
dnscount = 0
nodnscount = 0
print (bcolors.OKBLUE + bcolors.UNDERLINE +'%-4s |%-18s |%-6s |%s' % ('No.',"Hostname","Ping","STATUS") + bcolors.ENDC)
with open(myfilename,mode='r') as varfile:
  for line in varfile:
    counter = counter + 1
    line = line.replace('\n','')
    try:
      startcolor = bcolors.OKGREEN
      statusText2 = ''
      addr = socket.gethostbyname(line)
      pingresp = pinghost(addr)
      if addr:
        fqdn = socket.getfqdn(line) 
        dnscount = dnscount + 1
        if pingresp == 'ok':
          pingcount = pingcount + 1
        else:
          startcolor = bcolors.WARNING
          statusText2 = bcolors.FAIL + '[host not reachable]'
      pingResponse = pingresp
      statusText = fqdn + ',' + addr + statusText2
    except IOError:
      nodnscount = nodnscount + 1
      statusText = 'NO DNS Entry Found'
      pingResponse = 'na'
      startcolor = bcolors.FAIL
    #else:
      #print 'Done'
    finally:
      print (startcolor + '%-4s |%-18s |%-6s |%s' % ( counter ,line,pingResponse,statusText) + bcolors.ENDC)

varfile.close() #close the file

timeend = "$(date)"
print (bcolors.OKBLUE + "\n======================== Summary ======================================" + bcolors.ENDC)
print (bcolors.OKGREEN , dnscount , "with DNS |" + bcolors.WARNING , nodnscount , "without DNS |" + bcolors.OKGREEN , pingcount , " reachable" + bcolors.ENDC)
