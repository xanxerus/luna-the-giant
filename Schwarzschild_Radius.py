#!/usr/bin/pypy
from math import sqrt

#References
#https://en.wikipedia.org/wiki/Schwarzschild_radius
#http://hyperphysics.phy-astr.gsu.edu/hbase/vision/eyescal.html

'''Schwarzchild Radius'''

LUNAR_SCALE_FACTOR = 1.448417e+08

#https://oddlespuddle.com/sugar-content/
density = 1035.05886522
mass = 1.570981e+26

#https://oddlespuddle.com/volume/
female_volume = 4.994885e-02

#http://www.averageheight.co/average-female-height-by-country
female_height = 1.622

#http://hypertextbook.com/facts/2002/AniciaNdabahaliye1.shtml
eye_diameter = 2.4e-2

#https://en.wikipedia.org/wiki/Gravitational_constant
G = 6.674e-11

#https://en.wikipedia.org/wiki/Speed_of_light
c = 299792458

print "Luna's Schwarzchild height (meters): %f" % (4*G*mass / pow(c, 2))
print

collapse_height = sqrt( (pow(c, 2) * pow(female_height, 3)) / (2*G*density*female_volume) )

print "Height of collapse (meters): %e" % collapse_height
print

schwarzchild_scale_factor = collapse_height / female_height

print "Schwarzchild Scale Factor: %e" % schwarzchild_scale_factor
print

schwarzchlid_eye_diameter = schwarzchild_scale_factor * eye_diameter

print "Schwarzchild Eye Diameter: %e" % schwarzchlid_eye_diameter
print

print "Eye light lag (seconds):", schwarzchlid_eye_diameter / (c/1.37) / 60 
print 
