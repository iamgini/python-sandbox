import socket

addr1 = socket.gethostbyname('google.com')
addr2 = socket.gethostbyname('yahoo.com')

print(addr1, addr2)

socket.get
def pinghost(hostname):
    command_line = "/bin/ping -c1 " + hostname
    args = shlex.split(command_line)
    #p = subprocess.Popen(['/bin/ping ',hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        elif (output. ('Ping request could not find host')) :
            pingStatus = 'host_not_found'
            break
        if (output.startswith('Request timed out.')) :
            #No Echo Reply messages were received within the default time of 1 second.
            pingStatus = 'timed_out'
            break
        #end if
    #endFor
    return pingStatus
#endDef
