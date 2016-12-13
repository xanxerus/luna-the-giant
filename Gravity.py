#!/usr/bin/env pypy

'''Gravity'''

from math import radians, cos, acos, sin, sqrt

#givens

LUNAR_SCALE_FACTOR = 1.448417e+08
female_height = 1.622
mass = 1.570981e+26
female_mass = 51.7

furman_lat, furman_lon = radians(34.922753), radians(-82.441248)
utd_lat, utd_lon = radians(32.989924), radians(-96.751620)
earth_radius = 6.378137e6
female_com_ratio = 0.543
male_mass = 74.
G = 6.674e-11
g = 9.8

#basic calculations
central_angle = acos(sin(furman_lat)*sin(utd_lat) +cos(furman_lat)*cos(utd_lat)*cos(abs(furman_lon-utd_lon)))
print 'Central Angle:', central_angle

chord = 2*earth_radius*sin(central_angle/2)
com_height = LUNAR_SCALE_FACTOR*female_com_ratio*female_height
print 'Center of mass height: %e' % com_height

com_distance = sqrt(earth_radius**2 + (earth_radius+com_height)**2 - 2*earth_radius*(earth_radius+com_height)*cos(central_angle))
print 'Center of mass distnace %e' % com_distance

force_gravity = (G*mass*male_mass) / (com_distance**2)
print 'Force of gravity:', force_gravity

earth_gravity = g*male_mass
print 'Earth gravity on Endymion:', earth_gravity

air_pressure = 1.54*1.013e5
print 'Air pressure:', air_pressure

proportion_air_gravity = air_pressure/force_gravity
print 'Proportion of air pressure to gravity:', proportion_air_gravity
