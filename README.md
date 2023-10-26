# csgo_elo

### Important notice about CS2
-----------------------

Due to the release of CS2 and Valve wiping CS:GO off the face of the earth, this repository is now going to be archived.<br> N.B It is currently unknown whether this programs calculations are even remotely accurate in CS2

-----------------------

A program for calculating approximate SG2 elo gain from CS:GO matches

IMPORTANT: This program is written in python, and for simplification reasons it requires python (https://www.python.org/) to be installed on your local machine in order to run

The executable file (the file you actually need) is csgo_elo.py

About the SG2 elo system:
  - SG2 stands for simplified Glicko-2. Glicko-2 is the system CS:GO uses for calculating elo.
  - It is important to understand that the SG2 system is a mostly accurate estimation of the Actual Glicko-2 system.
  - It is also important to know that the Glicko-2 system is used by CS:GO to calculate elo, used for matchmaking and the elo itself is not even a direct           representation of your rank, so the SG2 system is essentially an estimate of an estimate of your rank, so it should not be taken as a direct rankup             calculation.
  - More information about the SG2 system along with the equation for calculating it used in this program can be found in this steam community post:                 https://steamcommunity.com/sharedfiles/filedetails/?id=888007256
  
  
  This is a very simple program and is not endorsed by or related to Valve or CS:GO
