# Time Planner
def meeting_planner(slotsA, slotsB, dur):
  i = j = 0
  while i < len(slotsA) and j < len(slotsB):
    a_start, a_end = slotsA[i]
    b_start, b_end = slotsB[j]
    
    over_start, over_end = max(a_start, b_start), min(a_end, b_end)
    if over_end - over_start >= dur:
      return [over_start, over_start+dur]
    
    if a_end < b_end:
      i += 1
    else:
      j += 1
  
  return []