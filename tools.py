xrng = lambda nx, y: [nx, y != 1 and xrng(nx, y-1) + [y-1]][y != 1]
rng = lambda y: xrng([0], y)
norng = lambda y: [1] * y