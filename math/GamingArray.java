class GamingArray {
    public static String gamingArray(List<Integer> arr) {
    // Write your code here
        int cnt = 0;
        int largest = 0;
        for (int i : arr) {
            if (i > largest) {
                cnt++;
                largest = i;
            }
        }
        if (cnt % 2 == 0) {
            return "ANDY";
        }
        return "BOB";
    }
}
