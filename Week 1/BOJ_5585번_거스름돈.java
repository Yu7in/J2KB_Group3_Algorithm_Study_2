import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int pay = scanner.nextInt();

        int money = 1000 - pay;
        int count = 0;

        while(money > 0){
            if(money >= 500){
                count++;
                money -= 500;
            }else if(money >= 100){
                count++;
                money -= 100;
            }else if(money >= 50){
                count++;
                money -= 50;
            }else if(money >= 10){
                count++;
                money -= 10;
            }else if(money >= 5){
                count++;
                money -= 5;
            }else{
                count++;
                money -= 1;
            }
        }
        System.out.println(count);
    }
}