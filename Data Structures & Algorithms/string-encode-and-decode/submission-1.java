class Solution {

    public String encode(List<String> strs) {
        StringBuilder res= new StringBuilder();
        for (String s: strs){
            res.append(s.length()).append('#').append(s);
        }
        return res.toString();

    }

    public List<String> decode(String str) {
        List<String> res=new ArrayList<>();
        int i=0;
        while(i<str.length()){
            int j=i;
            while(str.charAt(j)!='#'){
                j++;
            }
            int leng_s=Integer.parseInt(str.substring(i,j));
            i=j+1;
            j=i+leng_s;
            String word=str.substring(i,j);
            res.add(word);
            i=j;
        }
        return res;

    }
}
