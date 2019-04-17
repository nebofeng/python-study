import os
import sys
print("hello")
__console__=sys.stdout
f=open("out.txt","w")
sys.stdout=f
print("hello before close")

sys.stdout=__console__
print("hello after close")