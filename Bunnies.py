#!/usr/bin/env pypy

from math import pi as PI

#https://www.aqua-calc.com/page/density-table/substance/carrots-coma-and-blank-raw-coma-and-blank-crown-coma-and-blank-tops-blank-and-blank-scrapings-blank--op-cup-blank-grated-cp-
carrot_density = 464.9428124 #kg per m^3

#http://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
earth_radius = 6.378137e6 #m
earth_mass = 5.9723e24 #kg

sphere_area = lambda r: 4*PI*r*r

planet_volume = earth_mass / carrot_density
print "A spherical carrot with Earth's mass has a volume of %e m^3" % planet_volume

planet_radius = pow(3*planet_volume / (4*PI), 1/3.)
print "It has a radius %f times that of Earth" % (planet_radius/earth_radius)


#https://www.rspca.org.uk/adviceandwelfare/pets/rabbits/diet/myths
print
print "Turns out rabbits don't actually eat carrots."
print


#what rabbits eat:
#http://www.peteducation.com/article.cfm?c=18+1803&aid=1638
#https://www.saveafluff.co.uk/rabbit-info/importance-of-hay

#water on earth
#https://water.usgs.gov/edu/earthhowmuch.html
