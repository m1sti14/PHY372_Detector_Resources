from matplotlib import pyplot as plt
import numpy as np
import csv

data = np.genfromtxt('beamSize.csv', delimiter = ',')
print(data.shape)
x = data[:,8]
y = data[:,7]
plt.figure()
plt.plot(x,y)
#plt.show()

x = [0,
5,
10,
15,
20,
25,
30,
35,
40,
45,
50,
55,
60,
65,
70,
75,
80,
85,
90,
95,
100,
105,
110,
115,
120,
]
y = [92,
157,
265,
396,
570,
817,
1100,
1450,
1720,
2018,
2211,
2408,
2630,
2690,
2590,
2435,
2150,
1830,
1450,
1040,
702,
443,
285,
174,
103,
]
plt.figure()
plt.plot(x,y)
#plt.show()

x = [0,
0.1,
0.2,
0.3,
0.4,
0.5,
0.6,
0.7,
0.8,
0.9,
1,
1.1,
1.2,
1.3,
1.4,
]
y = [590,
579,
578,
576,
563,
545,
513,
471,
325,
261,
112,
46.1,
15.2,
10.7,
8.6,
]

plt.figure()
plt.plot(x,y)
plt.show()