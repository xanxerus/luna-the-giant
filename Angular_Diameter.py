#!/usr/bin/pypy

'''Angular Diameter'''

from math import sqrt, cos, atan


#givens
M_PER_KM = 1000.
moon_diameter = 2 * 1738.1 * 1000
female_height = 1.622
LUNAR_SCALE_FACTOR = 1.448417e+08

#givens
central_angle = 0.209708531621
eye_depression = .105
lunar_distance = 356500*M_PER_KM
earth_radius = 6371*M_PER_KM
min_lunar_distance = 356500*M_PER_KM - earth_radius
max_lunar_distance = 406700*M_PER_KM - earth_radius

eye_height = LUNAR_SCALE_FACTOR*(female_height-eye_depression)
print 'Eye height: %e' % eye_height

print 'Minimum distance from Earth surface to moon center %e' % min_lunar_distance

eye_distance = sqrt(earth_radius**2 + (earth_radius+eye_height)**2 - 2*earth_radius*(earth_radius+eye_height)*cos(central_angle))
print 'Eye distance: %e' % eye_distance

eye_angular_diameter = 2*atan(moon_diameter/(2*eye_distance))
print 'Eye angular diameter:', eye_angular_diameter


print 'Max distance from surface to moon center %e' % max_lunar_distance
max_angular_diameter = 2*atan(moon_diameter/(2*max_lunar_distance))
print 'Max angular diameter:', max_angular_diameter

print 'Min distance from surface to moon center %e' % min_lunar_distance
min_angular_diameter = 2*atan(moon_diameter/(2*min_lunar_distance))
print 'Min angular diameter:', min_angular_diameter


print 'Max proportion:', eye_angular_diameter/min_angular_diameter
print 'Min proportion:', eye_angular_diameter/max_angular_diameter
