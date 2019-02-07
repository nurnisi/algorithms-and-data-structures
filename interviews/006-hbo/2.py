# In many scripting languages, single-quotes and double-quotes can be used 
# interchangeably. var foo = “bar”; and var foo = ‘bar’; are equivalent statements. 
# Much like standardizing on tabs or spaces for whitespace in a codebase, 
# let’s say that we want to standardize on one set of quotes or the other. 
# For this problem, we want to write a script that reads in files in such 
# a scripting language, such as javascript, and will convert them all to use 
# the specified convention. To simplify the problem, we can assume that 
# all of the inputs are valid javascript files.




# special cases
# \" and \' should not be converted

# input
# var foo = "bar" + " foo"
# output:
# var foo = 'bar'

# input
# var foo = "bar\""
# output:
# var foo = 'bar\"'

# input
# var foo = "bar's happy"
# output:
# var foo = 'bar\'s happy'

# input
# # bar's happy
# output 
# # bar's happy

# state = 0 -> in code, iterate until i switch a state 
# state = 1 -> in string starting with ", read string
# state = 2 -> in string starting with ', read string
# state = 3 -> in comment, ignore

class Converter:
    
    def main(self, path):
        # reading
        file = self.readFile(path)
        
        # processing
        processedFile = self.processFile(file)
        
        return processedFile
        
        
    # read a file
    def readFile(self, path):
        file = # read file
        return file
    
    # input: var foo = "bar" + " foo"
    # process: var foo = 'bar" + " foo"
    
    # input
    # var foo = "bar\""
    # output:
    # var foo = 'bar\"'
    
    
    # input
    # var foo = "bar's happy"
    # processing:
    # var foo = 'bar's
    # output:
    # var foo = 'bar\'s happy'
    
    # process the file
    def processFile(self, file):
        state = 0
        
        
        for line in file:
            
            for i, ch in enumarated(line):
                if state == 0:
                    if ch is "\"" or ch is "\'":
                        if ch is "\"": state = 1
                        else: state = 2
                        line[i] = "'"
                        
                elif state == 1:
                    if ch is "\'":
                        line.insert("\")
                        i += 1
                        
                    if (ch is "\"" or ch is "\'") and line[i - 1] != "\\":
                        line[i] = "'"
                        state = 0

                elif state == 2:
                    if (ch is "\"" or ch is "\'") and line[i - 1] != "\\":
                        line[i] = "'"
                        state = 0
                
                    
                elif state == 3:
                    state = 0
                    break
                    
                
        
