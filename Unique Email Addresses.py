https://leetcode.com/problems/unique-email-addresses/
  
from collections import defaultdict

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        domain_dict = defaultdict(set)

        for email in emails:
            local_name, domain_name = email.split('@')
            
            # local_name.split('+')[0] gives us everything before the + sign
            # .replace('.','') replaces all . to a empty space.
            domain_dict[domain_name].add(local_name.split('+')[0].replace('.',''))
            
        unique_emails = 0
        for domain in domain_dict:
            unique_emails += len(domain_dict[domain])
             
        return unique_emails
