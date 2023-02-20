public class MovingInABoard {
    public static String run(String startPosition, int R, int C) {
        final int boardSize = 8;
        final int cpNum = 49;
        final int cpSmallLetter = 97;
        int startRow = startPosition.codePointAt(0) - cpNum;
        int startCol = startPosition.codePointAt(1) - cpSmallLetter;
        int endRow = (startRow + R) % boardSize;
        int endCol = (startCol + C) % boardSize;
        String endPosition = "" + (endRow + 1) + (char) (endCol + cpSmallLetter);
        return endPosition;
    }
}
