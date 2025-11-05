class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        int total= (n*(n+1))/2;
        int sumArr=0;
        for(int i: nums){
            sumArr+=i;
        }
        return total-sumArr;

        
    }
}