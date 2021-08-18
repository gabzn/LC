A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. 

https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1229/


class Solution 
{
    public Node copyRandomList(Node head) 
    {
        if(head == null) return null;
        
        Node ptr = head;
        
        // Make a copy of each node in the original list and put them in a map.
        // Using a map to instantly look up old node -> new node.
        Map<Node, Node> nodeMap = new HashMap<>();
        while(ptr != null)
        {
            nodeMap.put(ptr, new Node(ptr.val));
            ptr = ptr.next;
        }
        
        // Reset ptr back to the head of the original list.
        // Go through the map again to connect next and random.
        ptr = head;
        while(ptr != null)
        {
            Node copyPtr = nodeMap.get(ptr);
            copyPtr.next = nodeMap.get(ptr.next);
            copyPtr.random = nodeMap.get(ptr.random);
            ptr = ptr.next;
        }
        return nodeMap.get(head);
    }
}
