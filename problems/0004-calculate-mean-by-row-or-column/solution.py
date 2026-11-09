import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for x in matrix:
			means.append(np.mean(x))
	if mode == "column":
		for x in np.transpose(np.array(matrix)):
			means.append(np.mean(x))
	return means