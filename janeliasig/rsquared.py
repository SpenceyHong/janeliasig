def rsquared(x, y):
    
    slope, intercept, r_value, p_value, std_err = sp.stats.linregress(x, y)
    return r_value ** 2