#!/usr/bin/pypy

'''Gravity 2'''

from decimal import Decimal
from math import e, sin

#https://oddlespuddle.com/sugar-content/
luna_mass = 1.570981e+26

#https://oddlespuddle.com/gravity/
central_angle = 0.209708531621
com_height = 1.275687e+08

#http://www.averageheight.co/average-male-height-by-country
male_mass = 74.

#http://www.averageheight.co/average-female-height-by-country
female_mass = 51.7

#http://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
earth_radius = 6.378137e6

#https://en.wikipedia.org/wiki/Gravitational_constant
G = 6.674e-11

woman_distance = 2 * earth_radius * sin(central_angle/2)
print 'The distance between UTD and Furman University (meters): %e' % woman_distance
f_woman = G*male_mass*female_mass / woman_distance**2
print 'Average force of gravity between a UTD boy and a Furman girl: %e' % f_woman

print

#http://www.prb.org/Publications/Articles/2002/HowManyPeopleHaveEverLivedonEarth.aspx
sofar = 107602707791 

#http://www.prb.org/pdf04/04WorldDataSheet_ENG.pdf
P1, B1 = 6396e6, 21/1000.

#http://www.prb.org/pdf16/prb-wpds2016-web-2016.pdf
P2, B2 = 7418151841., 20/1000.
D2 = 8/1000.

#http://home2.fvcc.edu/~dhicketh/DiffEqns/spring13projects/Population%20Model%20Project%202013/PopulationModels2013.pdf
K, r = 12.089e9, 0.028

c = (B1-B2) / (P2-P1)
b = B1 + c*P1
d = b-r
a = (d-D2)/P2
A = Decimal(P2 / (K*e**(r*2016) - P2*e**(r*2016)))

def Bt(t):
	return ( (Decimal(1) + A*Decimal(r*t).exp()).ln() * Decimal(b*K - c*K*K) - Decimal(c*K*K) / Decimal(Decimal(1) + A*Decimal(r*t).exp()) ) / Decimal(r)

def B(q, w):
	return Bt(w) - Bt(q)

def D(q, w):
	return B(q, w) - (P(w) - P(q))

def P(t):
	return (K*A*e**(r*t)) / (1 + A*e**(r*t))

total_pop = sofar + B(2011, 5e5)
print 'Number of people who wil ever live: %e' % total_pop
print '(Assuming humanity dies off by 500,000 AD)'
print

#https://www.census.gov/population/international/data/idb/region.php?N=%20Results%20&T=10&A=aggregate&RT=0&Y=2016&R=1&C=
female_ratio = Decimal(sum((287047314, 295555732, 271093454, 246580992, 239042844, 228387092, 
				  207351391, 170558952, 152109594, 118877093, 85170799, 67005265, 
				  44065869, 24568704, 9736777, 2374033, 407552))) / Decimal(7323187457)
print 'Ratio of women who are 20+ to population: %f' % female_ratio 
print 'Number of 20+ years old women who will ever live: %e' % (total_pop*female_ratio)
print

male_ratio = Decimal(sum((305426815, 307759783, 280252886, 253573506, 243854302, 
						  231861422, 205697679, 164436459, 142826480, 107987301, 
						  73614120, 52365037, 30505239, 13995704, 4211461, 
						  768012, 94044))) / Decimal(7323187457)
print 'Ratio of men who are 20+ to population: %f' % male_ratio 
print 'Number of 20+ years old men who will ever live: %e' % (total_pop*male_ratio)
print 


f_max = G*male_mass*luna_mass / (com_height**2)
f_min = G*male_mass*luna_mass / ((com_height+2*earth_radius)**2)
f_women = G*male_mass*female_mass*float(total_pop*female_ratio) / earth_radius**2
f_world = G*male_mass*(female_mass*float(total_pop*female_ratio) + male_mass*float(total_pop*male_ratio)) / earth_radius**2

print
print '%-20s | %17s | %12s | %12s' % ('Object', 'Gravity Force (N)', 'Ratio to min', 'Ratio to max')
print '-'*71
print '%-20s | %17.3f | %12.3f | %12.3f' % ('Luna\'s Maximum Force', f_max, f_max/f_min, f_max/f_max)
print '%-20s | %17.3f | %12.3f | %12.3f' % ('Luna\'s Minimum Force', f_min, f_min/f_min, f_min/f_max)
print '%-20s | %17.3e | %12.3e | %12.3e' % ('One Furman girl', f_woman, f_woman/f_min, f_woman/f_max)
print '%-20s | %17.3e | %12.3e | %12.3e' % ('All women ever', f_women, f_women/f_min, f_women/f_max)
print '%-20s | %17.3e | %12.3e | %12.3e' % ('All people ever', f_world, f_world/f_min, f_world/f_max)

print f_max/f_world
