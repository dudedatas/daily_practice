"""
Date: 2026-04-02
Practice 
"""


import random
import math

def ab_game(rng=random) -> tuple[int, int]:
    """
    Simulates ONE complete game.
    Returns (Awin, Bwin) where exactly one of them is 1 and the other is 0.
    """
    while True:
        # Person A tosses a fair coin: 1=heads, 0=tails
        x = rng.choice([0, 1])
        if x == 1:
            return (1, 0)  # A wins immediately
        else:
            # Person B rolls a fair die: 1..6
            y = rng.randint(1, 6)
            if y <= 4:
                return (0, 1)  # B wins
            # else y in {5,6}: continue to next round


def simulate(nsims: int = 10_000, seed: int | None = 12345) -> tuple[float, float, tuple[float, float]]:
    """
    Runs nsims independent games, estimates P(A wins) and computes
    95% CI using the normal approximation:
        p_hat ± 1.96 * sqrt(p_hat(1-p_hat)/nsims)
    Returns (p_hat, err, (lo, hi))
    """
    rng = random.Random(seed)

    a_wins = 0
    for _ in range(nsims):
        Awin, _Bwin = ab_game(rng)
        a_wins += Awin

    p_hat = a_wins / nsims
    err = 1.96 * math.sqrt(p_hat * (1 - p_hat) / nsims)
    lo, hi = p_hat - err, p_hat + err
    return p_hat, err, (lo, hi)


if __name__ == "__main__":
    p_hat, err, (lo, hi) = simulate(nsims=10_000, seed=12345)
    print(f"estpA = {p_hat:.4f}")
    print(f"err   = {err:.4f}")
    print(f"95% CI: [{lo:.4f}, {hi:.4f}]")