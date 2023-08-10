package br.com.collections.viw;

import java.util.ArrayList;
import java.util.Scanner;

public class ExemploLista {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		//	list se comporta como vetor
		ArrayList<String> lista = new ArrayList();
		
//		para adiconar
		lista.add("Maçã");
		lista.add("uva");
		lista.add("banana");
		lista.add("abacaxi");
		
		System.out.println(lista.get(0));
		
//		exibir a qtd de elementos na lista 
		System.out.println("A qtd de frutas é:"+lista.size());
		
//		System.out.println(lista);
		
//		verifica se tem maca na lista
		if(lista.contains("Maçã")) {
			System.out.println("A lista tem maca");
		}
//		verifica se a lista esta vazia
		if(lista.isEmpty()) {
			System.out.println("A lista esta vazia");
		}
		
//		para remover
//		lista.clear()
		
		for(String item : lista) {
			System.out.println(item);
		}
	}

}
