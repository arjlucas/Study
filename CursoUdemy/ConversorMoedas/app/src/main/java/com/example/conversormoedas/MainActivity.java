package com.example.conversormoedas;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.w3c.dom.Text;

// 4 - Para o funcionamento dos eventos de clique, é ideal que a classe MainActivity possa implementar
// os métodos da View.onClickListener, se comportando como a própria Classe.
public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    //2 - Um objeto da classe é instanciado, para obter os métodos que a classe provê
    private ViewHolder mViewHolder = new ViewHolder();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //3 - Os métodos para o objeto mViewHolder da classe ViewHolder são chamados passando como
        //parâmetro os IDs criados e aplicados lá na interface activity_main.xml - Esses métoos
        //vão mapear os objetos pelo ID, permitindo uma referência posterior.
        this.mViewHolder.editValue = findViewById(R.id.edit_Value);
        this.mViewHolder.textDolar = findViewById(R.id.text_Dolar);
        this.mViewHolder.textEuro = findViewById(R.id.text_Euro);
        this.mViewHolder.buttonCalculate = findViewById(R.id.button_Calculate);
        //6 - Agora, pode-se chamar o método da View.onClickListener como se fosse da própria
        // MainActivity já que ela implementa seus métodos, assim, referenciando apenas como this.
        // Essa flexibilização permite a adição com apenas uma linha de código para cada elemento
        // que se queira adicionar uma ação associada ao evento de click.
        this.mViewHolder.buttonCalculate.setOnClickListener(this);
        this.clearValues();

    }

    // 5- Com a MainActivity se comportando como a View.onClickListener, é necessário implementar um
    // de seus métodos, neste caso o onClick.
    @Override
    public void onClick(View v) {
        //7 - Aqui é inserido o código de ação referente a ação para cada elemento desejado. Como
        //em tese seriam vários, é ideal organizar o código com a inserção de estruturas
        //condicionais, permitindo um direcionamento de ação ao código específico.
        if (v.getId() == R.id.button_Calculate) {
            String value = this.mViewHolder.editValue.getText().toString();
            if ("".equals(value)) {
                Toast.makeText(this, this.getString(R.string.informe_valor), Toast.LENGTH_LONG).show();
            }
            else{
                Double real = Double.valueOf(value);
                this.mViewHolder.textDolar.setText(String.format("%.2f", (real/4)));
                this.mViewHolder.textEuro.setText(String.format("%.2f", (real/5)));
            }
        }
    }

    private void clearValues() {
        this.mViewHolder.textDolar.setText("");
        this.mViewHolder.textEuro.setText("");
    }

    //1 - É criada a classe ViewHolder, para permitir uma indexação dos findViewById e deixar
    //o código mais eficiente, eliminando a necessidade do rerun do método a procura do
    //item em questão. Todos os itens a serem alterados são declarados na classe.
    private static class ViewHolder {
        EditText editValue;
        TextView textDolar;
        TextView textEuro;
        Button buttonCalculate;
    }
}
