#!/usr/bin/python 
from poly import polygon
from poly import face 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from drawlight import drawlight

sources = []
allpolys = []

OffSet1 = 0.0017

tgtoffset = 0.5
tgtlen = 1.25
#tgtrad = 0.04
#tgtrad = 0.002
tgtrad = 1.4142*0.0025

target = polygon( ([-tgtlen/2,-tgtrad], [tgtlen/2, -tgtrad], [tgtlen/2,tgtrad], [-tgtlen/2,tgtrad]) )

################################################################

###### Lead shield in the target region (for collimating photons)

#seg 1
x1_shield_top=0.400
x1_shield_bottom=-1.150
z1_shield=1.200

x2_shield_top=1.400 #*1.414 The shield is a rectangle (in CAD), but the narrow dimension is the one relevant for here
x2_shield_bottom=-0.400
z2_shield=1.200

x3_shield_top=1.400
x3_shield_bottom=-0.400
z3_shield=1.600

x4_shield_top=0.400
x4_shield_bottom=-1.150
z4_shield=1.600


shield_top  = polygon( ([z1_shield,  x1_shield_top], [z4_shield,  x4_shield_top], [z3_shield,  x3_shield_top], [z2_shield,  x2_shield_top] ), notSource=False)
shield_bottom = polygon( ([z1_shield, x1_shield_bottom], [z4_shield, x4_shield_bottom], [z3_shield, x3_shield_bottom], [z2_shield, x2_shield_bottom] ), notSource=False)

###### Lead collar (for collimating photons)

#seg 1
x1_collar=0.074#+0.05
z1_collar=2.851#+1.5

x2_collar=0.185 #*1.414 The collar is a rectangle (in CAD), but the narrow dimension is the one relevant for here
z2_collar=2.851#+1.5

x3_collar=0.185 #*1.414
z3_collar=3.051#+1.5

x4_collar=0.074#+0.05
z4_collar=3.051#+1.5


collar_top    = polygon( ([z1_collar,  x1_collar], [z4_collar,  x4_collar], [z3_collar,  x3_collar], [z2_collar,  x2_collar] ), notSource=False)
collar_bottom = polygon( ([z2_collar, -x2_collar], [z3_collar, -x3_collar], [z4_collar, -x4_collar], [z1_collar, -x1_collar] ), notSource=False)

###### Hybrid upstream Lead collar (for ep scattering)

x1_collar3=0.335
z1_collar3=4.4305+4.5

x2_collar3=2.000
z2_collar3=4.4305+4.5

x3_collar3=2.000
z3_collar3=4.6805+4.5

x4_collar3=0.335
z4_collar3=4.6805+4.5


collar3_top    = polygon( ([z1_collar3,  x1_collar3], [z4_collar3,  x4_collar3], [z3_collar3,  x3_collar3], [z2_collar3,  x2_collar3] ), notSource=False)
collar3_bottom = polygon( ([z2_collar3, -x2_collar3], [z3_collar3, -x3_collar3], [z4_collar3, -x4_collar3], [z1_collar3, -x1_collar3] ), notSource=False)

#################################################################

###### First downstream Lead collar (for ep scattering)

x1_collar1=0.600
z1_collar1=12.300+4.5

x2_collar1=0.750 
z2_collar1=12.300+4.5

x3_collar1=0.750
z3_collar1=12.400+4.5

x4_collar1=0.600
z4_collar1=12.400+4.5


collar_top1    = polygon( ([z1_collar1,  x1_collar1], [z4_collar1,  x4_collar1], [z3_collar1,  x3_collar1], [z2_collar1,  x2_collar1] ), notSource=False)
collar_bottom1 = polygon( ([z2_collar1, -x2_collar1], [z3_collar1, -x3_collar1], [z4_collar1, -x4_collar1], [z1_collar1, -x1_collar1] ), notSource=False)

###### Second downstream Lead collar (for ep scattering)

x1_collar2=0.952
z1_collar2=18.900+4.5

x2_collar2=1.200
z2_collar2=18.900+4.5

x3_collar2=1.200
z3_collar2=19.000+4.5

x4_collar2=0.952
z4_collar2=19.000+4.5


collar_top2    = polygon( ([z1_collar2,  x1_collar2], [z4_collar2,  x4_collar2], [z3_collar2,  x3_collar2], [z2_collar2,  x2_collar2] ), notSource=False)
collar_bottom2 = polygon( ([z2_collar2, -x2_collar2], [z3_collar2, -x3_collar2], [z4_collar2, -x4_collar2], [z1_collar2, -x1_collar2] ), notSource=False)

#################################################################

######inner photon collimator (Col 1)
# Previous implementation assumed it was a solid shape from front face to back face, 
# but this neglects the fact that it tapers inwards a lot in the first 30cm and then 
# untapers in the last 10cm - updating by splitting into 5 segments

col1_inner_offset = 0.0019

x1_inner_photon_1=0.024-col1_inner_offset
z1_inner_photon_1=5.175-tgtoffset

x2_inner_photon_1=0.031703 # 0.05670 is the outer radius of the Col1 cooling fans, 0.031703 is the outer radius of Col1 otherwise
z2_inner_photon_1=5.175-tgtoffset

x3_inner_photon_1=0.031703
z3_inner_photon_1=5.275-tgtoffset

x4_inner_photon_1=0.024-col1_inner_offset
z4_inner_photon_1=5.275-tgtoffset

x1_inner_photon_2=0.020386-col1_inner_offset
z1_inner_photon_2=5.275-tgtoffset

x2_inner_photon_2=0.028703
z2_inner_photon_2=5.275-tgtoffset

x3_inner_photon_2=0.028703
z3_inner_photon_2=5.375-tgtoffset

x4_inner_photon_2=0.020386-col1_inner_offset
z4_inner_photon_2=5.375-tgtoffset

x1_inner_photon_3=0.018696-col1_inner_offset
z1_inner_photon_3=5.375-tgtoffset

x2_inner_photon_3=0.026703
z2_inner_photon_3=5.375-tgtoffset

x3_inner_photon_3=0.026703
z3_inner_photon_3=5.475-tgtoffset

x4_inner_photon_3=0.018696-col1_inner_offset
z4_inner_photon_3=5.475-tgtoffset

x1_inner_photon_4=0.015529-col1_inner_offset
z1_inner_photon_4=5.475-tgtoffset

x2_inner_photon_4=0.026703
z2_inner_photon_4=5.475-tgtoffset

x3_inner_photon_4=0.026703
z3_inner_photon_4=5.575-tgtoffset

x4_inner_photon_4=0.015529-col1_inner_offset
z4_inner_photon_4=5.575-tgtoffset

x1_inner_photon_5=0.015529-col1_inner_offset
z1_inner_photon_5=5.575-tgtoffset

x2_inner_photon_5=0.026703
z2_inner_photon_5=5.575-tgtoffset

x3_inner_photon_5=0.026703
z3_inner_photon_5=5.675-tgtoffset

x4_inner_photon_5=0.015808-col1_inner_offset
z4_inner_photon_5=5.675-tgtoffset

# one has to assign the coordinates in anti-clock sequence
coll_inner_photon_top_1    = polygon( ([z1_inner_photon_1,  x1_inner_photon_1], [z4_inner_photon_1,  x4_inner_photon_1], [z3_inner_photon_1,  x3_inner_photon_1], [z2_inner_photon_1,  x2_inner_photon_1] ), notSource=False)
coll_inner_photon_bottom_1 = polygon( ([z2_inner_photon_1, -x2_inner_photon_1], [z3_inner_photon_1, -x3_inner_photon_1], [z4_inner_photon_1, -x4_inner_photon_1], [z1_inner_photon_1, -x1_inner_photon_1] ), notSource=False)

coll_inner_photon_top_2    = polygon( ([z1_inner_photon_2,  x1_inner_photon_2], [z4_inner_photon_2,  x4_inner_photon_2], [z3_inner_photon_2,  x3_inner_photon_2], [z2_inner_photon_2,  x2_inner_photon_2] ), notSource=False)
coll_inner_photon_bottom_2 = polygon( ([z2_inner_photon_2, -x2_inner_photon_2], [z3_inner_photon_2, -x3_inner_photon_2], [z4_inner_photon_2, -x4_inner_photon_2], [z1_inner_photon_2, -x1_inner_photon_2] ), notSource=False)

coll_inner_photon_top_3    = polygon( ([z1_inner_photon_3,  x1_inner_photon_3], [z4_inner_photon_3,  x4_inner_photon_3], [z3_inner_photon_3,  x3_inner_photon_3], [z2_inner_photon_3,  x2_inner_photon_3] ), notSource=False)
coll_inner_photon_bottom_3 = polygon( ([z2_inner_photon_3, -x2_inner_photon_3], [z3_inner_photon_3, -x3_inner_photon_3], [z4_inner_photon_3, -x4_inner_photon_3], [z1_inner_photon_3, -x1_inner_photon_3] ), notSource=False)

coll_inner_photon_top_4    = polygon( ([z1_inner_photon_4,  x1_inner_photon_4], [z4_inner_photon_4,  x4_inner_photon_4], [z3_inner_photon_4,  x3_inner_photon_4], [z2_inner_photon_4,  x2_inner_photon_4] ), notSource=False)
coll_inner_photon_bottom_4 = polygon( ([z2_inner_photon_4, -x2_inner_photon_4], [z3_inner_photon_4, -x3_inner_photon_4], [z4_inner_photon_4, -x4_inner_photon_4], [z1_inner_photon_4, -x1_inner_photon_4] ), notSource=False)

coll_inner_photon_top_5    = polygon( ([z1_inner_photon_5,  x1_inner_photon_5], [z4_inner_photon_5,  x4_inner_photon_5], [z3_inner_photon_5,  x3_inner_photon_5], [z2_inner_photon_5,  x2_inner_photon_5] ), notSource=False)
coll_inner_photon_bottom_5 = polygon( ([z2_inner_photon_5, -x2_inner_photon_5], [z3_inner_photon_5, -x3_inner_photon_5], [z4_inner_photon_5, -x4_inner_photon_5], [z1_inner_photon_5, -x1_inner_photon_5] ), notSource=False)


#########collimator 2,  three segments
increasecolth = 0.05
coll2move = 0.075 # col2 is decided to move 75 mm upstream
#seg 1
x1_coll_2_1=-0.035
z1_coll_2_1=5.825-tgtoffset-coll2move

x2_coll_2_1=-0.021336
#x2_coll_2_1=-0.02955
z2_coll_2_1=5.825-tgtoffset-coll2move

x3_coll_2_1=-0.021336
#x3_coll_2_1=-0.02955
z3_coll_2_1=5.975-tgtoffset-coll2move

x4_coll_2_1=-0.035
z4_coll_2_1=5.975-tgtoffset-coll2move


coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), notSource=False)
#coll_2_1   = polygon( ([z1_coll_2_1, x1_coll_2_1], [z4_coll_2_1, x4_coll_2_1], [z3_coll_2_1, x3_coll_2_1], [z2_coll_2_1, x2_coll_2_1] ), isDetector=True)


#seg 2

x1_coll_2_2=-0.300
#x1_coll_2_2=-0.300
z1_coll_2_2=5.825-tgtoffset-coll2move

x2_coll_2_2=-0.101
#x2_coll_2_2=-0.108
z2_coll_2_2=5.825-tgtoffset-coll2move

x3_coll_2_2=-0.101
#x3_coll_2_2=-0.108
z3_coll_2_2=5.975-tgtoffset-coll2move

x4_coll_2_2=-0.300
#x4_coll_2_2=-0.300
z4_coll_2_2=5.975-tgtoffset-coll2move


coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), notSource=False)
#coll_2_2   = polygon( ([z1_coll_2_2, x1_coll_2_2], [z4_coll_2_2, x4_coll_2_2], [z3_coll_2_2, x3_coll_2_2], [z2_coll_2_2, x2_coll_2_2] ), isDetector=True)

#seg 3

x1_coll_2_3=0.021336
#x1_coll_2_3=0.02955
z1_coll_2_3=5.825-tgtoffset-coll2move

x2_coll_2_3= 0.300
#x2_coll_2_3= 0.300
z2_coll_2_3=5.825-tgtoffset-coll2move

x3_coll_2_3= 0.300
#x3_coll_2_3= 0.300
z3_coll_2_3=5.975-tgtoffset-coll2move

x4_coll_2_3=0.021336
#x4_coll_2_3=0.02955
z4_coll_2_3=5.975-tgtoffset-coll2move


coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), notSource=False)
#coll_2_3   = polygon( ([z1_coll_2_3, x1_coll_2_3], [z4_coll_2_3, x4_coll_2_3], [z3_coll_2_3, x3_coll_2_3], [z2_coll_2_3, x2_coll_2_3] ), isDetector=True)


############# Col2 photon collimating inner_pipe
##pipe
x1_pipe0=0.0255
z1_pipe0=5.4

x2_pipe0=0.0285
z2_pipe0=5.4

x3_pipe0=0.0315
z3_pipe0=7.345

x4_pipe0=0.0285
z4_pipe0=7.345


coll_pipe01   = polygon( ([z1_pipe0, x1_pipe0], [z4_pipe0, x4_pipe0], [z3_pipe0, x3_pipe0], [z2_pipe0, x2_pipe0] ), notSource=False)
coll_pipe02   = polygon( ([z2_pipe0, -x2_pipe0], [z3_pipe0, -x3_pipe0], [z4_pipe0, -x4_pipe0], [z1_pipe0, -x1_pipe0] ), notSource=False)

##pipe
x1_pipe1_1=0.0355
z1_pipe1_1=7.875

x2_pipe1_1=0.0385
z2_pipe1_1=7.875

x3_pipe1_1=0.0385
z3_pipe1_1=9.875

x4_pipe1_1=0.0355
z4_pipe1_1=9.875


coll_pipe11_1   = polygon( ([z1_pipe1_1, x1_pipe1_1], [z4_pipe1_1, x4_pipe1_1], [z3_pipe1_1, x3_pipe1_1], [z2_pipe1_1, x2_pipe1_1] ), notSource=False)
coll_pipe12_1   = polygon( ([z2_pipe1_1, -x2_pipe1_1], [z3_pipe1_1, -x3_pipe1_1], [z4_pipe1_1, -x4_pipe1_1], [z1_pipe1_1, -x1_pipe1_1] ), notSource=False)
##pipe
x1_pipe1=0.033*1.03
#x1_pipe1=0.035
z1_pipe1=9.50

x2_pipe1=0.036*1.03
#x2_pipe1=0.038
z2_pipe1=9.5

x3_pipe1=0.0396*1.03
#x3_pipe1=0.0419
#z3_pipe1=11.3
z3_pipe1=9.875

x4_pipe1=0.0366*1.03
#x4_pipe1=0.0389
#z4_pipe1=11.3
z4_pipe1=9.875


coll_pipe11   = polygon( ([z1_pipe1, x1_pipe1], [z4_pipe1, x4_pipe1], [z3_pipe1, x3_pipe1], [z2_pipe1, x2_pipe1] ), notSource=False)
coll_pipe12   = polygon( ([z2_pipe1, -x2_pipe1], [z3_pipe1, -x3_pipe1], [z4_pipe1, -x4_pipe1], [z1_pipe1, -x1_pipe1] ), notSource=False)

##step
x1_pipe2=0.0366*1.03
#x1_pipe2=0.0389
z1_pipe2=11.3

x2_pipe2=0.0396*1.03
#x2_pipe2=0.0419
z2_pipe2=11.3

x3_pipe2=0.0396*1.03
#x3_pipe2=0.0419
z3_pipe2=11.35
#z3_pipe2=12.37

x4_pipe2=0.0366*1.03
#x4_pipe2=0.0389
z4_pipe2=11.35
#z4_pipe2=12.37

coll_pipe21   = polygon( ([z1_pipe2, x1_pipe2], [z4_pipe2, x4_pipe2], [z3_pipe2, x3_pipe2], [z2_pipe2, x2_pipe2] ), notSource=False)
coll_pipe22   = polygon( ([z2_pipe2, -x2_pipe2], [z3_pipe2, -x3_pipe2], [z4_pipe2, -x4_pipe2], [z1_pipe2, -x1_pipe2] ), notSource=False)

#Downstream beampipe outside the vacuum enclosure
##pipe
x1_pipe3=0.522
z1_pipe3=19.0+4.5

x2_pipe3=0.525
z2_pipe3=19.0+4.5

x3_pipe3=0.525
z3_pipe3=19.5+4.5

x4_pipe3=0.522
z4_pipe3=19.5+4.5


coll_pipe31   = polygon( ([z1_pipe3, x1_pipe3], [z4_pipe3, x4_pipe3], [z3_pipe3, x3_pipe3], [z2_pipe3, x2_pipe3] ), notSource=False)
coll_pipe32   = polygon( ([z2_pipe3, -x2_pipe3], [z3_pipe3, -x3_pipe3], [z4_pipe3, -x4_pipe3], [z1_pipe3, -x1_pipe3] ), notSource=False)

##step
x1_pipe4=0.522
z1_pipe4=19.5+4.5

x2_pipe4=0.553
z2_pipe4=19.5+4.5

x3_pipe4=0.553
z3_pipe4=19.503+4.5

x4_pipe4=0.522
z4_pipe4=19.503+4.5

coll_pipe41   = polygon( ([z1_pipe4, x1_pipe4], [z4_pipe4, x4_pipe4], [z3_pipe4, x3_pipe4], [z2_pipe4, x2_pipe4] ), notSource=False)
coll_pipe42   = polygon( ([z2_pipe4, -x2_pipe4], [z3_pipe4, -x3_pipe4], [z4_pipe4, -x4_pipe4], [z1_pipe4, -x1_pipe4] ), notSource=False)

##pipe
x1_pipe5=0.550
z1_pipe5=19.503+4.5

x2_pipe5=0.553
z2_pipe5=19.503+4.5

x3_pipe5=0.553
z3_pipe5=20.5+4.5

x4_pipe5=0.550
z4_pipe5=20.5+4.5


coll_pipe51   = polygon( ([z1_pipe5, x1_pipe5], [z4_pipe5, x4_pipe5], [z3_pipe5, x3_pipe5], [z2_pipe5, x2_pipe5] ), notSource=False)
coll_pipe52   = polygon( ([z2_pipe5, -x2_pipe5], [z3_pipe5, -x3_pipe5], [z4_pipe5, -x4_pipe5], [z1_pipe5, -x1_pipe5] ), notSource=False)

##step
x1_pipe6=0.550
z1_pipe6=20.5+4.5

x2_pipe6=0.587
z2_pipe6=20.5+4.5

x3_pipe6=0.587
z3_pipe6=20.503+4.5

x4_pipe6=0.584
z4_pipe6=20.503+4.5

coll_pipe61   = polygon( ([z1_pipe6, x1_pipe6], [z4_pipe6, x4_pipe6], [z3_pipe6, x3_pipe6], [z2_pipe6, x2_pipe6] ), notSource=False)
coll_pipe62   = polygon( ([z2_pipe6, -x2_pipe6], [z3_pipe6, -x3_pipe6], [z4_pipe6, -x4_pipe6], [z1_pipe6, -x1_pipe6] ), notSource=False)

##pipe
x1_pipe7=0.584
z1_pipe7=20.503+4.5

x2_pipe7=0.587
z2_pipe7=20.503+4.5

x3_pipe7=0.587
z3_pipe7=21.5+4.5

x4_pipe7=0.584
z4_pipe7=21.5+4.5


coll_pipe71   = polygon( ([z1_pipe7, x1_pipe7], [z4_pipe7, x4_pipe7], [z3_pipe7, x3_pipe7], [z2_pipe7, x2_pipe7] ), notSource=False)
coll_pipe72   = polygon( ([z2_pipe7, -x2_pipe7], [z3_pipe7, -x3_pipe7], [z4_pipe7, -x4_pipe7], [z1_pipe7, -x1_pipe7] ), notSource=False)


##step
x1_pipe8=0.584
z1_pipe8=21.5+4.5

x2_pipe8=0.618
z2_pipe8=21.5+4.5

x3_pipe8=0.618
z3_pipe8=21.503+4.5

x4_pipe8=0.584
z4_pipe8=21.503+4.5

coll_pipe81   = polygon( ([z1_pipe8, x1_pipe8], [z4_pipe8, x4_pipe8], [z3_pipe8, x3_pipe8], [z2_pipe8, x2_pipe8] ), notSource=False)
coll_pipe82   = polygon( ([z2_pipe8, -x2_pipe8], [z3_pipe8, -x3_pipe8], [z4_pipe8, -x4_pipe8], [z1_pipe8, -x1_pipe8] ), notSource=False)


##pipe
x1_pipe9=0.615
z1_pipe9=21.503+4.5

x2_pipe9=0.618
z2_pipe9=21.503+4.5

x3_pipe9=0.618
z3_pipe9=23.0+4.5

x4_pipe9=0.615
z4_pipe9=23.0+4.5


coll_pipe91   = polygon( ([z1_pipe9, x1_pipe9], [z4_pipe9, x4_pipe9], [z3_pipe9, x3_pipe9], [z2_pipe9, x2_pipe9] ), notSource=False)
coll_pipe92   = polygon( ([z2_pipe9, -x2_pipe9], [z3_pipe9, -x3_pipe9], [z4_pipe9, -x4_pipe9], [z1_pipe9, -x1_pipe9] ), notSource=False)


##step
x1_pipe10=0.615
z1_pipe10=23.0+4.5

x2_pipe10=0.663
z2_pipe10=23.0+4.5

x3_pipe10=0.663
z3_pipe10=23.003+4.5

x4_pipe10=0.615
z4_pipe10=23.003+4.5

coll_pipe101   = polygon( ([z1_pipe10, x1_pipe10], [z4_pipe10, x4_pipe10], [z3_pipe10, x3_pipe10], [z2_pipe10, x2_pipe10] ), notSource=False)
coll_pipe102   = polygon( ([z2_pipe10, -x2_pipe10], [z3_pipe10, -x3_pipe10], [z4_pipe10, -x4_pipe10], [z1_pipe10, -x1_pipe10] ), notSource=False)

##pipe
x1_pipe11=0.660
z1_pipe11=23.003+4.5

x2_pipe11=0.663
z2_pipe11=23.003+4.5

x3_pipe11=0.663
z3_pipe11=25.0+4.5

x4_pipe11=0.660
z4_pipe11=25.0+4.5

coll_pipe111   = polygon( ([z1_pipe11, x1_pipe11], [z4_pipe11, x4_pipe11], [z3_pipe11, x3_pipe11], [z2_pipe11, x2_pipe11] ), notSource=False)
coll_pipe112   = polygon( ([z2_pipe11, -x2_pipe11], [z3_pipe11, -x3_pipe11], [z4_pipe11, -x4_pipe11], [z1_pipe11, -x1_pipe11] ), notSource=False)


##step
x1_pipe12=0.660
z1_pipe12=25.0+4.5

x2_pipe12=0.713
z2_pipe12=25.0+4.5

x3_pipe12=0.713
z3_pipe12=25.003+4.5

x4_pipe12=0.660
z4_pipe12=25.003+4.5

coll_pipe121   = polygon( ([z1_pipe12, x1_pipe12], [z4_pipe12, x4_pipe12], [z3_pipe12, x3_pipe12], [z2_pipe12, x2_pipe12] ), notSource=False)
coll_pipe122   = polygon( ([z2_pipe12, -x2_pipe12], [z3_pipe12, -x3_pipe12], [z4_pipe12, -x4_pipe12], [z1_pipe12, -x1_pipe12] ), notSource=False)

##pipe
x1_pipe13=0.710
z1_pipe13=25.003+4.5

x2_pipe13=0.713
z2_pipe13=25.003+4.5

x3_pipe13=0.713
z3_pipe13=26.5176+4.5

x4_pipe13=0.710
z4_pipe13=26.5176+4.5

coll_pipe131   = polygon( ([z1_pipe13, x1_pipe13], [z4_pipe13, x4_pipe13], [z3_pipe13, x3_pipe13], [z2_pipe13, x2_pipe13] ), notSource=False)
coll_pipe132   = polygon( ([z2_pipe13, -x2_pipe13], [z3_pipe13, -x3_pipe13], [z4_pipe13, -x4_pipe13], [z1_pipe13, -x1_pipe13] ), notSource=False)


##pipe after Vaccum chamber after hybrid
##Step
x1_pipe14=0.600
z1_pipe14=12.405+4.5

x2_pipe14=1.2627
z2_pipe14=12.405+4.5

x3_pipe14=1.2627
z3_pipe14=12.4431+4.5

x4_pipe14=0.600
z4_pipe14=12.4431+4.5

coll_pipe141   = polygon( ([z1_pipe14, x1_pipe14], [z4_pipe14, x4_pipe14], [z3_pipe14, x3_pipe14], [z2_pipe14, x2_pipe14] ), notSource=False)
coll_pipe142   = polygon( ([z2_pipe14, -x2_pipe14], [z3_pipe14, -x3_pipe14], [z4_pipe14, -x4_pipe14], [z1_pipe14, -x1_pipe14] ), notSource=False)

##pipe
x1_pipe15=1.250
z1_pipe15=12.4431+4.5

x2_pipe15=1.2627
z2_pipe15=12.4431+4.5

x3_pipe15=1.2627
z3_pipe15=18.8569+4.5

x4_pipe15=1.250
z4_pipe15=18.8569+4.5

coll_pipe151   = polygon( ([z1_pipe15, x1_pipe15], [z4_pipe15, x4_pipe15], [z3_pipe15, x3_pipe15], [z2_pipe15, x2_pipe15] ), notSource=False)
coll_pipe152   = polygon( ([z2_pipe15, -x2_pipe15], [z3_pipe15, -x3_pipe15], [z4_pipe15, -x4_pipe15], [z1_pipe15, -x1_pipe15] ), notSource=False)

##Step
x1_pipe16=0.952
z1_pipe16=18.8569+4.5

x2_pipe16=1.2627
z2_pipe16=18.8569+4.5

x3_pipe16=1.2627
z3_pipe16=18.895+4.5

x4_pipe16=0.952
z4_pipe16=18.895+4.5

coll_pipe161   = polygon( ([z1_pipe16, x1_pipe16], [z4_pipe16, x4_pipe16], [z3_pipe16, x3_pipe16], [z2_pipe16, x2_pipe16] ), notSource=False)
coll_pipe162   = polygon( ([z2_pipe16, -x2_pipe16], [z3_pipe16, -x3_pipe16], [z4_pipe16, -x4_pipe16], [z1_pipe16, -x1_pipe16] ), notSource=False)

################# collimator 4, 3 segmentations

downstream_col4_shift=-1.5
dss=downstream_col4_shift ### This shift is largely arbitrary

#seg 1

x1_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
#x1_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
z1_coll_4_1=9.725+dss-tgtoffset

x2_coll_4_1=-0.1965 #-0.1714 #Was -0.23495, then was -0.1655, current sculpt values reflect updated moller envelopes at this upstream z position
#x2_coll_4_1=-0.1714 #-0.1714 #Was -0.23495, then was -0.1655, current sculpt values reflect updated moller envelopes at this upstream z position
z2_coll_4_1=9.725+dss-tgtoffset

x3_coll_4_1=-0.1965 # -0.1714 #Was -0.23495, then was -0.1655
#x3_coll_4_1=-0.1714 # -0.1714 #Was -0.23495, then was -0.1655
z3_coll_4_1=9.875+dss-tgtoffset

x4_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
#x4_coll_4_1=-0.300 #Was simulation -0.300 # Was CAD -0.254
z4_coll_4_1=9.875+dss-tgtoffset


coll_4_1   = polygon( ([z1_coll_4_1, x1_coll_4_1], [z4_coll_4_1, x4_coll_4_1], [z3_coll_4_1, x3_coll_4_1], [z2_coll_4_1, x2_coll_4_1]), notSource=False)


#seg 2

x1_coll_4_2=-0.0535 #0.05 #Was -0.06377, then was -0.0525
#x1_coll_4_2=-0.05 #0.05 #Was -0.06377, then was -0.0525
z1_coll_4_2=9.775+dss-tgtoffset

x2_coll_4_2=-0.030861
z2_coll_4_2=9.775+dss-tgtoffset

x3_coll_4_2=-0.030861
z3_coll_4_2=9.875+dss-tgtoffset

x4_coll_4_2=-0.0535 #0.05 #Was -0.06377, then was -0.0525
#x4_coll_4_2=-0.05 #0.05 #Was -0.06377, then was -0.0525
z4_coll_4_2=9.875+dss-tgtoffset


coll_4_2   = polygon( ([z1_coll_4_2, x1_coll_4_2], [z4_coll_4_2, x4_coll_4_2], [z3_coll_4_2, x3_coll_4_2], [z2_coll_4_2, x2_coll_4_2]), notSource=False)

#seg 3

x1_coll_4_3=0.030861
z1_coll_4_3=9.775+dss-tgtoffset

x2_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
#x2_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
z2_coll_4_3=9.775+dss-tgtoffset

x3_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
#x3_coll_4_3=0.300 #Was simulation -0.300 # Was CAD -0.254
z3_coll_4_3=9.875+dss-tgtoffset

x4_coll_4_3=0.030861
z4_coll_4_3=9.875+dss-tgtoffset


coll_4_3   = polygon( ([z1_coll_4_3, x1_coll_4_3], [z4_coll_4_3, x4_coll_4_3], [z3_coll_4_3, x3_coll_4_3], [z2_coll_4_3, x2_coll_4_3]), notSource=False)


######### collimator 5 (shaped like a tuning fork), 1 seg


x1_coll_5=-0.11638 # use this if you just want the exact y=0 slice
z1_coll_5=12.8-tgtoffset

x2_coll_5=-0.07422 #from GDML
z2_coll_5=12.8-tgtoffset  #thickness of collimator 5 = 35 mm

x3_coll_5=-0.07422 #from GDML
z3_coll_5=12.87-tgtoffset

x4_coll_5=-0.11638 # use this if you just want the exact y=0 slice
z4_coll_5=12.87-tgtoffset

coll_5   = polygon( ([z1_coll_5, x1_coll_5], [z4_coll_5, x4_coll_5], [z3_coll_5, x3_coll_5], [z2_coll_5, x2_coll_5]), notSource=False)

###### Lintel (for ep scattering)

x1_lintel=0.435
z1_lintel=7.785+4.5

x2_lintel=0.650
z2_lintel=7.785+4.5

x3_lintel=0.650
z3_lintel=7.885+4.5

x4_lintel=0.435
z4_lintel=7.885+4.5


#collar_top2    = polygon( ([z1_lintel,  x1_lintel], [z4_lintel,  x4_lintel], [z3_lintel,  x3_lintel], [z2_lintel,  x2_lintel] ), notSource=False)
lintel = polygon( ([z2_lintel, -x2_lintel], [z3_lintel, -x3_lintel], [z4_lintel, -x4_lintel], [z1_lintel, -x1_lintel] ), notSource=False)

#################################################################

#### quartz

#quartz1 = polygon( ([28.0, 0.6], [28.01, 0.6], [28.01, 1.4], [28, 1.4]), isDetector=True )
#quartz2 = polygon( ([28.0, -1.4], [28.01, -1.4], [28.01, -0.6], [28, -0.6]), isDetector=True )

det_inner_radius=0.69 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
det_outer_radius=1.30 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
det_z_pos=26.5
det_z_extent=1.0 # was = .02 for ideal detector

quartz1 = polygon( ([det_z_pos, det_inner_radius], [det_z_pos+det_z_extent, det_inner_radius], [det_z_pos+det_z_extent, det_outer_radius], [det_z_pos, det_outer_radius]), isDetector=True )
quartz2 = polygon( ([det_z_pos, -det_outer_radius], [det_z_pos+det_z_extent, -det_outer_radius], [det_z_pos+det_z_extent, -det_inner_radius], [det_z_pos, -det_inner_radius]), isDetector=True )

#### sub-quartz array detector to give an idea about the available space before photons become an issue again

sub_det_inner_radius=0.6 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
sub_det_outer_radius=0.689 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
sub_det_z_pos=26.5
sub_det_z_extent=1.0 # was = .02 for ideal detector
#sub_det_inner_radius=0.06 # was 0.55, probably fine at 0.6, ring 1 quartz actually begins at 0.69
#sub_det_outer_radius=0.689 # ring 6 quartz ends at 1.2, PMTs begin at 1.3
#sub_det_z_pos=6.0
#sub_det_z_extent=1.0 # was = .02 for ideal detector

sub_quartz1 = polygon( ([sub_det_z_pos, sub_det_inner_radius], [sub_det_z_pos+sub_det_z_extent, sub_det_inner_radius], [sub_det_z_pos+sub_det_z_extent, sub_det_outer_radius], [sub_det_z_pos, sub_det_outer_radius]), isDetector=True )
sub_quartz2 = polygon( ([sub_det_z_pos, -sub_det_outer_radius], [sub_det_z_pos+sub_det_z_extent, -sub_det_outer_radius], [sub_det_z_pos+sub_det_z_extent, -sub_det_inner_radius], [sub_det_z_pos, -sub_det_inner_radius]), isDetector=True )


#quartz1 = polygon( ([28.0, 0.55], [28.02, 0.55], [28.02, 1.3], [28, 1.3]), isDetector=True )
#quartz2 = polygon( ([28.0, -1.3], [28.02, -1.3], [28.02, -0.55], [28, -0.55]), isDetector=True )

##################################################################################################################################

sources.append(target)

allpolys.append(shield_top)
allpolys.append(shield_bottom)

allpolys.append(collar_top)
allpolys.append(collar_bottom)

allpolys.append(collar_top1)
allpolys.append(collar_bottom1)

allpolys.append(collar_top2)
allpolys.append(collar_bottom2)

allpolys.append(collar3_top)
allpolys.append(collar3_bottom)

allpolys.append(coll_inner_photon_top_1)
allpolys.append(coll_inner_photon_bottom_1)
allpolys.append(coll_inner_photon_top_2)
allpolys.append(coll_inner_photon_bottom_2)
allpolys.append(coll_inner_photon_top_3)
allpolys.append(coll_inner_photon_bottom_3)
allpolys.append(coll_inner_photon_top_4)
allpolys.append(coll_inner_photon_bottom_4)
allpolys.append(coll_inner_photon_top_5)
allpolys.append(coll_inner_photon_bottom_5)

allpolys.append(coll_2_1)
allpolys.append(coll_2_2)
allpolys.append(coll_2_3)

allpolys.append(coll_pipe01)
allpolys.append(coll_pipe02)

allpolys.append(coll_pipe11_1)
allpolys.append(coll_pipe12_1)

#allpolys.append(coll_pipe11)
#allpolys.append(coll_pipe12)

#allpolys.append(coll_pipe21)
#allpolys.append(coll_pipe22)

allpolys.append(coll_pipe31)
allpolys.append(coll_pipe32)

allpolys.append(coll_pipe41)
allpolys.append(coll_pipe42)

allpolys.append(coll_pipe51)
allpolys.append(coll_pipe52)

allpolys.append(coll_pipe61)
allpolys.append(coll_pipe62)

allpolys.append(coll_pipe71)
allpolys.append(coll_pipe72)

allpolys.append(coll_pipe81)
allpolys.append(coll_pipe82)

allpolys.append(coll_pipe91)
allpolys.append(coll_pipe92)

allpolys.append(coll_pipe101)
allpolys.append(coll_pipe102)

allpolys.append(coll_pipe111)
allpolys.append(coll_pipe112)

allpolys.append(coll_pipe121)
allpolys.append(coll_pipe122)

allpolys.append(coll_pipe131)
allpolys.append(coll_pipe132)

allpolys.append(coll_pipe141)
allpolys.append(coll_pipe142)

allpolys.append(coll_pipe151)
allpolys.append(coll_pipe152)

allpolys.append(coll_pipe161)
allpolys.append(coll_pipe162)

allpolys.append(coll_4_1)
allpolys.append(coll_4_2)
allpolys.append(coll_4_3)


allpolys.append(coll_5)
allpolys.append(lintel)

allpolys.append(quartz1)
allpolys.append(quartz2)
#allpolys.append(sub_quartz1)
#allpolys.append(sub_quartz2)

########################################################################
#  Rough out blocking areas

#for i in range(6):
#    z = 10 + i*3.0
#    ghost  = polygon(([z,-1.4],[z+0.001,-1.4],[z+0.001,1.4], [z,1.4]), isEthereal=True )
#   ghost  = polygon(([z,-1.4],[z+1.5,-1.4],[z+1.5,1.4], [z,1.4]), isEthereal=True )
#    allpolys.append(ghost)

#  One bounce ghost regions
##################################1
#ghost1a = polygon(([28,-1.4], [28, -1.39], [uscoll1_z-uscoll1_thick/2+0.01, uscoll1_r1_up], [uscoll1_z-uscoll1_thick/2, uscoll1_r1_up]), isEthereal=True)
###############################################2
#ghost1b = polygon(([28,-0.6], [28, -0.59], [uscoll1_z+uscoll1_thick/2+0.01, uscoll1_r1_dn], [uscoll1_z+uscoll1_thick/2, uscoll1_r1_dn]), isEthereal=True)

#ghost2a = polygon(([28,-1.4], [28, -1.39], [dscoll1_z-dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z-dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

#ghost2b = polygon(([28,-0.6], [28, -0.59], [dscoll1_z+dscoll1_thick/2+0.01, dscoll1_r1], [dscoll1_z+dscoll1_thick/2, dscoll1_r1]), isEthereal=True)

#allpolys.append(ghost1a)
#allpolys.append(ghost1b)
#allpolys.append(ghost2a)
#allpolys.append(ghost2b)

#  Raw

#z1 = 6.1
#z2 = 7.1

#t = uscoll2_r2 - uscoll2_r1

#slope = (dscoll2_r1- uscoll2_r1)/(dscoll2_thick/2+dscoll2_z - uscoll2_z-uscoll2_thick/2)

#gr1 = uscoll2_r1 + slope*(z1 - uscoll2_z - uscoll2_thick/2)
#gr2 = uscoll2_r1 + slope*(z2 - uscoll2_z - uscoll2_thick/2)

#smallghost1 = polygon(( [z1, -gr1-t], [z2, -gr2-t], [z2, -gr2], [z1, -gr1]), isEthereal = False)

#print "Ghost blocking points:"
#print smallghost1.pts[0][0], smallghost1.pts[0][1]
#print "\t", smallghost1.pts[3][1]
#print smallghost1.pts[1][0], smallghost1.pts[1][1]
#print "\t", smallghost1.pts[2][1]


#smallghost2 = polygon( ([10.1729, -0.0277], [10.7712, -0.0738], [13.7226, -0.1123], [11.374, -0.0320] ), isEthereal=False)

#smallghost1 = polygon(( [6.3932, -0.0350], [8.0240, -0.0425], [7.6242, -0.0334], [6.2734, -0.0281]), isEthereal = False)
#smallghost2 = polygon( ([10.1729, -0.0277], [10.6515, -0.0566], [13.2529, -0.0882], [11.374, -0.0320] ), isEthereal=False)


# straight z
#smallghost1 = polygon(( [6.2734, -0.0334], [7.6852, -0.0385], [7.6852, -0.0334], [6.2734, -0.0281]), isEthereal = False)
#smallghost2 = polygon( ([10.1729, -0.0277], [10.1729, -0.0566], [11.3749, -0.0566], [11.374, -0.0320] ), isEthereal=False)

# Reduce z
#smallghost1 = polygon(( [6.273, -0.039 ], [7.874, -0.0474], [7.874, -0.0383691664116], [6.273, -0.0274]), isEthereal = False)
#smallghost2 = polygon( ([10.472, -0.0431780215291], [10.472, -0.0697], [12.074, -0.079], [12.074, -0.0490] ), isEthereal=False)

#################################################################
#allpolys.append(smallghost1)
###by YX3
#################################################################

#allpolys.append(smallghost2)

#print sources
#print allpolys

print "Starting"

for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light( sources, otherpolys )

print "Doing once bounce lighting"

# One bounce
for apoly in allpolys:
    otherpolys = list(allpolys)
    otherpolys.remove(apoly)
    apoly.light(otherpolys, [], 2 )

#print "Ghost intersections:"

#  Print out ghost region values
#for aghost in [ghost1a, ghost1b, smallghost1]:
#    for aface in aghost.faces:
#	print "Of ", aface.v1[0], aface.v1[1], " -> ", aface.v2[0], aface.v2[1]
#	for lface in aface.getlitfaces():
#	    print "\t", lface.v1[0], lface.v1[1], " -> ", lface.v2[0], lface.v2[1]

mydraw = drawlight(allpolys+sources)

Gtk.main()
