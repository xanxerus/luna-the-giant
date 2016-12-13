#!/usr/bin/env pypy

'''Volume'''

#givens
LUNAR_SCALE_FACTOR = 1.448417e+08
M3_PER_LITER = 0.001
M_PER_CM = .01

female_height = 1.622
female_mass = 51.7
earth_volume = 1.08321e21

#dubois' formula
female_surface_area = 0.007184 * (female_height/M_PER_CM)**0.725 * (female_mass)**0.425
print 'Female surface area (m^2):', female_surface_area

print 'Weight to height ratio:', (female_mass / (female_height/M_PER_CM))

#NMRI's volume formula
female_volume = M3_PER_LITER * 62.90 * female_surface_area * (female_mass/(female_height/M_PER_CM))**0.578
print 'Female volume: %e' % female_volume

#lunar step
volume = LUNAR_SCALE_FACTOR**3 * female_volume
print 'Luna volume: %e' % volume

print 'Proportion to Earth volume:', volume/earth_volume
