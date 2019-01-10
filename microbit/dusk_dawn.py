from datetime import datetime
import ephem

dt = datetime.now()
cnv_dt = dt.strftime("%Y/%m/%d")
print("Date: {}".format(cnv_dt))

shalford = ephem.Observer()
shalford.pressure = 0
#shalford.horizon = '0:00'
shalford.horizon = '-0:34'
shalford.lat, shalford.lon = '51.215078', '-0.559162'  # use strings for degrees!
td_str = '{} 12:00'.format(cnv_dt)
shalford.date = td_str

rise_ed = shalford.previous_rising(ephem.Sun())
set_ed = shalford.next_setting(ephem.Sun())

print(rise_ed)
print(set_ed)

rise_dt = rise_ed.datetime()
set_dt = set_ed.datetime()

print(rise_dt.ctime())
print(set_dt.ctime())

mars = ephem.Mars(shalford)
print("Mars: alt-{}, az-{}".format(mars.alt, mars.az))

m = ephem.Moon(td_str)
print("Moon in {}".format(ephem.constellation(m)))
m = ephem.Saturn(td_str)
print("Saturn in {}".format(ephem.constellation(m)))
m = ephem.Jupiter(td_str)
print("Jupiter in {}".format(ephem.constellation(m)))
m = ephem.Saturn(td_str)
print("Saturn in {}".format(ephem.constellation(m)))
m = ephem.Mars(td_str)
print("Mars in {}".format(ephem.constellation(m)))