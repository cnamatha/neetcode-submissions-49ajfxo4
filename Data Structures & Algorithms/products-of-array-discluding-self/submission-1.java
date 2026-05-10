class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n=nums.length;
        int forw=1;
        int backw =1;
        int[] res=new int[n];
        Arrays.fill(res,1);
        for (int i=0;i<n;i++){
            res[i]*=forw;
            forw*=nums[i];
        }
        for (int i=n-1;i>=0;i--){
            res[i]*=backw;
            backw*=nums[i];
        }
        return res;
    }
}  
