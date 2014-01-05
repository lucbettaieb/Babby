package babbydad;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.*;

import javax.swing.JFrame;

/**
 * @author Luc A. Bettaieb
 * 
 * BabbyDad gets input from the keyboard and sends it over socket to the server.
 * 
 */

public class BabbyDad {

    public static void main(String[] args) throws IOException {
        JFrame frame = new JFrame("Key Listener");
        
               
        KeyListener listener;
        listener = new KeyListener() {
        CommandSender cs = new CommandSender("10.0.1.147",50000);
            
            public void keyTyped(KeyEvent e) {
                if(e.getKeyChar() == 'w'){
                    cs.send("w");
                }
                
                if(e.getKeyChar() == 'a'){
                    cs.send("a");
                }
                
                if(e.getKeyChar() == 's'){
                    cs.send("s");
                }
                
                if(e.getKeyChar() == 'd'){
                    cs.send("d");
                }  
                
                if(e.getKeyChar() == 'q'){
                    cs.close();
                    System.exit(0);
                }
            }

            public void keyPressed(KeyEvent e) {}
            public void keyReleased(KeyEvent e) {}
        };
        
        frame.addKeyListener(listener);
 
        frame.pack();
        frame.setVisible(true);

    }
}

    
