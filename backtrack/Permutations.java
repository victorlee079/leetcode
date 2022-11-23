class Solution {
    private List<List<Integer>> result = new ArrayList<>();

    private void solve(int[] nums, int index) {
        if (index == nums.length) {
            List<Integer> path = new ArrayList<>();
            for (int num : nums) {
                path.add(num);
            }
            result.add(path);
            return;
        }

        for (int i = index; i < nums.length; i++) {
            swap(nums, i, index);
            solve(nums, index+1);
            swap(nums, i, index);
        }
    }

    private void swap(int[] arr, int i, int j) {
        if (i != j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    public List<List<Integer>> permute(int[] nums) {
        solve(nums, 0);
        return result;
    }
}
