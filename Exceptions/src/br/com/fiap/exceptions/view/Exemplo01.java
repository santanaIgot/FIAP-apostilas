package br.com.fiap.exceptions.view;

import java.util.Scanner;

import br.com.fiap.exceptions.Produto;



public class Exemplo01 {

	public static void main(String[] args) {
		
		Scanner entrada = new Scanner(System.in);
		Produto p = new Produto(null, 0);
		
		// TODO Auto-generated method stub
		try { 
			//Ler a idade do usuário com JOptionPane
			System.out.println("Digite a idade");
			int idade = entrada.nextInt();
			//Exibir a idade
			System.out.println(idade);
		} catch(NumberFormatException e) {
			System.out.println("Número inválido");
			System.out.println(e.getMessage());
		} catch (Exception e) {
			System.out.println("Index inválido");
		} finally {
			System.out.println("Bloco que sempre executa");
		}
		System.out.println("Finalizando o programa");
		
		
		

		
		
	}//main

}
