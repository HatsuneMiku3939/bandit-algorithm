
def test_algorithm(algo, arms, times):
	result = []
	cumulative_reward = 0.0
	for t in range(times):
		chosen_arm = algo.select_arm()
		reward = arms[chosen_arm].draw()

		if t == 0:
			cumulative_reward = reward
		else:
			cumulative_reward = cumulative_reward + reward

		algo.update(chosen_arm, reward)
		result.append([t + 1, chosen_arm, reward, cumulative_reward])

	return result
