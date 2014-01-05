package babbydad;

import java.io.*;
import java.net.*;

/**
 * @author Luc A. Bettaieb
 * Class for sending chars over socket to the python server.
 */

public class CommandSender {
    String host;
    int portnum;
    PrintWriter out;
    
    Socket dataSocket;
    
    public CommandSender(String server, int port){
        host = server;
        portnum = port;
        
        System.out.println("Connecting...");
        dataSocket = null;
        out = null;
        
        try {
            dataSocket = new Socket(host, portnum);
            out = new PrintWriter(dataSocket.getOutputStream(), true);
            
        } catch(UnknownHostException e){
            System.err.println("The host is messed up, check: "+host);
            System.exit(1);
        } catch(IOException e){
            System.err.println("Couldn't get IO for "+host);
            System.exit(1);
        }
        
        System.out.println("..connected!");
    }
    
    public void send(String input){
        out.println(input);
    }
    
    public void close(){
        out.close();
        try{
            dataSocket.close();
        } catch(IOException e){
            System.err.println("Something went wrong with closing the data socket.");
        }
    }
}