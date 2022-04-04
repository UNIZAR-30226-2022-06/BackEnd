package com.arqsoft.univibes

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class Reset : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.resetpassword_activity)

        restablecer()
    }

    private fun restablecer(){

        val email = findViewById<EditText>(R.id.mailEditText)
        val resetButton: Button = findViewById(R.id.reseteoButton)


        var t = Toast.makeText(this, R.string.Resetear, Toast.LENGTH_SHORT)

        resetButton.setOnClickListener{
            if(email.text.isEmpty()){
                t.cancel()
                t = Toast.makeText(this, R.string.Resetear, Toast.LENGTH_SHORT)
                t.show()
            }else{
                t.cancel()
                Toast.makeText(this, concatenaStrings(email.text.toString()) , Toast.LENGTH_LONG).show()
                goLogin()
            }
        }

    }

    private fun goLogin(){
        val pantallaLogin = Intent(this, SignIn::class.java)
        startActivity(pantallaLogin)
    }

    private fun concatenaStrings(correo: String):String {
        val builder = StringBuilder()
        builder.append(getString(R.string.MensajeEnviado)) /////////////////////IMPORTANTE
            .append(" ")
            .append(correo)
        return builder.toString()
    }
}