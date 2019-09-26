class Solution:
	def islandPerimeter(self, grid: List[List[int]]) -> int:
		land_count = 0
		common_sides = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j]:
					land_count += 1

					if j != 0 and grid[i][j - 1]:
						common_sides += 1
					if j != len(grid[i]) - 1 and grid[i][j + 1]:
						common_sides += 1
					if i != 0 and grid[i - 1][j]:
						common_sides += 1
					if i != len(grid) - 1 and grid[i + 1][j]:
						common_sides += 1

		return 4 * land_count - common_sides
