import ephem

moons = ((ephem.Io(), 'i'),
         (ephem.Europa(), 'e'),
         (ephem.Ganymede(), 'g'),
         (ephem.Callisto(), 'c'))

time_int = 0.5
days_shown = 1
  
# How to place discrete characters on a line that actually represents
# the real numbers -maxradii to +maxradii.

linelen = 65
maxradii = 30.

def put(line, character, radii):
    if abs(radii) > maxradii:
        return
    offset = radii / maxradii * (linelen - 1) / 2
    i = int(linelen / 2 + offset)
    line[i] = character

interval = ephem.hour * time_int
now = ephem.now()
now -= now % interval

t = now
while t < now + days_shown:
    line = [' '] * linelen
    put(line, 'J', 0)
    for moon, character in moons:
        moon.compute(t)
        put(line, character, moon.x)
    print str(ephem.date(t))[5:], ''.join(line).rstrip()
    t += interval

print 'East is to the right;',
print ', '.join([ '%s = %s' % (c, m.name) for m, c in moons ])
