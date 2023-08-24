package br.com.fiap.exceptions.view;

import java.util.Scanner;

import br.com.fiap.exceptions.Produto;
public class Exemplo02 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		//instanciar produto
		Produto p = new Produto("Carlos", 10);
		
		
		try {
			//ler imposto
			System.out.println("Digite o valor do imposto");
			double valorImposto = entrada.nextDouble();
			
			//Calcular e exibir imposto
			double valor = p.calcularImposto(valorImposto);
			System.out.println(valor);
		}catch (NumberFormatException e) {
			System.err.println("Digite o valor certo !!!");
			System.out.println(e.getMessage());
		}catch(RuntimeException e) {
			System.err.println(e.getMessage());
			//throw new RuntimeException("O imposto deve ser maior que 0 "); dando e.getMessage() ele vai retornar esta msg
		}finally {
			
		}

		
		
		//calcula\r valor total
		

		try {
			System.out.println("Digite a qtd:");
			int quantidade = entrada.nextInt();
			
			int valor = (int) p.calcularImposto(quantidade);
			System.out.println(valor);
		}catch (NumberFormatException e) {
			System.err.println("A qtd deve ser maior q 0");
			System.err.println(e.getMessage());
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
		
		
		
	}
	
// se o imposto for maior q 0 vai dar dar uma exception
// se pssar uma string vai dar exception
	
	
}
