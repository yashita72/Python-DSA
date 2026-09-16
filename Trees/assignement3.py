

def kth_moment(stream, k):
 
    counts = {}
    for item in stream:
        counts[item] = counts.get(item, 0) + 1

    # Step 2: sum of (frequency ^ k)
    moment = 0
    for item in counts:
        moment += counts[item] ** k

    return counts, moment


# ---------- Main ----------
data = input("Enter stream of size 20 (space separated): ").split()

if len(data) != 20:
    print("Error: stream must have exactly 20 elements. You entered", len(data))
else:
    k = int(input("Enter value of k: "))

    counts, moment = kth_moment(data, k)

    print("\n--- Result ---")
    print("Distinct elements :", len(counts))
    for item in counts:
        print("Element", item, "-> frequency =", counts[item])

    print("\n", k, "th moment =", moment, sep="")