import random
import time
import matplotlib.pyplot as plt
# from Tkinter import *

if __name__ == "__main__":
	plt.figure(1)
	t = []
	m = random.randint(200000, 400000)
	w = tuple([5 for j in range(-4000, 4000)])

	for i in range(300):
		plt.clf()
		k = random.choices([j for j in range(-4000, 4000)], weights = w, k=1)[0]
		print(k)

		if(m + k < m):
			w = tuple([10 for j in range(-4000, 0)] + [2 for j in range(-4000, 0)])
		else:
			w = tuple([2 for j in range(-4000, 0)] + [10 for j in range(-4000, 0)])

		m += k
		t += [m]
		t = t[-100:]
		plt.plot(t)
		avg = sum(t[-10:])/10
		if(avg < 150000 or avg>450000):
			plt.text(75, 550000, "Critical " + str(m), color = "red")
		else:
			plt.text(75, 550000, "Normal " + str(m), color = "green")

		plt.ylabel("Platelets")
		plt.axis([0, 100, 0, 600000])
		plt.pause(0.001)

	plt.show()