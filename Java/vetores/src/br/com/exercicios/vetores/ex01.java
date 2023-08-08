package br.com.exercicios.vetores;

import java.util.Scanner;

public class ex01 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner entrada = new Scanner(System.in);

	
	String [] produtos = new String [5];
	int [] qtd = new int [5];
	double [] preco = new double [5];
	
	double desconto = 15 ;
		for(int i=0; i < produtos.length ; i++) {
			System.out.println("Digite o nome do produto:"+ (i+1));
			produtos[i] = entrada.next();
			
			System.out.println("Digite a qtd de produtos:"+ (i+1));
			qtd[i] = entrada.nextInt();
			
			System.out.println("Digite o preco dos produtos:"+ (i+1));
			preco[i] = entrada.nextDouble();
			
			
		}
		
		
		
	}

}
