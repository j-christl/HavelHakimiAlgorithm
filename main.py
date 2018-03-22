# Small python3 program implementing the
# Havel-Hakimi algorithm (recursively)
# to decide if there exists a graph
# for a given degree sequence
#
# https://github.com/yoshc


def main():
    # example 1: (1, 1, 2, 3, 4, 4, 5)
    # is a valid degree sequence
    print("\nSequence 1:")
    havel_hakimi([1, 1, 2, 3, 4, 4, 5])

    # example 2: (2, 2, 2, 2, 3)
    # is a valid degree sequence
    print("\nSequence 2:")
    havel_hakimi([2, 2, 2, 2, 3])


def havel_hakimi(seq):
    # if seq is empty or only contains zeros,
    # degree sequence is valid
    if len(seq) < 1 or all(deg == 0 for deg in seq):
        print("Finished! Graph IS constructable with Havel Hakimi algorithm.")
        return True

    print(seq, end="")
    seq.sort()
    print(" --sort--> ", end="")
    print(seq)

    last = seq[len(seq)-1]
    if last > len(seq)-1:
        print("Failed! Graph IS NOT constructable with Havel Hakimi algorithm.")
        return False

    print(seq, end="")

    # remove last element
    seq.remove(last)

    # iterate seq backwards
    for num in range(len(seq)-1, len(seq)-last-1, -1):
        if seq[num] > 0:
            seq[num] -= 1
        else:
            print("\nFailed! Graph is not constructable with Havel Hakimi algorithm")
            return False

    print(" --alg-->", end="")
    print(seq)

    # recursive call
    havel_hakimi(seq)


if __name__ == "__main__":
    main()
