class Solution {
    fun removeStars(s: String): String {
        val stk = ArrayDeque<Char>()
        for (c in s) {
            when (c) {
                '*' -> if (!stk.isEmpty()) stk.removeLast()
                else -> {
                    stk.add(c)
                }
            }
        }
        return stk.joinToString("")
    }
}
