package com.lucasaraujo.FestaFimDeAno.view;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.lucasaraujo.FestaFimDeAno.R;
import com.lucasaraujo.FestaFimDeAno.constant.FimDeAnoConstants;
import com.lucasaraujo.FestaFimDeAno.data.SecurityPreferences;

import java.text.SimpleDateFormat;
import java.util.Calendar;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private ViewHolder mViewHolder = new ViewHolder();
    private static SimpleDateFormat SIMPLE_DATE_FORMAT = new SimpleDateFormat("dd/MM/yyyy");
    private SecurityPreferences mSecurityPreferences;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        this.mViewHolder.textDaysLeft = findViewById(R.id.text_days_left);
        this.mViewHolder.textToday = findViewById(R.id.text_today);
        this.mViewHolder.buttonConfirm = findViewById(R.id.button_confirm);
        this.mViewHolder.buttonConfirm.setOnClickListener(this);
        this.mViewHolder.textToday.setText(SIMPLE_DATE_FORMAT.format(Calendar.getInstance().getTime()));
        String daysLeft = String.format("%s %s", String.valueOf(this.getDaysLeft()), getString(R.string.dias));
        this.mViewHolder.textDaysLeft.setText(daysLeft);
        this.mSecurityPreferences = new SecurityPreferences(this);

    }

    @Override
    public void onClick(View v) {
        if (v.getId() == R.id.button_confirm) {
            String presence = this.mSecurityPreferences.getStoredString(FimDeAnoConstants.PRESENCE_KEY);
            Intent intent = new Intent(this, DetailsActivity.class);
            intent.putExtra(FimDeAnoConstants.PRESENCE_KEY, presence);
            startActivity(intent);
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        this.verifyPresence();
    }

    private void verifyPresence(){
        String presence = this.mSecurityPreferences.getStoredString(FimDeAnoConstants.PRESENCE_KEY);
        if (presence.equals("")){
            this.mViewHolder.buttonConfirm.setText(getString(R.string.nao_confirmado));
        }
        else if (presence.equals(FimDeAnoConstants.CONFIRMATION_YES)){
            this.mViewHolder.buttonConfirm.setText(getString(R.string.sim));
        }
        else{
            this.mViewHolder.buttonConfirm.setText(getString(R.string.nao));
        }
    }


    private int getDaysLeft() {
        Calendar CalendarToday = Calendar.getInstance();
        int today = CalendarToday.get(Calendar.DAY_OF_YEAR);
        Calendar calendarLastDay = Calendar.getInstance();
        int dayMax = calendarLastDay.getActualMaximum(Calendar.DAY_OF_YEAR);
        return dayMax - today;
    }

    private static class ViewHolder {
        TextView textToday;
        TextView textDaysLeft;
        Button buttonConfirm;
    }
}
