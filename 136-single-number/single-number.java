class Solution {
    public int singleNumber(int[] nums) {
        int n=nums.length;
        HashSet<Integer> set= new HashSet<>();
        for(int i :nums){
            if(set.contains(i)){
                set.remove(i);
            }
            else{
                set.add(i);
            }
      
        }
          for(int j: set){
                return j;
            }
        
       return -1;
    }
}