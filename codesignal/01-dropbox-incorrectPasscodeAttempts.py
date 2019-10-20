def incorrectPasscodeAttempts(passcode, attempts):
    cnt = 0
    for att in attempts:
        if att == passcode:
            cnt = 0
        else:
            cnt += 1
            
        if cnt >= 10:
            return True
    return False