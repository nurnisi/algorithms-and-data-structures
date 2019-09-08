# 937. Reorder Data in Log Files
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        for l in logs:
            lsp = l.split(' ')
            if lsp[1].isdigit(): digit_logs.append(l)
            else: letter_logs.append((lsp[1:], lsp[0]))
        return [' '.join([idn] + log) for log, idn in sorted(letter_logs)] + digit_logs

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def f(log):
            id_, rest = log.split(' ', 1)
            return (0, rest, id_) if not rest[0].isdigit() else (1,)
        return sorted(logs, key=f)