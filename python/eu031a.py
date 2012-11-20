# project euler (projecteuler.net) problem 31
# solution by Kevin Retzke (retzkek@gmail.com), May 2012

def countCombinations(vals, total):
    if vals == []:
        return 1 if total == 0 else 0
    count = 0
    if vals[0] <= total:
        count += countCombinations(vals, total-vals[0])
    count += countCombinations(vals[1:], total)
    return count

if __name__=="__main__":
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    print countCombinations(coins, 200)
