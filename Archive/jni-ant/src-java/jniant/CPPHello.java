package jniant;

public class CPPHello {
	public static void main(String[] args) {
		System.loadLibrary("libCPPHello");
		new CPPHello().printHello();
	}

	private native void printHello();
}