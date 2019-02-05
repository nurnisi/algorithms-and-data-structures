import sys
import collections

class Tracker:
    def __init__(self):
        # dictionary to store hostnames and corresponding server numbers
        self.hosts = collections.defaultdict(list)

    def next_server_number(self, array):
        array.sort()
        
        # return 1 if 1st number is not 1
        if array and array[0] != 1:
            return 1

        # search for the smallest number
        for i in range(1, len(array)):
            # if two consecutive numbers are not equal and
            # difference between them is bigger than 1 return next smallest
            if array[i] != array[i - 1] and array[i] - array[i - 1] != 1:
                return array[i - 1] + 1

        # if no such numbers found return length + 1
        return len(array) + 1

    def allocate(self, host_type):
        # get next server number
        number = self.next_server_number(self.hosts[host_type])

        # append the number to array of host's numbers
        self.hosts[host_type].append(number)

        # return allocated hostname
        return ''.join((host_type, str(number)))

    def deallocate(self, hostname):
        # get index of host number from hostname
        i = len(hostname) - 1
        while hostname[i].isnumeric():
            i -= 1

        # split hostname into name and number
        name, number = hostname[:i+1], int(hostname[i+1:])

        # check validity of hostname
        if name not in self.hosts and number not in self.hosts[name]:
            return "There is no host with name: {}".format(hostname)

        # deallocate hostname
        self.hosts[name].remove(number)