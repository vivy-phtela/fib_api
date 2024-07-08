from functools import lru_cache

@lru_cache
def calculate_fibonacci(n: int) -> int:
    """
    n番目のフィボナッチ数を計算
    
    Parameters
    ----------
    n : int
        計算したいフィボナッチ数の番号

    Returns
    ----------
    nth_fibonacci : int
        n番目のフィボナッチ数
    """
    if n == 1 or n == 2:
        return 1
    previous, current = 1, 1
    for _ in range(2, n):
        previous, current = current, previous + current
    return current