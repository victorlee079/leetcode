class Solution {
    private int maxTime = -1;

    private void buildTime(int[] array) {
        int hours = array[0] * 10 + array[1];
        int minutes = array[2] * 10 + array[3];
        if (hours < 24 && minutes < 60) {
            maxTime = Math.max(maxTime, hours * 60 + minutes);
        }
    }

    private void swap(int[] array, int i, int j) {
        if (i != j) {
            int temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
    }

    private void permutate(int[] array, int start) {
        if (start == array.length) {
            buildTime(array);
            return;
        }

        for (int i = start; i < array.length; i++) {
            swap(array, i, start);
            permutate(array, start+1);
            swap(array, i, start);
        }
    }

    public String largestTimeFromDigits(int[] arr) {
        permutate(arr, 0);
        if (maxTime > -1) {
            return String.format("%02d:%02d", maxTime / 60, maxTime % 60);
        } else {
            return "";
        }
    }
}
