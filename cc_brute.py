#!/usr/bin/env python3

# Celestial Compass brute-force script

# CONFIG
# 1 pos == 60 deg
startPos = [0, 0, 4]
# 1 rot == 60 deg == 1 moon
rotSpeed = [3, 3, 1]
# Define which positions are rotated together
# Positions: [0, 1, 2]
rotA = [1, 2]
rotB = [0, 1]
rotC = [0, 2]
# /CONFIG

import sys

for rnA in range(10):
    for rnB in range(10):
        for rnC in range(10):
            # Goal: currPos == [0, 0, 0]
            currPos = startPos.copy()
            
            for posID in rotA:
                currPos[posID] = (currPos[posID] + (rotSpeed[posID] * rnA)) % 6
            for posID in rotB:
                currPos[posID] = (currPos[posID] + (rotSpeed[posID] * rnB)) % 6
            for posID in rotC:
                currPos[posID] = (currPos[posID] + (rotSpeed[posID] * rnC)) % 6
            
            if currPos == [0, 0, 0]:
                # Print number of rotations
                print(rnA, rnB, rnC)
                sys.exit(0)
