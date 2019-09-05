# Busiest Time in The Mall
def find_busiest_period(data):
  peak_time = peak_vis = cur_vis = i = 0
  
  while i < len(data):
    time, v, enter = data[i]
    cur_vis += v if enter else -v
    
    if i == len(data)-1 or time != data[i+1][0]:
      if cur_vis > peak_vis:
        peak_vis = cur_vis
        peak_time = time
        
    i += 1

  return peak_time