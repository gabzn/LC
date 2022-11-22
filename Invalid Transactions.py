https://leetcode.com/problems/invalid-transactions/
  
class Solution(object):
    def invalidTransactions(self, transactions):
        if not transactions:
            return []
        
        res = []
        
        # Split the string into a list and sort each transaction by the time.
        for ind, transaction in enumerate(transactions):
            transactions[ind] = transactions[ind].split(',')
        transactions.sort(key=lambda transaction: int(transaction[1])) 
                
        # For each transaction, compare the rest to see if it is invalid.
        for ind, transaction in enumerate(transactions):
            # Amount exceeds 1000.
            if int(transaction[2]) > 1000:
                res.append(",".join(transaction))
                continue
                
            # Compare all other transactions.
            for i in range(len(transactions)):
                # Skip the same transaction.
                if i == ind:
                    continue
                
                # Same name, within 60 mins, different city.
                if transactions[i][0] == transaction[0] and (abs(int(transactions[i][1]) - int(transaction[1])) <= 60) and transactions[i][3] != transaction[3]:
                    res.append(",".join(transaction))
                    break
        
        return res
