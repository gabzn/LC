https://leetcode.com/problems/accounts-merge/
  
1: Iterative DFS
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
2: Recursive DFS
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
