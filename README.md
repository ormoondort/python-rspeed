# python-rspeed
split speed into x and y parts using direction

## Pre-requests
You don't need anything except python 3 to work with that.

## Usage
Basically, you have speed A and vector of direction that you use to move object.
```
from python-rspeed import split_speed

speed = 200
dir = {x=100, y=300}


dspeed = split_speed(speed, dir)

# so you have your speed split into x and y dimensions
# and any object can be moved in any direction with 
# same speed
print(dspeed.x)
print(dspeed.y)
```