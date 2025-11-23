import math
from statistics import mean, pstdev

def safe_mean(vals):
    return round(mean(vals), 2) if vals else 0.0

def margin_of_error(vals):
    n = len(vals)
    if n <= 1:
        return 0.0
    sd = pstdev(vals)
    me = sd / math.sqrt(n)
    return round(me, 2)
