def gaussian_kernel(sigma):
	x = np.arange(-200, 201)
	kernel = []

	for i in x:
		kernel.append(stats.norm.pdf(i, 0, sigma))
	return kernel