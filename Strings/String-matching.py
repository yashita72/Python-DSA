def matchingStrings(stringList, queries):
    result = []

    for i in range(len(queries)):
        count = 0

        for j in range(len(stringList)):
            if queries[i] == stringList[j]:
                count += 1

        result.append(count)

    return result
#hackerrank  problem solved using brute force approach