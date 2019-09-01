# 937. Reorder Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for i, l in enumerate(logs):
            spl = l.split(' ')
            if spl[1].isnumeric():
                digit_logs.append(l)
            else:
                letter_logs.append([' '.join(spl[1:] + spl[:1]), i])
        
        return [logs[i] for _, i in sorted(letter_logs)] + digit_logs