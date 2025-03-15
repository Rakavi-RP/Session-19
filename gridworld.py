import numpy as np

def calculate_gridworld_values():
    # Grid parameters
    N = 4  # 4x4 grid
    states = N * N
    terminal_state = states - 1  # Bottom-right corner (state 15)
    
    # Initialize value function with zeros
    V = np.zeros((N, N))
    
    # Rewards: -1 for each move, 0 for terminal state
    rewards = np.full((N, N), -1)
    rewards[N-1, N-1] = 0  # Terminal state has 0 reward
    
    # Define possible actions: up, down, left, right
    actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Parameters
    gamma = 1.0  # No discounting
    theta = 1e-4  # Convergence threshold
    
    # Value iteration
    iteration = 0
    while True:
        iteration += 1
        delta = 0  # Track maximum change
        V_new = np.copy(V)
        
        # For each state
        for i in range(N):
            for j in range(N):
                if i == N-1 and j == N-1:  # Skip terminal state
                    continue
                
                v = 0
                # For each action (with equal probability 0.25)
                for action in actions:
                    next_i = max(0, min(N-1, i + action[0]))
                    next_j = max(0, min(N-1, j + action[1]))
                    
                    # Calculate expected value
                    v += 0.25 * (rewards[i, j] + gamma * V[next_i, next_j])
                
                V_new[i, j] = v
                delta = max(delta, abs(V_new[i, j] - V[i, j]))
        
        # Update value function
        V = V_new
        
        # Check for convergence
        if delta < theta:
            print(f"Converged after {iteration} iterations.")
            break
    
    return V

if __name__ == "__main__":
    final_values = calculate_gridworld_values()
    print("Final Value Function:")
    print(final_values) 