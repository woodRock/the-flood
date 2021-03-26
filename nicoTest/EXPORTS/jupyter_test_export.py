# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
msg= "helloooo!"
print( msg)
msg+=" world"


# %%
a= 3
b= 2
while a< 1000:
    a, b= b, a+ b
m= msg+" "+ str( a)
print( m)


# %%
from numpy import pi, cos, sin, sqrt, arange
import matplotlib.pyplot as pp

numPts= a #1000
print( "a: "+ str(a))
inds= arange( 0, numPts, dtype= float)+ 0.5

r= sqrt( inds/ numPts)
theta= pi*( 1+ 5** 0.5)* inds

pp.scatter( r* cos( theta), r* sin( theta))
pp.show()


# %%
import nbconvert


