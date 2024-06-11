// Definición de una clase llamada MyThread que extiende la clase Thread
class MyThread extends Thread {
    // Método run que se sobrescribe para definir el comportamiento del hilo
    public void run() {
        // Imprime un mensaje en la consola indicando que el hilo está en ejecución
        System.out.println("Thread is running.");
    }
}

// Clase principal que contiene el método main, punto de entrada del programa
public class Main {
    // Método main que se ejecuta al iniciar el programa
    public static void main(String[] args) {
        // Crea una instancia de la clase MyThread
        MyThread thread = new MyThread();
        // Inicia el hilo, llamando internamente al método run
        thread.start();
    }
}
