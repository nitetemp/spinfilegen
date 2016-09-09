from datetime import date
import datetime
import os
sn = 0
days = datetime.datetime.today().day
months = datetime.datetime.today().month
years = datetime.datetime.today() .year
f = open('%s%sspin.html'%(days,months), 'w')
f.write('<!DOCTYPE html>')
f.write('\n<html>')
f.write('\n<head>')
f.write('\n<link rel="stylesheet" type="text/css" href="ff.css">')
f.write('\n<body>')
f.write('\n<h5>Dear Priya,</h5>')
f.write('\n<h3>Spinneys Quality Check for Products Send on %s/%s/%s</h3>'%(days,months,years))
f.write('\n<p>It was observed that the products for Spinneys were on average of good quality with minor issues that were resolved completely. </p>')
f.write('\n<h5>Summary of Products</h5>')
f.write('\n<table>')
f.write('\n<tr>')
f.write('\n<th>S.No</th>')
f.write('\n<th>Name of Product</th>')
f.write('\n<th>Picture of Product</th>')
f.write('\n<th>Quality of Product</th>')
f.write('\n</tr>')
for root, subdirs, files in os.walk('C:\Users\LEON\Desktop\spin%s%s'%(days,months)):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
             flet = os.path.join(root, file)
             sn = sn+1
             f.write('\n<tr>')
             f.write('\n<td>%s</td>'%sn)
             f.write('\n<td>''</td>')
             f.write('\n<td><img src="file:///%s" alt="" style="width:200px; height:auto;"></td>'%flet)
             f.write('\n<td>Good</td>')
             f.write('\n</tr>')
f.write('\n</table>')
by = date(2015, 11, 28)
since = date(years,months,days)
res = since - by
datecode = res.days
datecode = datecode - 1
f.write('\n<footer>')
f.write('\n<p>%s</p>'%datecode)
f.write('\n</footer>')
f.write('\n</body>')
f.write('\n</head>')
f.write('\n</html>')
f.closed
