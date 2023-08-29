package br.com.fiap.exercicio.view;

import br.com.fiap.exercicio.model.ContaCorrente;

public class TesteContaCorrente {
	public static void main(String[] args) {
		  // Instanciar uma ContaCorrente com valor e limite
        ContaCorrente conta = new ContaCorrente(1000.0, 500.0);
        
        // Setar o limite
        try {
            conta.setLimite(700.0);
            System.out.println("Limite definido com sucesso: " + conta.getLimite());
        } catch (Exception e) {
            System.out.println("Erro ao definir o limite: " + e.getMessage());
        }
        
        // Depositar na conta
        try {
            conta.depositar(300.0);
            System.out.println("Depósito realizado com sucesso. Saldo atual: " + conta.getSaldo());
        } catch (Exception e) {
            System.out.println("Erro ao depositar: " + e.getMessage());
        }
        
        // Sacar da conta
        try {
            conta.sacar(200.0);
            System.out.println("Saque realizado com sucesso. Saldo atual: " + conta.getSaldo());
        } catch (Exception e) {
            System.out.println("Erro ao sacar: " + e.getMessage());
        }
	}
}
