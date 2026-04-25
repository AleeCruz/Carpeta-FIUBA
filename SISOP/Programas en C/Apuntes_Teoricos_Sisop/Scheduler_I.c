/**
 * Vamos a ver sobre los conceptos elementales de Scheduler
 * 
 * ¿Cuales son los conceptos mas importantes del Scheduler ?
 * 
 * ->Cambio de contexto 
 * ->Memoria Virtual
 * ->Trampoline
 * ->Trapframe
 * 
 */



 /**
  * Primero debemos repasar lo que vimos en las ultimas clases
  * Se vio en clases anteriores que que todo proceso tiene un contexto asociado 
  * 
  * El contexto informalmente se puede pensar como el estado completo del proceso en ejecucion 
  * conformado por:
  * 
  * ->Espacio de direccione de memoria
  * ->Registros del procesador
  * ->Estructuras del kernel
  * 
  * 
  * Cuando el SO interrumpe momentaneamente la ejecucion de un proceso  y restaura la ejecucion 
  * de uno suspendido se produce un cambio de contexto 
  * 
  * 
  * 
  * ¿Que cosas son la que inducen a uncambio de contexto de user-kernel o kernel-user?
  * 
  * ->System calls
  * ->I/O Interrupt 
  * ->Timer Interrupt
  * ->Exceptions
  * 
  * 
  * 
  * ¿Cuando se debe de ahce un cambio de contexto ?
  * ->Timer:Por timer uno puede indcir un cambio de contexto, ejemplo concreto 
  * si se llegara a hacer un read al kernel para la memoria, el kernel no se quedara esperando
  * hasta que la memoria termine de leer, realizara una correspondiente cambio de contexto.
  * ->I/O bloqueante
  * ->Proceso Terminado :Tambien es un cambio de contexto 
  * 
  * 
  * ¿Entonces los cambios de context tiene un paso intermedio ?
  * SI luego habalremos sobre eso pero basicamente es el scheduler
  * SU razon de ser es decidir quien va a ser el siguiente que se va aejecutar 
  * Vamos a ver distintos tipos de scheduler , y varias ideas similares y ejemplos que incluyen
  * el como se ejecutan dicho scheduler
  */

/**Que hace el scheduler ?
 * El scheduler elige el proceso siguiente 
 * 
 * ¿QUe es el cambio de memoria ?
 * Es ir y ejecutar el cambiar toda la memoria , basicamente manipalr las paginas
 * EL kernel es el que tiene el permiso para hcer eso 
 * 
 * ¿Quien es el que hace el cambio de contexto ?
 * Basicamente lo hace siempre el kernel , porque es el mas privilegiado
 */



 /**
  * Veremos un resumen de lo que es un cambio de contexto 
  * 
  * 1.-Comineza con una transicion de Kernel.space. Los procesos no pueden cmabiar desde user space
  * a) Esto puede ocurrir tantopor interrupciones, excepciones, como cuando el usuario
  * llama a la System call
  * b) En todos los casos se puede o no producir un cambio de contexto.
  * 
  * 
  * 2.- Si se decide que hay que realizar un cambio de contexto ,se invoca al SCHEDULER
  * 
  * 3.- El scheduler elije el siguiente proceso a ejecutar y llama al switch
  * 
  * 4.-Switch le saca una  foto al estado del kernel space y de user space y restaura el proceso
  * candidato(que queda en el kernel)
  * 
  * 5.-Regresa al USer space del nuevo proceso 
  * 
  * 
  * 
  * 
  * 
  * 
  * 
  * 
  */
























