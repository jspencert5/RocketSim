## Refactor Notes (3/14)
The project structure has been changed, and see doc on Discord for assignments. SQLAlchemy and Scipy are now added as requirements. To run the program, cd into the simluator director and run "python osim.py"

## Progress (2/20)
What I've done so far is create a small program that takes in an initial velocity from the user and the launch angle. It then calculates the max height, max distance (horizontal), and time of flight. Once the time of flight is calculated, it is passed into the linspace function to create an array of evenly spaced time points, at a resolution of 30 per second (time of flight * 30). The time array is then passed to an X and Y position function and X,Y coordinates at each time point are calculated. These points are then plotted on a graph and the max statistics are printed.

## What to Work On
- Work on thrust math
- Incorporate mass into the calculations
- Export position data to CSV file
