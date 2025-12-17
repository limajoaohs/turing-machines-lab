import java.util.Scanner;

public class ContadorDeOcorrencias {
    public int count(int[] array,int elemento, int leftIndex,int rightIndex){
        if (array != null && array.length != 0 && leftIndex >= 0 && rightIndex < array.length){
            int primeiroIndice = encontrarPrimeiroIndice(array,elemento,leftIndex,rightIndex);
            if (primeiroIndice == -1){
                return 0;
            }
            int ultimoIndice = encontrarUltimoIndice(array,elemento,leftIndex,rightIndex);
            return ultimoIndice - primeiroIndice +1;
        }
        return 0;
    }
    private int encontrarPrimeiroIndice(int[] array,int elemento,int leftIndex,int rightIndex){
        int retorna  = -1;
        if (leftIndex <= rightIndex){
            int meio = leftIndex + (rightIndex - leftIndex) / 2;
            if (((meio == leftIndex) || array[meio - 1]<elemento) && array[meio]==elemento){
                retorna = meio;
            }
            else if(elemento > array[meio]){
                retorna = encontrarPrimeiroIndice(array, elemento, meio + 1, rightIndex);
            }
            else{
                retorna = encontrarPrimeiroIndice(array, elemento, leftIndex, meio - 1);
            }
        }
        return retorna;
    }
    private int encontrarUltimoIndice(int[] array,int elemento,int leftIndex,int rightIndex){
        int retorna = -1;
        if (leftIndex <= rightIndex){
            int  meio = leftIndex + (rightIndex - leftIndex) / 2;
            if ((meio == rightIndex || array[meio+1] > elemento) && array[meio] == elemento){
                retorna = meio;
            } else if(elemento <array[meio]){
                retorna = encontrarUltimoIndice(array,elemento,leftIndex,meio -1);
            }else{
                retorna = encontrarUltimoIndice(array,elemento,meio+1,rightIndex);
            }
        }
        return retorna;
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        ContadorDeOcorrencias contador = new ContadorDeOcorrencias();
        int[] array = {1,2,3,4,4,4,4,4,5,6,7};
        String input = scanner.next();
        int elemento = Integer.parseInt(input);
        int valor = contador.count(array,elemento,0,5);
        System.out.println(valor);
    }
}

