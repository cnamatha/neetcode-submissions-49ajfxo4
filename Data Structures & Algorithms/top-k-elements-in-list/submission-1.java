class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> c_map=new HashMap<>();
        List<List<Integer>> new_n=new ArrayList<>(nums.length+1);
        for (int i = 0; i <= nums.length; i++) {
            new_n.add(new ArrayList<>());
        }
        for (int i: nums){
            
            c_map.put(i,c_map.getOrDefault(i,0)+1);
        }
        for (int key_n:c_map.keySet()){
            int c_m=c_map.get(key_n);
            new_n.get(c_m).add(key_n);
        }
        int[] res=new int[k];
        int index=0;
        for (int i=new_n.size()-1;i>=0&&index<k;i--){
            for (int n:new_n.get(i)){
                res[index++]=n;
                if (index==k){
                    return res;
                }
            }
        }
        return res;



         
    }
}
