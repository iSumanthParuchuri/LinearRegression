import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
	# number of observations/points 
	n = np.size(x) 

	# mean of x and y vector 
	m_x, m_y = np.mean(x), np.mean(y) 

	# calculating cross-deviation and deviation about x 
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	# calculating regression coefficients 
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 

	return(b_0, b_1) 

def plot_regression_line(x, y, b): 
	# plotting the actual points as scatter plot 
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 50) 

	# predicted response vector 
	y_pred = b[0] + b[1]*x 

	# plotting the regression line 
	plt.plot(x, y_pred, color = "g") 

	# putting labels 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# function to show plot 
	plt.show() 

def main(): 
    # observations 
    #x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    #y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
    df = pd.read_excel('sales-1.xlsx', sheet_name='Regression analysis' , usecols = ["Rainfall (mm)","Umbrellas sold"])

    y = np.array(df["Rainfall (mm)"])
    z = np.array(df["Umbrellas sold"])
    a = [x for x in y if ~np.isnan(x)]
    b = [x for x in z if ~np.isnan(x)]
    x = np.array(a)
    y = np.array(b)    

    #x = np.array([0, 1, 2, 3, 4, 5])
    #y = np.array([1, 2, 3, 4, 5, 6])

    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\n b_0 = {} \n b_1 = {}".format(b[0], b[1])) 

    # plotting regression line 
    plot_regression_line(x, y, b) 

if __name__ == "__main__": 
	main() 
	
#Results in snapshot-1.1 and snapshot-1.2
