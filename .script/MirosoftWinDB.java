import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MirosoftWinDBGUI extends JFrame {

    public MirosoftWinDBGUI() {
        setTitle("MirosoftWinDB");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(5, 1));

        JButton fileExplorerButton = new JButton("File Explorer");
        JButton calculatorButton = new JButton("Calculator");
        JButton notepadButton = new JButton("Notepad");
        JButton settingsButton = new JButton("Settings");
        JButton exitButton = new JButton("Exit");

        fileExplorerButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                runPythonScript("file_explorer.py");
            }
        });

        calculatorButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                runPythonScript("calculator.py");
            }
        });

        notepadButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                runPythonScript("notepad.py");
            }
        });

        settingsButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                runPythonScript("settings.py");
            }
        });

        exitButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                System.exit(0);
            }
        });

        panel.add(fileExplorerButton);
        panel.add(calculatorButton);
        panel.add(notepadButton);
        panel.add(settingsButton);
        panel.add(exitButton);

        add(panel);
    }

    private void runPythonScript(String scriptName) {
        try {
            ProcessBuilder pb = new ProcessBuilder("python", scriptName);
            pb.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        EventQueue.invokeLater(() -> {
            MirosoftWinDBGUI gui = new MirosoftWinDBGUI();
            gui.setVisible(true);
        });
    }
}
