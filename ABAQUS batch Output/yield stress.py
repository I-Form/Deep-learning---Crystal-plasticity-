import matplotlib.pyplot as plt
def find_cross_point(x,y,k,b):
    '''
    :param x: an array of x
    :param y: an array of y
    :param k: the slope of the line
    :param b: the intercept of the line
    :return: x_c and y_c, the coordinate of cross point
    '''
    if len(x) != len(y):
        exit("Error! The length of x and y are not equal!")
    l = len(x)
    pre = x[0]
    pre_value = y[0] - (x[0] * k + b)
    for i in range(1,l):
        now = x[i]
        now_value = y[i] - (x[i] * k + b)
        if now_value == 0:
            return x[i],y[i]
        elif now_value * pre_value > 0:
            pre = x[i]
            pre_value = y[i]
            continue
        elif now_value * pre_value < 0:
            k_fit = (y[i] - y[i-1])/(x[i]-x[i-1])
            b_fit = y[i] - x[i] * k_fit
            x_c = (b_fit - b) / (k - k_fit)
            y_c = k * (b_fit - b)/(k - k_fit) + b
            return x_c, y_c

if __name__ == "__main__":
    y=[]
    y_file = open("CPStressTimetrace.out","r")
    for line in y_file.readlines():
        line = line.strip()
        if len(line) != 0:
            y.append(float(line))
    x=[]
    x_file = open("CPStrainTimetrace.out","r")
    for line in x_file.readlines():
        line = line.strip()
        if len(line) != 0:
            x.append(float(line))

    k = (y[1]/x[1] + y[2]/x[2] + y[3]/x[3] + y[4]/x[4] + y[5]/x[5]) / 5
    b = -0.002 * k
    end_y = max(y)*1.1
    end_x = (end_y - b) / k
    start_x = 0
    start_y = b
    x2 = [start_x, end_x]
    y2 = [start_y, end_y]
    plt.plot(x,y,color='red',label='Line1')
    plt.plot(x2,y2,color='skyblue',label='Line2',linestyle='--')
    
    plt.xlabel('Strain')
    plt.ylabel('Stress (MPa)')
    plt.xlim((0,end_x*1.1))
    plt.ylim((0,end_y*1.1))
    x_c, y_c = find_cross_point(x,y,k,b)
    plt.plot(x_c,y_c,'ro')
    plt.annotate(str(round(y_c,2)), xy=(x_c, y_c), xytext=(x_c, y_c*0.6),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
    print(x_c,y_c)
    plt.savefig("teriri.png")
    plt.show()

