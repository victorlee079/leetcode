class MisèreNim {
    public static String misereNim(List<Integer> s) {
        boolean allIsOne = true;
        for (int i : s) {
            if (i != 1) {
                allIsOne = false;
                break;
            }
        }
        Integer res = s.stream().reduce((x, y) -> (x ^ y)).get();
        if (allIsOne) {
            if (s.size() % 2 == 0) return "First";
            else return "Second";
        } 
        else if (res == 0) {
            return "Second";
        }
        else {
            return "First";
        }
    }
}
