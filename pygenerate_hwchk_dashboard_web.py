# Version 2.1.0 - gineesh.mada-pparambath@t-systems.com
# This was written in bash and later converted to python as part of improvement. 
# Should be run on central controlnode only - amsd2a-n-s00008
import random
import string
#import wget
#import urllib.request
#import urllib2
import requests
import os

#import ast

RANDOM_oa_output = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_oa_output_all = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_cnlist = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_indcndata = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_datafromcn = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_bladedatafromcn = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_bladedata = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_bladedata_file = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
RANDOM_bladedata1 = "/tmp/" + ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
#print "RANDOM_oa_output - " + RANDOM_oa_output + "\nRANDOM_oa_output_all - " + RANDOM_oa_output_all +  "\nRANDOM_cnlist - "  + RANDOM_cnlist + "\nRANDOM_indcndata - "  + RANDOM_indcndata + "\nRANDOM_bladedata - " + RANDOM_bladedata +  "\nRANDOM_bladedata1 - " + RANDOM_bladedata1 + "\nRANDOM_bladedata_file - " + RANDOM_bladedata_file

# function to touch a file 
def create_empty_file(filename):
  with open(filename, 'wb') as temp_file:
    temp_file.write(' ')
    #print filename + " Created"
    return True
#result = create_empty_file(RANDOM_bladedata_file)

WEBURLFILE="/var/www/html/hwchk/allbchw-dashboard-beta.html"
WEBURLJS="/var/www/html/hwchk/js/Chart.min.js"
WEBURLJSDYNAMIC="/var/www/html/hwchk/js/Chart-data-dynamic-2.js"

# list of controlndoes
controlnodes = [
  "abe-a-rgs1.europe.shell.com",
  "amsd2a-a-rgs2.europe.shell.com",
  "anaans-a-rgs1.europe.shell.com",
  "ass-a-rgs1.europe.shell.com",
  "bejdc1-a-rgs1.asia-pac.shell.com",
  "bngsti-a-rgs1.asia-pac.shell.com",
  "bripld-a-rgs1.asia-pac.shell.com",
  "caihas-a-rgs1.africa-me.shell.com",
  "calbdc-a-rgs1.americas.shell.com",
  "calrbq-a-rgs1.americas.shell.com",
  "cbj-n-s00005.asia-pac.shell.com",
  "dohqsr-n-s00019.africa-me.shell.com",
  "houcy1-a-rgs1.americas.shell.com",
  "houic-n-s00169.americas.shell.com",
  "jak-a-rgs1.asia-pac.shell.com",
  "mownov-a-rgs1.europe.shell.com",
  "mussdo-a-rgs1.africa-me.shell.com",
  "npl-a-rgs1.asia-pac.shell.com",
  "pejjbt-a-rgs1.asia-pac.shell.com",
  "pfncli-a-rgs1.americas.shell.com",
  "pth-a-rgs1.asia-pac.shell.com",
  "riosed-a-rgs1.americas.shell.com",
  "ris-a-rgs1.europe.shell.com",
  "scz-a-rgs1.americas.shell.com",
  "tunidl-a-rgs1.africa-me.shell.com",
  "yuzdze-a-rgs1.europe.shell.com",
]
#print controlnodes
# add a color array
array_color = [
	"rgba(102, 255, 153, 0.9\)",
	"rgba(255, 0, 102, 0.9\)",
	"rgba(0, 153, 204, 0.9\)",
	"rgba(77, 153, 0, 0.9\)",
	"rgba(0, 0, 153, 0.9\)",
	"rgba(153, 77, 0, 0.9\)",
	"rgba(0, 153, 38, 0.9\)",
	"rgba(0, 153, 153, 0.9\)",
	"rgba(204, 153, 0, 0.9\)",
	"rgba(102, 0, 204, 0.9\)",
	"rgba(204, 204, 0, 0.9\)",
	"rgba(102, 0, 0, 0.9\)",
	"rgba(172, 230, 0, 0.9\)",
	"rgba(255, 153, 0, 0.9\)",
	"rgba(0, 32, 128, 0.9\)",
	"rgba(204, 102, 153, 0.9\)",
	"rgba(0, 230, 230, 0.9\)",
	"rgba(0, 0, 51, 0.9\)",
	"rgba(255, 51, 0, 0.9\)",
	"rgba(102, 255, 153, 0.9\)",
	"rgba(255, 128, 223, 0.9\)",
	"rgba(153, 194, 255, 0.9\)",
	"rgba(51, 153, 255, 0.9\)",
	"rgba(119, 179, 0, 0.9\)",
	"rgba(255, 163, 26, 0.9\)",
	"rgba(0, 51, 0, 0.9\)",
	"rgba(255, 64, 0, 0.9\)",
	"rgba(0, 0, 255, 0.9\)",
	"rgba(153, 51, 102, 0.9\)",
	"rgba(123, 10, 2, 0.9\)",
	"rgba(255, 140, 12, 0.9\)",
	"rgba(200, 0, 0, 0.9\)",
	"rgba(10, 0, 200, 0.9\)",
	"rgba(172, 230, 0, 0.9\)",
	"rgba(255, 153, 0, 0.9\)",
	"rgba(0, 32, 128, 0.9\)",
	"rgba(204, 102, 153, 0.9\)",
	"rgba(0, 230, 230, 0.9\)",
	"rgba(0, 0, 51, 0.9\)",
	"rgba(255, 51, 0, 0.9\)",
	"rgba(102, 255, 153, 0.9\)",
	"rgba(255, 128, 223, 0.9\)",
	"rgba(153, 194, 255, 0.9\)",
]
#print array_color

##
NODNSCOUNT=0
LOGDECOM=""
BCNOTREACHABLE=""
NOACCESSCOUNT=0
ACCESSCOUNT=0
PHYDECOM=""
ACTIVEBC=""
##

##touch $WEBURLFILE
##touch $WEBURLJSDYNAMIC

# print/collect details to dynamic-js
WEBURLJSDYNAMIC_data = "var config = {\n"
WEBURLJSDYNAMIC_data = WEBURLJSDYNAMIC_data + "\ttype: 'doughnut',\n"
WEBURLJSDYNAMIC_data = WEBURLJSDYNAMIC_data + "\tdata: {\n"
WEBURLJSDYNAMIC_data = WEBURLJSDYNAMIC_data + "\t\tdatasets: [{\n"
WEBURLJSDYNAMIC_data = WEBURLJSDYNAMIC_data + "\t\t\tdata: [\n"

from datetime import datetime
date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #"$(date)"
WEBURLFILE_data = ""
WEBURLFILE_data = WEBURLFILE_data + "<html><Title>Central Dashboard (AMS) | VWS Hardware Report <Dev> </Title>\n"
WEBURLFILE_data = WEBURLFILE_data + "<style>\n"
WEBURLFILE_data = WEBURLFILE_data + "@font-face {\n"
WEBURLFILE_data = WEBURLFILE_data + "\tfont-family: \'Roboto\';\n"
WEBURLFILE_data = WEBURLFILE_data + "\tfont-style: normal;\n"
WEBURLFILE_data = WEBURLFILE_data + "\tfont-weight: 700;\n"
WEBURLFILE_data = WEBURLFILE_data + "\tsrc: local(\'Roboto Bold\'), local(\'Roboto-Bold\'), url(fonts/Roboto-700.woff2) format(\'woff2\');\n"
WEBURLFILE_data = WEBURLFILE_data + "}\n"
WEBURLFILE_data = WEBURLFILE_data + "@font-face {\n"
WEBURLFILE_data = WEBURLFILE_data + "\tfont-family: \'Roboto\';\n"
WEBURLFILE_data = WEBURLFILE_data + "\tfont-style: normal;\n"
WEBURLFILE_data = WEBURLFILE_data + "\tfont-weight: 400;\n"
WEBURLFILE_data = WEBURLFILE_data + "\tsrc: local(\'Roboto\'), local(\'Roboto-Regular\'), url(fonts/Roboto-400.woff2) format(\'woff2\');\n"
WEBURLFILE_data = WEBURLFILE_data + "}\n"

WEBURLFILE_data = WEBURLFILE_data + "body { font-family: Roboto, Arial, Tahoma, Consolas, Arial, Tahoma, sans-serif; font-size: 9px; background-color: #eee ;padding: 0px; margin: 0px}\n"
WEBURLFILE_data = WEBURLFILE_data + "hr { border: 1px dotted #dddddd; }\n"
WEBURLFILE_data = WEBURLFILE_data + "h1, h2, h3, h4, h5 { margin: 5px; }\n"
WEBURLFILE_data = WEBURLFILE_data + "table, tr, td { border-bottom: 1px solid #eeeeee; border-spacing: 5px; font-family: Roboto, Arial, Tahoma, Consolas, Arial; font-size: 12px;}\n"
WEBURLFILE_data = WEBURLFILE_data + ".toptable { border: 0px solid #dddddd; padding: 5px;vertical-align: text-top; border-spacing: 0px; margin: 0px; text-align=right; font-family: Roboto, Arial, Tahoma, Consolas, Arial; font-size: 12px; }"
WEBURLFILE_data = WEBURLFILE_data + "</style>\n"
WEBURLFILE_data = WEBURLFILE_data + "<script src=\"js/Chart.min.js\"></script>\n"
WEBURLFILE_data = WEBURLFILE_data + "<body>\n"

WEBURLFILE_data = WEBURLFILE_data + "<div style=\"background-color: #fff; width: auto; padding: 5px; margin-top: 0px; border-bottom: 1px solid #ddd; padding-left: 20px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h1>Central Dashboard | VWS Asset Report</h1>\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"

WEBURLFILE_data = WEBURLFILE_data + "<div style=\"padding-left: 20px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h2><font color=green>Global Summary</font>\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
# load dynamic data
WEBURLFILE_data = WEBURLFILE_data + "<script src=\"js/Chart-data-dynamic-2.js\"></script>\n"

# Collect this header to a new variable
WEBURLFILE_data_header = WEBURLFILE_data
WEBURLFILE_data = ""


# start outer table
WEBURLFILE_data = WEBURLFILE_data + "<table style=\"width: 100%; padding: 0px;border: 0px solid #dddddd\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<tr>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td style=\"width: 60%; border: 0px\" valign=top>\n"
# show chart
WEBURLFILE_data = WEBURLFILE_data + "<div id=\"canvas-holder\" style=\"width: auto; padding: 15px; border: 1px solid #ddd; background-color: #fff; margin: 10px; margin-right: 5px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h1>Hardware Scan Data</h1>\n"
WEBURLFILE_data = WEBURLFILE_data + "<h2>Active Blades</h2>\n"
WEBURLFILE_data = WEBURLFILE_data + "\t<canvas id=\"chart-area\" />\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
# show chart 2
WEBURLFILE_data = WEBURLFILE_data + "<div id=\"canvas-holder1\" style=\"width: auto; padding: 15px; border: 1px solid #ddd; background-color: #fff; margin: 10px; margin-right: 5px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h2>Active Enclosures</h2>\n"
WEBURLFILE_data = WEBURLFILE_data + "\t<canvas id=\"chart-area1\" height=\"200\"/>\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
WEBURLFILE_data = WEBURLFILE_data + "</td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td style=\"width: 40%; border: 0px\" valign=\"top\">\n"
# show chart 3 - Host Type
WEBURLFILE_data = WEBURLFILE_data + "<div id=\"canvas-holder2\" style=\"width: auto; padding: 15px; border: 1px solid #ddd; background-color: #fff; margin: 10px; margin-left: 5px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h2>Host Types (DHCP Data)</h2>\n"
WEBURLFILE_data = WEBURLFILE_data + "\t<canvas id=\"chart-area2\" height=\"60\"/>\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
# show chart 4 - Status
WEBURLFILE_data = WEBURLFILE_data + "<div id=\"canvas-holder3\" style=\"width: auto; padding: 15px; border: 1px solid #ddd; background-color: #fff; margin: 10px; margin-left: 5px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h2>Blade Status (DHCP Data)</h2>\n"
WEBURLFILE_data = WEBURLFILE_data + "\t<canvas id=\"chart-area3\" height=\"100\" />\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
# show chart 5 - template
WEBURLFILE_data = WEBURLFILE_data + "<div id=\"canvas-holder4\" style=\"width: auto; padding: 15px; border: 1px solid #ddd; background-color: #fff; margin: 10px; margin-left: 5px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<h2>Templates Used (DHCP Data)</h2>\n"
WEBURLFILE_data = WEBURLFILE_data + "\t<canvas id=\"chart-area4\" />\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
WEBURLFILE_data = WEBURLFILE_data + "</td></tr>\n"
WEBURLFILE_data = WEBURLFILE_data + "</table>\n"
# closed outer table
WEBURLFILE_data = WEBURLFILE_data + "<script type=\"text/javascript\">\n"
WEBURLFILE_data = WEBURLFILE_data + "window.onload = function() {\n"
WEBURLFILE_data = WEBURLFILE_data + "\tvar ctx = document.getElementById(\"chart-area\").getContext(\"2d\");\n"
WEBURLFILE_data = WEBURLFILE_data + "\twindow.myPie = new Chart(ctx, config);\n"
WEBURLFILE_data = WEBURLFILE_data + "\tvar ctx1 = document.getElementById(\"chart-area1\").getContext(\"2d\");\n"
WEBURLFILE_data = WEBURLFILE_data + "\twindow.myPie = new Chart(ctx1, config1);\n"
WEBURLFILE_data = WEBURLFILE_data + "\tvar ctx2 = document.getElementById(\"chart-area2\").getContext(\"2d\");\n"
WEBURLFILE_data = WEBURLFILE_data + "\twindow.myPie = new Chart(ctx2, config2);\n"
WEBURLFILE_data = WEBURLFILE_data + "\tvar ctx3 = document.getElementById(\"chart-area3\").getContext(\"2d\");\n"
WEBURLFILE_data = WEBURLFILE_data + "\twindow.myPie = new Chart(ctx3, config3);\n"
WEBURLFILE_data = WEBURLFILE_data + "\tvar ctx4 = document.getElementById(\"chart-area4\").getContext(\"2d\");\n"
WEBURLFILE_data = WEBURLFILE_data + "\twindow.myPie = new Chart(ctx4, config4);\n"
WEBURLFILE_data = WEBURLFILE_data + "};\n"
WEBURLFILE_data = WEBURLFILE_data + "</script>\n"

WEBURLFILE_data = WEBURLFILE_data + "<div id=\"table-summary\" style=\"width: 95%; padding: 15px; border: 1px solid #ddd; background-color: #fff; margin: 15px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<br><table style=\"width: 100%; padding: 5px;border: 0px solid #dddddd\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<tr>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td>&nbsp</td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td><font color=black><b>RGS site(s)</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right><font color=black><b>Active BC(s)</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right><font color=black><b>Total Blades</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right><font color=black><b>Missing DNS <br>(Logical Decom)</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right><font color=black><b>BC NO Access <br>(Physc Decom)</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td><font color=black><b>Report Date</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td><font color=black><b>Individual Dashboards (Regions)</b></font></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "</tr>\n"

#print WEBURLJSDYNAMIC_data + WEBURLFILE_data
# get details from all CN and display in summary"
PARAM_ACCESSCOUNT_TOTAL=0
PARAM_TOTALBLADES_TOTAL=0
counter = 1
RANDOM_bladedata = ''
array_site = [] #empty array for rgs details
site_dict = {}
for cn in controlnodes:
  cn_url ="http://" + cn + "/hwchk/allbchw.html"
  cn_url_blade = "http://" + cn + "/hwchk/allblades"
  #filedata = urllib2.urlopen(cn_url, timeout = 60)
  #datatowrite = filedata.read()
  #with open(RANDOM_datafromcn, 'wb') as f:
  #    f.write(datatowrite)
  #with open(RANDOM_datafromcn,mode='r') as g:
  #    print(g.read())
  try:
    r = requests.get(cn_url, timeout = 10)
  except requests.exceptions.ConnectTimeout:
    r = requests.get("http://localhost/hwchk/noaccessrgs", timeout = 10)
    #print "\nCannot find ..... " + cn_url
  #print "\nGot it ..... " + cn_url

  with open(RANDOM_indcndata, 'wb') as f:
    f.write(r.content)
  #with open(RANDOM_datafromcn,mode='r') as g:
    #print(g.read())
  # Retrieve HTTP meta-data
  #print(r.status_code)  
  #print(r.headers['content-type'])  
  #print(r.encoding) 

  # read the bladedata url
  try:
    blade_read = requests.get( cn_url_blade, timeout = 20 )
  except requests.exceptions.ConnectTimeout:
    print "\nCannot find ..... " + cn_url_blade
  # append bladedata for later use
  RANDOM_bladedata = RANDOM_bladedata + blade_read.content

  print cn_url
  # read the cndata and find the parameters
  PARAM_DATE = ''
  PARAM_RGSSITECODE = ''
  PARAM_ACCESSCOUNT = ''
  PARAM_TOTALBLADES = ''
  PARAM_NOACCESSCOUNT = ''

  for line in open(RANDOM_indcndata, 'r'):
    line = line.replace('\n','')
    line = line.replace('\"','')
    if 'param_date' in line:
      line_content = line.split(' ')
      line_content_data = line_content[3].replace('value=','')
      PARAM_DATE = line_content_data.replace('>','')

    if 'param_rgssitecode' in line:
      line_content = line.split(' ')
      line_content_data = line_content[3].replace('value=','')
      PARAM_RGSSITECODE = line_content_data.replace('>','')

    if 'param_activebc' in line:
      line_content = line.split(' ')
      line_content_data = line_content[3].replace('value=','')
      PARAM_ACCESSCOUNT = line_content_data.replace('>','')

    if 'param_totalblades' in line:
      line_content = line.split(' ')
      line_content_data = line_content[3].replace('value=','')
      PARAM_TOTALBLADES = line_content_data.replace('>','')

    if 'param_nodnscount' in line:
      line_content = line.split(' ')
      line_content_data = line_content[3].replace('value=','')
      PARAM_NODNSCOUNT = line_content_data.replace('>','')

    if 'param_noaccesscount' in line:
      line_content = line.split(' ')
      line_content_data = line_content[3].replace('value=','')
      PARAM_NOACCESSCOUNT = line_content_data.replace('>','')
      
      #print PARAM_DATE + PARAM_RGSSITECODE + PARAM_ACCESSCOUNT + PARAM_TOTALBLADES + PARAM_NOACCESSCOUNT
      site_dict[cn] = {'RGS':[PARAM_RGSSITECODE,PARAM_TOTALBLADES,PARAM_ACCESSCOUNT,PARAM_DATE,PARAM_NODNSCOUNT,PARAM_NOACCESSCOUNT]}
    
      # add row for the site in RGS table
      WEBURLFILE_data = WEBURLFILE_data + "<tr>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td align=right style=\"width: 5px; background-color: " + array_color[counter].replace('\\','')  + "\">&nbsp</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td>" + PARAM_RGSSITECODE + "</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td align=right>" + PARAM_ACCESSCOUNT + "</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td align=right>" + PARAM_TOTALBLADES + "</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td align=right>" + PARAM_NODNSCOUNT + "</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td align=right>" + PARAM_NOACCESSCOUNT + "</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td>" + PARAM_DATE + "</td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "<td><a href=\"http://" + cn + "/hwchk/allbchw.html\" target=\"_blank\">" + cn + "</a></td>\n"
      WEBURLFILE_data = WEBURLFILE_data + "</tr>\n"
      counter += 1
      # count total blades and active
      if PARAM_ACCESSCOUNT:
        # convert string to integer using int()
        PARAM_ACCESSCOUNT_TOTAL += int( PARAM_ACCESSCOUNT )
      if PARAM_ACCESSCOUNT:
        PARAM_TOTALBLADES_TOTAL += int( PARAM_TOTALBLADES )

# collect all bladedata to a file RANDOM_bladedata_file
with open(RANDOM_bladedata_file, mode='w') as blade_file:
  blade_file.write(RANDOM_bladedata)
with open("/var/www/html/hwchk/allbladesglobal", mode='w') as blade_file_global:
  blade_file_global.write(RANDOM_bladedata)

WEBURLFILE_data = WEBURLFILE_data + "<tr>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td>&nbsp</td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td><h2>Total</h2></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right><h2>" + str(PARAM_ACCESSCOUNT_TOTAL) + "</h2></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right><h2>" + str(PARAM_TOTALBLADES_TOTAL) + "</h2></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td align=right></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "<td></td>\n"
WEBURLFILE_data = WEBURLFILE_data + "</tr>\n"
WEBURLFILE_data = WEBURLFILE_data + "</table>\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"

# collect WEBURLFILE_data as content variable
WEBURLFILE_data_content = WEBURLFILE_data
WEBURLFILE_data = ""

# add jsfile content for active blades
for item in sorted(site_dict, key=lambda key: site_dict[key]):
  #print site_dict[item]
  #print site_dict[item]['RGS'][1]
  WEBURLJSDYNAMIC_data += "\t\t\t\t" + str(site_dict[item]['RGS'][1]) + ",\n"
WEBURLJSDYNAMIC_data += "\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tbackgroundColor: [\n"
array_counter = 1
for item in sorted(site_dict, key=lambda key: site_dict[key]):
  WEBURLJSDYNAMIC_data += "\t\t\t\t\'" + array_color[array_counter] + "\',\n" 
  array_counter += 1
WEBURLJSDYNAMIC_data += "\t\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tlabel: \'Dataset 1\'\n"
WEBURLJSDYNAMIC_data += "\t\t}],\n"
WEBURLJSDYNAMIC_data += "\t\tlabels: [\n"
array_counter=1
for item in sorted(site_dict, key=lambda key: site_dict[key]):
  WEBURLJSDYNAMIC_data += "\t\t\t\"" + site_dict[item]['RGS'][0] + "\[" + site_dict[item]['RGS'][1] + "\]\",\n"
WEBURLJSDYNAMIC_data += "\t\t\t]\n"
WEBURLJSDYNAMIC_data += "\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\toptions: {\n"
WEBURLJSDYNAMIC_data += "\t\t\tresponsive: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\tlegend: {\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tdisplay: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tposition: \'right\',\n"
WEBURLJSDYNAMIC_data += "\t\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\t\t}\n"
WEBURLJSDYNAMIC_data += "};\n"
WEBURLJSDYNAMIC_data += "\n"

#print details of 2nd chart [Active Enclosures] to dynamic-js
WEBURLJSDYNAMIC_data += "var config1 = {\n"
WEBURLJSDYNAMIC_data += "\ttype: 'horizontalBar',\n"
WEBURLJSDYNAMIC_data += "\tdata: {\n"
WEBURLJSDYNAMIC_data += "\t\tdatasets: [{\n"
WEBURLJSDYNAMIC_data += "\t\t\tdata: [\n"
for item in sorted(site_dict, key=lambda key: site_dict[key]):
  #print site_dict[item]
  WEBURLJSDYNAMIC_data += "\t\t\t\t" + str(site_dict[item]['RGS'][2]) + ",\n"
WEBURLJSDYNAMIC_data += "\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tbackgroundColor: [\n"
array_counter = 1
for item in sorted(site_dict, key=lambda key: site_dict[key]):
  WEBURLJSDYNAMIC_data += "\t\t\t\t\'" + array_color[array_counter] + "\',\n" 
  array_counter += 1
WEBURLJSDYNAMIC_data += "\t\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tlabel: \'Dataset 1\'\n"
WEBURLJSDYNAMIC_data += "\t\t}],\n"
WEBURLJSDYNAMIC_data += "\t\tlabels: [\n"
array_counter=1
for item in sorted(site_dict, key=lambda key: site_dict[key]):
  WEBURLJSDYNAMIC_data += "\t\t\t\"" + site_dict[item]['RGS'][0] + "\[" + site_dict[item]['RGS'][2] + "\]\",\n"
WEBURLJSDYNAMIC_data += "\t\t\t]\n"
WEBURLJSDYNAMIC_data += "\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\toptions: {\n"
WEBURLJSDYNAMIC_data += "\t\t\tresponsive: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\tlegend: {\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tdisplay: false,\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tposition: \'right\',\n"
WEBURLJSDYNAMIC_data += "\t\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\t\t}\n"
WEBURLJSDYNAMIC_data += "};\n"
WEBURLJSDYNAMIC_data += "\n"

# collect host-type, blade-status, template data from RANDOM_bladedata and save in lists
list_HostType = []
list_Blade_Status = []
list_Template = []
for item in RANDOM_bladedata.split("\n"):
  if 'decommissioned' not in item and 'out of operation' not in item:
    item_data = item.split(',')
    if not item.strip():
      #print "Blank"
      blank_str = "blankline"
    else:      
      item_data_value = item_data[1].split(":")
      list_HostType.append( item_data_value[1] )
      # check if any value missing and avoid out of reange error when fetching bladestatus
      if len(item_data) == 5:
        item_data_value = item_data[4].split(":")
        list_Blade_Status.append( item_data_value[1] )
      elif len(item_data) == 4:
        #print item_data
        item_data_value = item_data[3].split(":")
        list_Blade_Status.append( item_data_value[1] )

      item_data_value = item_data[2].split(":")
      list_Template.append( item_data_value[1] )

# collect unique values
mylist = set(list_HostType)
list_HostType_unique = list(mylist)
mylist = set(list_Blade_Status)
list_Blade_Status_unique = list(mylist)
mylist = set(list_Template)
list_Template_unique = list(mylist)

#print details of host-type [DHCP data] chart to dynamic-js
WEBURLJSDYNAMIC_data += "var config2 = {\n"
WEBURLJSDYNAMIC_data += "\ttype: 'horizontalBar',\n"
WEBURLJSDYNAMIC_data += "\tdata: {\n"
WEBURLJSDYNAMIC_data += "\t\tdatasets: [{\n"
WEBURLJSDYNAMIC_data += "\t\t\tdata: [\n"
for vwstype in range(len(list_HostType_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\t" + str(list_HostType.count(list_HostType_unique[vwstype])) + ",\n"
WEBURLJSDYNAMIC_data += "\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tbackgroundColor: [\n"
array_counter = 1
for vwstype in range(len(list_HostType_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\t\'" + array_color[array_counter] + "\',\n" 
  array_counter += 1
WEBURLJSDYNAMIC_data += "\t\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tlabel: \'Dataset 1\'\n"
WEBURLJSDYNAMIC_data += "\t\t}],\n"
WEBURLJSDYNAMIC_data += "\t\tlabels: [\n"
array_counter=1
for vwstype in range(len(list_HostType_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\"" + list_HostType_unique[vwstype] + "\[" + str(list_HostType.count(list_HostType_unique[vwstype])) + "\]\",\n"
WEBURLJSDYNAMIC_data += "\t\t\t]\n"
WEBURLJSDYNAMIC_data += "\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\toptions: {\n"
WEBURLJSDYNAMIC_data += "\t\t\tresponsive: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\tlegend: {\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tdisplay: false,\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tposition: \'left\',\n"
WEBURLJSDYNAMIC_data += "\t\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\t\t}\n"
WEBURLJSDYNAMIC_data += "};\n"
WEBURLJSDYNAMIC_data += "\n"

#print details of blade status [DHCP data] chart to dynamic-js
WEBURLJSDYNAMIC_data += "var config3 = {\n"
WEBURLJSDYNAMIC_data += "\ttype: 'horizontalBar',\n"
WEBURLJSDYNAMIC_data += "\tdata: {\n"
WEBURLJSDYNAMIC_data += "\t\tdatasets: [{\n"
WEBURLJSDYNAMIC_data += "\t\t\tdata: [\n"
for vwstype in range(len(list_Blade_Status_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\t" + str(list_Blade_Status.count(list_Blade_Status_unique[vwstype])) + ",\n"
WEBURLJSDYNAMIC_data += "\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tbackgroundColor: [\n"
array_counter = 1
for vwstype in range(len(list_Blade_Status_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\t\'" + array_color[array_counter] + "\',\n" 
  array_counter += 1
WEBURLJSDYNAMIC_data += "\t\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tlabel: \'Dataset 1\'\n"
WEBURLJSDYNAMIC_data += "\t\t}],\n"
WEBURLJSDYNAMIC_data += "\t\tlabels: [\n"
array_counter=1
for vwstype in range(len(list_Blade_Status_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\"" + list_Blade_Status_unique[vwstype] + "\[" + str(list_Blade_Status.count(list_Blade_Status_unique[vwstype])) + "\]\",\n"
WEBURLJSDYNAMIC_data += "\t\t\t]\n"
WEBURLJSDYNAMIC_data += "\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\toptions: {\n"
WEBURLJSDYNAMIC_data += "\t\t\tresponsive: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\tlegend: {\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tdisplay: false,\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tposition: \'left\',\n"
WEBURLJSDYNAMIC_data += "\t\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\t\t}\n"
WEBURLJSDYNAMIC_data += "};\n"
WEBURLJSDYNAMIC_data += "\n"

#print details of template data [DHCP data] chart to dynamic-js
WEBURLJSDYNAMIC_data += "var config4 = {\n"
WEBURLJSDYNAMIC_data += "\ttype: 'doughnut',\n"
WEBURLJSDYNAMIC_data += "\tdata: {\n"
WEBURLJSDYNAMIC_data += "\t\tdatasets: [{\n"
WEBURLJSDYNAMIC_data += "\t\t\tdata: [\n"
for vwstype in range(len(list_Template_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\t" + str(list_Template.count(list_Template_unique[vwstype])) + ",\n"
WEBURLJSDYNAMIC_data += "\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tbackgroundColor: [\n"
array_counter = 1
for vwstype in range(len(list_Template_unique)):
  #print array_counter 
  #print "--" + str(vwstype)
  WEBURLJSDYNAMIC_data += "\t\t\t\t\'" + array_color[array_counter] + "\',\n" 
  array_counter += 1
WEBURLJSDYNAMIC_data += "\t\t\t\t],\n"
WEBURLJSDYNAMIC_data += "\t\t\tlabel: \'Dataset 1\'\n"
WEBURLJSDYNAMIC_data += "\t\t}],\n"
WEBURLJSDYNAMIC_data += "\t\tlabels: [\n"
array_counter=1
for vwstype in range(len(list_Template_unique)):
  WEBURLJSDYNAMIC_data += "\t\t\t\"" + list_Template_unique[vwstype] + "\[" + str(list_Template.count(list_Template_unique[vwstype])) + "\]\",\n"
WEBURLJSDYNAMIC_data += "\t\t\t]\n"
WEBURLJSDYNAMIC_data += "\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\toptions: {\n"
WEBURLJSDYNAMIC_data += "\t\t\tresponsive: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\tlegend: {\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tdisplay: true,\n"
WEBURLJSDYNAMIC_data += "\t\t\t\tposition: \'left\',\n"
WEBURLJSDYNAMIC_data += "\t\t\t},\n"
WEBURLJSDYNAMIC_data += "\t\t\t}\n"
WEBURLJSDYNAMIC_data += "};\n"
WEBURLJSDYNAMIC_data += "\n"


# summary top
WEBURLFILE_data = WEBURLFILE_data + "<div id=\"table-summary\" style=\"width: 95%; padding: 0px 15px 0px 15px; border: 1px solid #ddd; background-color: #fff; margin: 15px\">"
WEBURLFILE_data = WEBURLFILE_data + "<br><table style=\"width: 100%; padding: 0px;border: 0px solid #dddddd;border-collapse: separate; border-spacing: 0px;\">"
WEBURLFILE_data = WEBURLFILE_data + "<tr>"
WEBURLFILE_data = WEBURLFILE_data + "<td class=\"toptable\" style=\"border-right: 0px solid #dddddd;\" ><h1>" + str(PARAM_ACCESSCOUNT_TOTAL) + "</h1><h2>Active Enclosures</h2></td>"
WEBURLFILE_data = WEBURLFILE_data + "<td class=\"toptable\" style=\"border-right: 0px solid #dddddd;\" ><h1>" + str(PARAM_TOTALBLADES_TOTAL) +"</h1><h2>Total Blades</h2></td>"
WEBURLFILE_data = WEBURLFILE_data + "<td class=\"toptable\" ><h2>Report Date</h2><h3>" + date_now + "</h3></font></td>"
WEBURLFILE_data = WEBURLFILE_data + "</tr>"
WEBURLFILE_data = WEBURLFILE_data + "</table>"
WEBURLFILE_data = WEBURLFILE_data + "</div>"

# collect WEBURLFILE_data summary
WEBURLFILE_data_summary = WEBURLFILE_data
WEBURLFILE_data = ""

WEBURLFILE_data = WEBURLFILE_data_header + WEBURLFILE_data_summary +  WEBURLFILE_data_content 

# add end of report
WEBURLFILE_data = WEBURLFILE_data + "<div style=\"background-color: #fff; width: auto; padding: 5px; margin-top: 0px; border-top: 1px solid #ddd; padding-left: 20px\">\n"
WEBURLFILE_data = WEBURLFILE_data + "<br>(End of Report)\n"
WEBURLFILE_data = WEBURLFILE_data + "</div>\n"
WEBURLFILE_data = WEBURLFILE_data + "</body></html>"
   
#print site_dict['bngsti-a-rgs1.asia-pac.shell.com'] 
#print WEBURLFILE_data
#print WEBURLJSDYNAMIC_data
#print RANDOM_bladedata
# write content to html and js file
with open(WEBURLFILE, 'wb') as webfile:
  webfile.write(WEBURLFILE_data)
with open(WEBURLJSDYNAMIC, 'wb') as webfile:
  webfile.write(WEBURLJSDYNAMIC_data)

#rm -rf RANDOM_oa_output
#rm -rf RANDOM_oa_output_all
#rm -rf RANDOM_cnlist
#rm -rf RANDOM_indcndata
#os.remove(RANDOM_bladedata_file)
os.remove(RANDOM_indcndata)
#rm -rf RANDOM_bladedata1