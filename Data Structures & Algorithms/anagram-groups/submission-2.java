class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
         Map<String,List<String>> n_map=new HashMap<>();
         for (String s: strs){
            int[] buck=new int[26];
            for (char c: s.toCharArray()){
                buck[c-'a']++;

            }
            String buck_s=Arrays.toString(buck);
            n_map.putIfAbsent(buck_s,new ArrayList<>());
            n_map.get(buck_s).add(s);
         }
         return new ArrayList<>(n_map.values());    
    }
}
