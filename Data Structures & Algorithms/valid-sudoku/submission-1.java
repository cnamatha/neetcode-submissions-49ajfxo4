class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer,Set<Integer>> rows=new HashMap<>();
        Map<Integer,Set<Integer>> cols=new HashMap<>();
        Map<String,Set<Integer>> boxes=new HashMap<>();
        for (int i=0;i<=8;i++){
            for (int j=0;j<9;j++){
                if (board[i][j]=='.'){
                    continue;
                }
                int val=board[i][j];
                String ind=i/3+","+j/3;
                if (rows.computeIfAbsent(i,k -> new HashSet<>()).contains(val) || cols.computeIfAbsent(j,k -> new HashSet()).contains(val) || boxes.computeIfAbsent(ind, k -> new HashSet<>()).contains(val)){
                    return false;
                }
                rows.get(i).add(val);
                cols.get(j).add(val);
                boxes.get(ind).add(val);

            }
        }
        return true;
    }
}
