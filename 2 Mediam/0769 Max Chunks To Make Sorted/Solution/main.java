package Solution;

class main {
    public static int maxChunksToSorted(int[] arr) {
        int max = 0, cnt = 0;
        for (int i=0; i<arr.length; i++) {
            max = Math.max(max, arr[i]);
            if (max == i)
                cnt += 1;
        }
        return cnt;
    }

    public static void main(String[] args) {
        int[] arr = new int[]{4,3,2,1,0};
        System.out.println(maxChunksToSorted(arr));
    }
}