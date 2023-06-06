class test {
    public static void main(String[] args) {
        int[] x = {5, 3, 4, 1, 2};

        for(int i = 1; i < x.length; i++) {
            int val = x[i];
            int j = i - 1;

            while (j >= 0 && x[j] > val) {
                x[j + 1] = x[j];
                j--;
            }

            x[j + 1] = val;
            
            for(int e : x) {
                System.out.print(e + " ");
            }
            System.out.println();
        }
    }
}