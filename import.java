import java.awt.Color;
import java.awt.Frame;
import java.awt.TextField;

class Sample extends Frame{

    TextField t1,t2;
    Sample(){

        setLayout(null);

        t1=new TextField();
        t2=new TextField();

        t1.setBounds(100,100,100,30);
        t2.setBounds(230,100,100,30);

        add(t1);
        add(t2);

        setBackground(Color.ORANGE);
        setBounds(100,100,600,400);
        setVisible(true);

    }
    public static void main(String args[]){
        new Sample();
    }
}