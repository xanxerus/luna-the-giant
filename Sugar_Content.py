#!/usr/bin/env pypy

'''Gummy Bears'''

#givens

KG_PER_LB = 0.453592

female_mass = 51.7
female_volume = 4.994885e-02
volume = 1.517770e+23

grams_sugar_per_serving = 18.
servings_per_giant_bear = 51.
giant_bear_mass = 4.8*KG_PER_LB
grams_annual_world_sugar_production = 1.72e14
years_age_of_universe = 13.82e9

#basic calculations
density = female_mass/female_volume
print 'Density (kg per m^3):', density
mass = density*volume
print 'Mass (kg): %e' % mass
sugar_content = grams_sugar_per_serving*servings_per_giant_bear/giant_bear_mass*mass
print 'Sugar content (grams): %e' % sugar_content
years_of_sugar = sugar_content/grams_annual_world_sugar_production
print 'Years of sugar: %e' % years_of_sugar
universes_of_sugar = years_of_sugar/years_age_of_universe
print 'Universes of sugar:', universes_of_sugar

