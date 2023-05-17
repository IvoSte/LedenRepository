def main():
    print("Hallo Leden!")


def test():
    print("Test")


def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonaci(n - 1) + fibonaci(n - 2)


# make gaussian
def gaussian(x, mu, sigma):
    return (
        1 / (sigma * math.sqrt(2 * math.pi)) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    )


if __name__ == "__main__":
    main()
