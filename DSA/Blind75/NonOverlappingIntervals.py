def minRemovels (ranges):

	size = len(ranges)
	rem = 0

	# Sort by minimum starting point
	ranges.sort()

	end = ranges[0][1]
	for i in range(1, size):

		# If the current starting point is less
		# than the previous interval's ending
		# point (ie. there is an overlap)
		if (ranges[i][0] < end):

			# Increase rem
			rem += 1

			# Remove the interval
			# with the higher ending point
			end = min(ranges[i][1], end)
			
		else:
			end = ranges[i][1]

	return rem

if __name__ == '__main__':
	
	Input = [ [ 19, 25 ],
			[ 10, 20 ],
			[ 16, 20 ] ]
				
	print(minRemovels(Input))
