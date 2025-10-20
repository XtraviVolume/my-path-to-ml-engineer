import numpy as np

sales= np.random.randint(10,50,size=(3,4))
last_month_sales= np.random.randint(10,50,size=(3,4))
stores1_2=sales[:, :2]
diff = sales -last_month_sales
weekly = np.sum(sales,axis=1)