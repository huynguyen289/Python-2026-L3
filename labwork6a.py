import matplotlib.pyplot as po
import numpy as np
x = np.linspace(-5, 5, 100)
y = 2*x + np.sin(x)**2 + 3
po.plot(x, y)
po.grid(True)
po.title("hello.po")
po.savefig("po.pdf")
po.xlabel("x")
po.ylabel("y")
po.show()