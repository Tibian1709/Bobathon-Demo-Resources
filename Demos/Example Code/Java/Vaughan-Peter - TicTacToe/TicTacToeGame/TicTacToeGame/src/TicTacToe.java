import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;


/**
 * Simple Tic-Tac-Toe in one file using Java Swing.
 * - Two-player (pass-and-play) on one computer
 * - Shows status, detects wins/draws
 * - Includes a Reset Game button
 *
 * How to run in IntelliJ:
 * 1) File → New Project → Language: Java → (choose SDK 17+)
 * 2) Create an empty project, then add a new Java class named `TicTacToe`.
 * 3) Paste this file's contents and click the green ▶ next to `main`.
 */

public class TicTacToe extends JFrame {
    private final JButton[][] cells = new JButton[3][3];
    private final JLabel status = new JLabel("X's turn", SwingConstants.CENTER);
    private final JButton resetButton = new JButton("Reset Game");


    private char current = 'X';
    private boolean gameOver = false;


    public TicTacToe() {
        super("Tic-Tac-Toe — Java Swing");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout(8, 8));


        // Header/status
        status.setFont(status.getFont().deriveFont(Font.BOLD, 18f));
        status.setBorder(BorderFactory.createEmptyBorder(8, 8, 8, 8));
        add(status, BorderLayout.NORTH);


        // Board grid
        JPanel grid = new JPanel(new GridLayout(3, 3, 6, 6));
        grid.setBorder(BorderFactory.createEmptyBorder(8, 8, 8, 8));
        Font cellFont = new Font(Font.SANS_SERIF, Font.BOLD, 48);

        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                JButton b = new JButton("");
                b.setFont(cellFont);
                b.setFocusPainted(false);
                b.setBackground(Color.WHITE);
                final int row = r;
                final int col = c;
                b.addActionListener((ActionEvent e) -> onCellClick(row, col));
                cells[r][c] = b;
                grid.add(b);
            }
        }
        add(grid, BorderLayout.CENTER);

        // Footer with reset
        JPanel footer = new JPanel(new FlowLayout(FlowLayout.CENTER));
        resetButton.addActionListener(e -> reset());
        footer.add(resetButton);
        add(footer, BorderLayout.SOUTH);


        setSize(360, 420);
        setLocationRelativeTo(null);
    }

    private void onCellClick(int r, int c) {
        if (gameOver) return;
        JButton b = cells[r][c];
        if (!b.getText().isEmpty()) return; // already played

        b.setBackground(Color.darkGray);
        b.setText(String.valueOf(current));
        b.setForeground(current == 'X' ? new Color(30, 144, 255) : new Color(220, 20, 60));


        if (isWin(current)) {
            status.setText(current + " wins! 🎉");
            gameOver = true;
            highlightWinningLine(current);
        } else if (isDraw()) {
            status.setText("It's a draw.");
            gameOver = true;
        } else {
            current = (current == 'X') ? 'O' : 'X';
            status.setText(current + "'s turn");
        }
    }

    private boolean isWin(char p) {
        // Rows & columns
        for (int i = 0; i < 3; i++) {
            if (eq(cells[i][0], p) && eq(cells[i][1], p) && eq(cells[i][2], p)) return true;
            if (eq(cells[0][i], p) && eq(cells[1][i], p) && eq(cells[2][i], p)) return true;
        }
    // Diagonals
        return (eq(cells[0][0], p) && eq(cells[1][1], p) && eq(cells[2][2], p)) ||
                (eq(cells[0][2], p) && eq(cells[1][1], p) && eq(cells[2][0], p));
    }

    private boolean isDraw() {
        for (int r = 0; r < 3; r++)
            for (int c = 0; c < 3; c++)
                if (cells[r][c].getText().isEmpty()) return false;
        return true;
    }


    private boolean eq(JButton b, char p) {
        return p == b.getText().chars().findFirst().orElse('\0');
    }

    private void highlightWinningLine(char p) {
        // Highlight any line that matches player p
        Color winColor = new Color(255, 235, 59);
        for (int i = 0; i < 3; i++) {
            if (eq(cells[i][0], p) && eq(cells[i][1], p) && eq(cells[i][2], p)) {
                for (int c = 0; c < 3; c++) cells[i][c].setBackground(winColor);
            }
            if (eq(cells[0][i], p) && eq(cells[1][i], p) && eq(cells[2][i], p)) {
                for (int r = 0; r < 3; r++) cells[r][i].setBackground(winColor);
            }
        }
        if (eq(cells[0][0], p) && eq(cells[1][1], p) && eq(cells[2][2], p)) {
            cells[0][0].setBackground(winColor);
            cells[1][1].setBackground(winColor);
            cells[2][2].setBackground(winColor);
        }
        if (eq(cells[0][2], p) && eq(cells[1][1], p) && eq(cells[2][0], p)) {
            cells[0][2].setBackground(winColor);
            cells[1][1].setBackground(winColor);
            cells[2][0].setBackground(winColor);
        }
    }

    private void reset() {
        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                cells[r][c].setText("");
                cells[r][c].setBackground(Color.WHITE);
            }
        }
        current = 'X';
        gameOver = false;
        status.setText("X's turn");
    }
}