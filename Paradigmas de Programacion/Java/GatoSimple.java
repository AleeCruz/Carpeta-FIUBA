public class GatoSimple {

    String color,raza,sexo;
    int edad;
    double peso;


    GatoSimple(String s){
        this.sexo = s;
    }

    String getSexo(){
        return this.sexo;
    }

    void maullar(){
        System.out.println("Miiiiaauuu");
    }

    void ronronear(){
        System.out.println("Mrrrrrrr");
    }


    void come(String comida){
        if (comida.equals("pescado")){
            System.out.println("Gracias por la comida");
        }else{
            System.out.println("Lo siento, yo solo como pescado");
        }
    }

    void peleaCon(GatoSimple contrincante){
        if(this.sexo.equals("hembra")){
            System.out.println("No me gusta pelear");
        }else{
            if (contrincante.getSexo().equals("hembra")){
                System.out.println("No me gusta pelear con hembras");
            }else{
                System.out.println("Vamos a pelear mi brother");
            }
        }




    }




}
