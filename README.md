# Q-Learning-With-Frozen-Lake
In this RL project we take advantage of Q-learning to solve Frozen Lake. 
In the Frozen Lake environment, the AI, or agent, has the challenge of moving from an initial tile to the goal, while trying to avoid any of the possible holes in the tiles. In Frozen Lake, we have 16 tiles and our agent is positioned in each one, resulting in 16 unique states. For each state, there are 4 actions available to our agent: left, down, right, and up. The objective is to learn which action will yield the best outcome in any given state. We need to find 64 quality values to correspond to the 16 states and 4 actions.

◀️ LEFT = 0
🔽 DOWN = 1
▶️ RIGHT = 2
🔼 UP = 3


Learning Rate - α
In order to maintain a balance between existing knowledge and new information, we set the learning rate, α, between 0 and 1. When α is 0, the original value remains unchanged, but when α is 1, the value is altered rapidly. In our experiment, we chose not to set a limit on the learning rate, setting α at 1; however, this proved to be too extreme, as the rewards and maximum value of the subsequent state superseded the current value.

Gamma - γ
The discount factor (γ) lies between 0 and 1 and defines how much an agent prioritizes future rewards compared to those in the present. When γ=0, the agent focuses solely on current rewards; on the other hand, γ=1 gives any potential future reward the same value as immediate rewards. In the case of the Frozen Lake game, a high discount factor is desired as there is only one reward to be earned at the end of the game.


Training ...


Epsilon-Greedy Algorithm
We must balance the behavior of our agent between EXPLORATION and EXPLOITATION. If the agent only focuses on exploitation, they can not learn new solutions. Similarly, if they only take random actions, they will not use the Q-table to make the training meaningful. We can adjust the level of randomness in the action selection over time, giving more focus to exploration at the start of the training, as it is important for discovering unknown state-action pairs. As the agent becomes more familiar with the environment, exploration will become less and less necessary.

Epsilon
Epsilon is an integral factor when choosing particular moves, relying on the Q values that we possess. For instance, if we elect to take a pure greedy approach (where epsilon equals 0), we will select the highest Q value among all the values pertaining to a certain state. However, this could potentially cause problems when attempting to explore as we could get caught in a local optimum. To combat this, randomness is added by having a given epsilon value, such as 1. By having this, actions are taken randomly at a 1 chance, disregarding the actual Q value. Thus, epsilon affects how much of a role randomness has in an action.
The agent now requires more time to achieve victory consistently, since its Q-table now has significantly more non-zero values than its previous incarnation. This indicates that it has managed to learn a variety of different action sequences to reach the goal, as it has been mandated to explore new state-action pairs rather than simply relying on the existing non-zero values.


Conclusion
The agent needs to meet the goal in a minimum number of actions with the least Training Episodes Which is set at 20 and 200 respectively. In evaluation, the minimum number of actions to complete the game is 6. 
