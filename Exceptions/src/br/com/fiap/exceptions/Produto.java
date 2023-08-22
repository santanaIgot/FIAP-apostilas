package br.com.fiap.exceptions;

public class Produto {
	private String nome;
	
	private double preco;

	public Produto(String nome, double preco) {
		this.nome = nome;
		this.preco = preco;
	}
	
	//Retornar o valor do imposto do produto
	public double calcularImposto(double imposto) {
		//Se o imposto for menor do que 0, lançar uma RuntimeException
		if (imposto< 0) {
			throw new RuntimeException("O imposto deve ser maior que 0 ");
			
		}
		return preco * (imposto / 100);
	}
	
	//Retornar o valor total dos produtos de acordo com a qtd
	public double calcularValorTotal(int quantidade) throws Exception {
		//Se a quatidade for menor ou igual a zero, lançar uma Exception = lançar erroo
		if ( quantidade <= 0) {
			throw new Exception("Quantidade não pode ser menor q zero");
		}
		return preco * quantidade;
	}
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public double getPreco() {
		return preco;
	}

	public void setPreco(double preco) {
		this.preco = preco;
	}
}
