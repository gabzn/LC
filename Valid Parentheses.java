class Solution 
{
    public boolean isValid(String s) 
    {
        //Every length of valid parentheses MUST BE even.
        if(s.length() % 2 != 0) return false;
        
        Stack<Character> stack = new Stack<>();
        
        //Basic idea: go through every character in the string. If the character is the LEFT-SIDE parenthesis, we'll push its RIGHT-SIDE to the stack.
        //Whenever the character is not the LEFT-SIDE parenthesis, we check the latest pushed character to see if it is the same.
        //If it is not the same return false;
        
        for(int i=0;i<s.length();i++)
        {
            char currentChar = s.charAt(i);
            
            if(currentChar == '(' || currentChar == '[' || currentChar == '{')
            {
                if(currentChar == '(') stack.push(')');
                if(currentChar == '[') stack.push(']');
                if(currentChar == '{') stack.push('}');
                continue;
            }
            
            if(stack.empty() || stack.pop() != currentChar) return false;
        }
        
        //When the loop is finished, simply return if the stack is empty.
        //Valid parentheses will make the stack become empty in the end. 
        return stack.empty();
    }
}
