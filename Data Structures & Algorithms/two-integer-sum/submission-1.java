class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> n_map=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int diff=target-nums[i];
            if (n_map.containsKey(diff)){
                return new int[]{n_map.get(diff),i};
            }
            n_map.put(nums[i],i);
        }
        return new int[]{};
    }
}
