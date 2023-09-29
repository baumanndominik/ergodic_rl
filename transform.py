import numpy as np
import statsmodels.api as sm
import scipy.integrate as integrate
from scipy.interpolate import interp1d

def TS_VS(time_series_data, loess_span=0.2, min_integrate_range=0.01):

    lowess = sm.nonparametric.lowess
    ts=np.diff(time_series_data)**2
    array_loess=lowess(np.log(ts),time_series_data[:-1], frac=loess_span)
    function_loess = interp1d(array_loess[:,0], y=array_loess[:,1], bounds_error=False, kind='linear', fill_value='extrapolate')
    v=lambda x:np.exp(function_loess(x))

    h_func=lambda t:integrate.fixed_quad(lambda x:v(x)**(-1/2),min_integrate_range,t,n=1000)[0]
    
    return h_func