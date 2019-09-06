# Flatten a Dictionary
def flatten_dictionary(dictionary):
  ans = {}
  def recurs(keys, d):
    if type(d) is int or type(d) is str:
      ans['.'.join(keys)] = d
    else:
      for k, v in d.items():
        recurs(keys + ([k] if k else []), v)
  
  recurs([], dictionary)
  return ans