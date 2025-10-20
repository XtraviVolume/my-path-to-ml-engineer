import numpy as np
grades = np.random.randint(40,100, size=(5,4))
student = grades[2,:]
fails_counts = np.sum(grades<60)
sred = np.mean(grades, axis=0)
grades[grades<60]=60
