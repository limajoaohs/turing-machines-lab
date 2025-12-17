import java.util.Scanner;
public class Gastos{ 
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String linha1 = sc.nextLine();
        String linha2 = sc.nextLine();
        String resposta = sc.nextLine();
        String[] meses = linha1.split(" ");
        String[] digitos = linha2.split(" ");
        for (int i = 0; i < meses.length; i++){
            if (meses[i].equals(resposta)){
                System.out.println(digitos[i]);
                break;
            }
        }
    }
}