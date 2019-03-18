from libraries.mpLogspace import mpLogspace
from mpmath import mpf

def StandardizeDistribution (xaxis,distribution):
    length = len(distribution)
    logXarray = xaxis
    
    surface = mpf('0')
    cdf=[mpf('0')]
    for i in range(1,length):
        surface += distribution[i]
        cdf.append(surface)                                            #eventually get cdf

    for i in range(0, length):
        #pdf[i]= distribution[2][i]                            #normalize pdf and cdf ( now: surface = 1 )
        cdf[i] = cdf[i] / surface
    stdDistribution = (length, logXarray, distribution, cdf )
    return stdDistribution


def StandardizeDistributionW(xaxis,distribution):
    length = len(distribution)
    logXarray = xaxis
    surfaceW = mpf('0')
    cdfW=[surfaceW]
    surface = mpf('0')
    cdf=[mpf('0')]
    #pdf=[None] * length
    for i in range(1,length):
        surfaceW += (logXarray[i]-logXarray[i-1])*distribution[i]
        cdfW.append(surfaceW)                                            #eventually get cdf
        surface += distribution[i]
        cdf.append(surface)
    
    max = 1
    for i in range(0, length):
        #pdf[i]= distribution[2][i]                            #normalize pdf and cdf ( now: surface = 1 )
        cdfW[i] = cdfW[i] / surfaceW
        cdf[i] = cdf[i] / surface
        if(distribution[i]>max):
            max = distribution[i]
    
    distribution = [d/max for d in distribution]
    
    stdDistribution = (length, logXarray, distribution, cdf,cdfW )
    return stdDistribution