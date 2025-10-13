class Solution {
    public int maxArea(int[] height) {
        int max=0;
        int end=height.length - 1;
        int i=0;
        while(i<end){
            int l=Math.abs(end-i);
            int h=Math.min(height[i], height[end]);
            int total=h*l;
            if(total> max){
                max= total;
            }
            if(height[i]<height[end]) i++;
            else end--;
        }
        return max;
    }
}