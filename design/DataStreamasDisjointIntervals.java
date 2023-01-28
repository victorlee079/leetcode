class SummaryRanges {
    TreeSet<int[]> set;

    public SummaryRanges() {
        set = new TreeSet<>((a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
    }

    public void addNum(int value) {
        int[] cur = new int[] { value, value };

        if (set.contains(cur))
            return;

        int[] low = set.lower(cur);
        int[] high = set.higher(cur);

        if (high != null && high[0] == value)
            return;

        if (low != null && low[1] + 1 == value && high != null && value + 1 == high[0]) {
            low[1] = high[1];
            set.remove(high);
        }

        else if (low != null && low[1] + 1 >= value) {
            low[1] = Math.max(low[1], value);
        }

        else if (high != null && high[0] - 1 == value) {
            high[0] = value;
        } else {
            set.add(cur);
        }
    }

    public int[][] getIntervals() {
        List<int[]> res = new ArrayList<>();
        for (int[] c : set) {
            res.add(c);
        }
        return res.toArray(new int[res.size()][]);
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(value);
 * int[][] param_2 = obj.getIntervals();
 */