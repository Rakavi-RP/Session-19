# GridWorld Value Iteration Implementation

This repository contains a Python implementation of the value iteration algorithm for a 4x4 GridWorld problem.

## Problem Description

- The agent starts at the top-left corner (state 0) and tries to reach the bottom-right corner (state 15)
- The agent can move up, down, left, or right with equal probability 
- The rewards are -1 for each move, and the terminal state (bottom-right) has a reward of 0
- There are no obstacles in the grid
- Discount factor (gamma) = 1 
- The algorithm stops when the maximum change in V(s) across all states is < 1e-4

## Files

- `gridworld.py`: Python script that implements the value iteration algorithm

## How to Run

```bash
# Make sure you have NumPy installed
pip install numpy

# Run the Python script
python gridworld.py
```

## Output

After running the code, you should see output similar to:

```
Converged after 471 iterations.
Final Value Function:
[[-59.42367735 -57.42387125 -54.2813141  -51.71012579]
 [-57.42387125 -54.56699476 -49.71029394 -45.13926711]
 [-54.2813141  -49.71029394 -40.85391609 -29.99766609]
 [-51.71012579 -45.13926711 -29.99766609   0.        ]]
```

The exact values may vary slightly due to the order of operations and floating-point precision.

## Understanding the Output

The resulting 4x4 grid shows the expected value of starting from each state. Note:

- The terminal state (bottom-right) has a value of 0 (no further rewards)
- States closer to the terminal have higher (less negative) values
- The top-left state (starting point) has the lowest value since it's furthest from the goal

