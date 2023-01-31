https://leetcode.com/problems/accounts-merge/
  
1: Union Find
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            
            if rank[root_x] == rank[root_y]:
                root[root_y] = root_x
                rank[root_x] += 1
            elif rank[root_x] > rank[root_y]:
                root[root_y] = root_x
            else:
                root[root_x] = root_y
        
        N = len(accounts)
        root = [i for i in range(N)]
        rank = [1 for _ in range(N)]
        
        # Map each email to its index in the accounts list
        email_idx = collections.defaultdict(int)
        
        # Go through all the accounts and emails and merge ONLY the ones that are in common
        # [j1@g.com, j2@g.com]  -> group 3
        # Say j1@g.com previously showed up in group 1, we want to merge group 3 to group 1
        # However, since j2@g.com didn't show up in any group before, we still process it as in it's in group 3
        for idx, acc in enumerate(accounts):    
            for email in acc[1:]:
                if email not in email_idx:
                    email_idx[email] = idx
                else:
                    union(email_idx[email], idx)
        
        # Now we need to fix the root so all emails know what group they are 'really' in
        group_ids_to_accounts = collections.defaultdict(list) 
        for email in email_idx:
            # email_idx[email] = find(email_idx[email])
            # idx = email_idx[email]
            
            # The find function will fix the group id and return it
            group_id = find(email_idx[email])            
            group_ids_to_accounts[group_id].append(email) 
        
        res = []
        for group_id in group_ids_to_accounts:
            accts_in_same_group = sorted(group_ids_to_accounts[group_id])
            
            temp = [accounts[group_id][0]]
            temp.extend(accts_in_same_group) 
            
            res.append(temp)
        
        return res
----------------------------------------------------------------------------------------------------------------------------------------------
2: Iterative DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_owner = collections.defaultdict(str)
        graph = collections.defaultdict(set)
        
        for account in accounts:
            owner = account[0]
            first_email = account[1]
            
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                
                email_owner[email] = owner
        
        res = []
        visited_emails = set()
        
        for email in graph:
            if email in visited_emails:
                continue
                
            emails = []
            stack = [email]
            
            self.dfs(graph, stack, emails, visited_emails)
            
            emails.sort()
            res.append([email_owner[email]] + emails)
        
        return res
    
    def dfs(self, graph, stack, emails, visited_emails):
            while stack:
                node = stack.pop()
                if node in visited_emails:
                    continue
                
                visited_emails.add(node)
                emails.append(node)
                
                for neighbour in graph[node]:
                    stack.append(neighbour) 
---------------------------------------------------------------------------------------------------------------------------------------------------------
3: Recursive DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_owner = collections.defaultdict(str)
        graph = collections.defaultdict(set)
        
        # Build the graph
        for account in accounts:
            owner = account[0]
            first_email = account[1]
            
            for email in account[1:]:
                graph[first_email].add(email)
                graph[email].add(first_email)
                
                email_owner[email] = owner
        
        res = []
        visited_emails = set()
        
        for email in graph:
            if email in visited_emails:
                continue
                
            emails = []
            self.dfs(graph, email, emails, visited_emails)
            
            emails.sort()
            res.append([email_owner[email]] + emails)
        
        return res
    
    def dfs(self, graph, email, emails, visited_emails):
        visited_emails.add(email)
        emails.append(email)
        
        for neighbour in graph[email]:
            if neighbour not in visited_emails:
                self.dfs(graph, neighbour, emails, visited_emails)
