def apriori(filename, minsup):
    
    def prune(candidates, minsup):
        f = {}
        for c in candidates:
            if candidates[c] >= minsup:
                f[c] = candidates[c]
        return f
    
    def generate_candidate(dic):
        candidates = set()
        for key1 in dic:
            for key2 in dic:
                if key1 != key2 and key1[:-1] == key2[:-1]:
                    if ord(key1[-1]) <= ord(key2[-1]):
                        new_candidate = (key1 + key2[-1])
                    else:
                        new_candidate = (key2 + key1[-1])
                    pruned = False
                    for i in range(len(new_candidate)):
                        if new_candidate[:i] + new_candidate[i+1:] not in dic:
                            pruned = True
                            break
                    if pruned:
                        continue
                    else:
                        candidates.add(new_candidate)

        return candidates
    
    def count_candidate(candidates, transactions):
        cnt_candidates = {}
        for candidate in candidates:
            cnt_candidates[candidate] = 0
            candidate_set = set(candidate)
            for trans in transactions:
                if candidate_set.issubset(transactions[trans]):
                    cnt_candidates[candidate] += 1
        return cnt_candidates
    
    apriori_result = {} # default initialization

    # complete your code
    f = open(filename, "r")
    apriori_result[1] = {"c":{}}
    transaction_sets = {}
    i = 0
    for transaction in f:
        transaction_sets[i] = set()
        transaction = transaction.rstrip()
        for item in transaction:
            apriori_result[1]["c"][item] = (apriori_result[1]["c"][item] + 1) if item in apriori_result[1]["c"] else 1
            transaction_sets[i].add(item)
        i += 1
    apriori_result[1]["f"] = prune(apriori_result[1]["c"], minsup)

    scan = 2
    while len(apriori_result[scan-1]["f"]) > 1:
        candidates = generate_candidate(apriori_result[scan-1]["f"])
        cnt_candidates = count_candidate(candidates, transaction_sets)
        if not cnt_candidates:
            break
        apriori_result[scan] = {}
        apriori_result[scan]["c"] = cnt_candidates
        pruned_candidates = prune(cnt_candidates, minsup)
        apriori_result[scan]["f"] = pruned_candidates
        scan += 1

    return apriori_result