class Solution {
    public boolean isPalindrome(String s) {
        String str=s.toLowerCase().replaceAll("[^a-zA-Z0-9]","");
        String result=new StringBuilder(str).reverse().toString();
        return str.equals(result);
        
    }
}