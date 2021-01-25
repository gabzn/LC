class Solution 
{
    public boolean checkIfExist(int[] arr) 
    {
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i=0;i<arr.length;i++)
        {
            if(map.containsKey(arr[i] * 2) || map.containsValue(arr[i])) return true;
            else    map.put(arr[i], arr[i] * 2);
        }
        
        return false;
    }
}

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.


Input: arr = [3,1,7,11]
Output: false
Explanation: In this case does not exist N and M, such that N = 2 * M.
