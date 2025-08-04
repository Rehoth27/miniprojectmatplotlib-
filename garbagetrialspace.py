import matplotlib.pyplot as plt
import numpy as np
import mplcursors
subjects = ['Discrete Mathematics', 'Fundamentals of Data Science', 'Design Algorithms and Analysis', 'Parallel Programming with Python', 'Web Development Frameworks']
marks = [32, 38, 36, 31, 35]
plt.scatter(subjects,marks)
plt.plot(subjects,marks)
plt.title('Internal Assessment I analysis', fontsize=20)
plt.xlabel('Subjects', fontsize=15)
plt.ylabel('Marks', fontsize=15)
plt.ylim(0, 50)
new_ticks = np.arange(0, 51, 5)
plt.yticks(new_ticks)
plt.grid(True, linestyle='--', alpha=0.6)
mplcursors.cursor(hover=True)
plt.show()
