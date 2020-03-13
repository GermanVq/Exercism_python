def slices(series, length):
    if length > len(series) or length < 1 or len(series) == 0:
        raise ValueError("There is no series")
    else:
        return [series[i:i+ length] 
            for i in range(0, len(series)) 
                if len(series[i:i +length])==length]