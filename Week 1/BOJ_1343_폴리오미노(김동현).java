import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String borad = br.readLine();

        borad = borad.replaceAll("XXXX", "AAAA");
        borad = borad.replaceAll("XX", "BB");

        if(borad.contains("X")){
            System.out.println("-1");
        }else{
            System.out.println(borad);
        }

    }
}