### Liquid Tube Game Solver
#### Using A Star Search Algorithm

This repository contains the solver for the Liquid Tube Game, which is a puzzle-solving application designed to automatically solve various configurations of the liquid tube puzzles. The puzzles involve a set of tubes filled with colored liquids, and the objective is to sort the liquids into tubes so that each tube contains liquid of only one color.

#### Features
- Supports solving puzzles with varying numbers of tubes, colors, and puzzle sizes.
- Includes multiple puzzle instances with different complexities and configurations.
- Outputs the step-by-step solution to each puzzle instance.

#### Files in the Repository
- `Instances.txt`: Contains the configurations for multiple puzzle instances. Each configuration specifies the number of empty tubes, filled tubes, total tube size, and the initial color distribution.
- `parseAndRun.py`: Script to parse the puzzle instances from `Instances.txt` and initiate the solving process.
- `puzzleSolver.py`: Core algorithm that implements the puzzle-solving logic based on the provided configurations.

#### How to Run
1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Navigate to the directory containing the scripts.
4. Run the command `python parseAndRun.py` to start solving puzzles. This script reads the puzzle configurations from `Instances.txt` and uses `puzzleSolver.py` to find and display the solutions.

#### Example Output
The output of the solver includes the steps required to sort the liquids in each tube, displayed sequentially for each puzzle instance. It provides clear guidance on which colors to move between tubes at each step.
```
==================================================
Test Case Index: 1
Number of Moves: 14
Total Checks: 37
Execution Time: 0.001065969467163086
```
#### Requirements
- Python 3.x