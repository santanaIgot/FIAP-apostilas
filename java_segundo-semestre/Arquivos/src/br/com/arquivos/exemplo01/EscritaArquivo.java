package br.com.arquivos.exemplo01;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class EscritaArquivo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
		//filewriter é uma classe que lê o arquivo
		FileWriter outputStream = new FileWriter("exemplo.txt");
		PrintWriter arquivoDeSaida = new PrintWriter(outputStream);
		
		arquivoDeSaida.print("teste");
		arquivoDeSaida.print("conteudo do arquivo");
		
//		arquivoDeSaida.close();
//		outputStream.close();
		
		
		}catch(IOException e) {
			e.printStackTrace();
		}
	}

}
