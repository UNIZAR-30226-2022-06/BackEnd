package com.arqsoft.univibes

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AlertDialog
import backend.MyApiEndpointInterface
import backend.clasesDB.Documento
import backend.clasesDB.Usuario
import okhttp3.MediaType
import okhttp3.RequestBody
import org.json.JSONArray
import org.json.JSONObject
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class SignIn : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        Thread.sleep(1000)
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.signin_activity)
        setup()
    }

    private fun setup(){

        val username = findViewById<EditText>(R.id.usernameEditText)
        val password = findViewById<EditText>(R.id.passwordEditText)
        val signInButton: Button = findViewById(R.id.SignInButton)
        val resetButton: Button = findViewById(R.id.resetPasswordButton)
        val signUpForButton: Button = findViewById(R.id.SignupForButton)

        var t = Toast.makeText(this, R.string.loginEmpty, Toast.LENGTH_SHORT)

        signInButton.setOnClickListener{
            /*if(username.text.isEmpty() || password.text.isEmpty()){
                t.cancel()
                t = Toast.makeText(this, R.string.loginEmpty, Toast.LENGTH_SHORT)
                t.show()
                //showAlert()
            }else{
                t.cancel()
                showGeneral(username.text.toString(), password.text.toString())
            }*/

            val retrofit = Retrofit.Builder()
                .baseUrl(MyApiEndpointInterface.BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build()
            val service = retrofit.create(MyApiEndpointInterface::class.java)
            val MEDIA_TYPE_JSON : MediaType? = MediaType.parse("application/json; charset=utf-8");
            //"{\"amigos\": [{\"nomUsuario\": \"c\"}]}"

            val j = JSONObject()
            val j2 = JSONObject()
            j.put("nombre", "qwer")
            j2.put("nombre", "asdf")
            val jsonArray = JSONArray()
            jsonArray.put(j)
            jsonArray.put(j2)
            val J = JSONObject()
            J.put("docsAnyadidos", jsonArray)
            println("json: "+J.toString())
            val body : RequestBody = RequestBody.create(MEDIA_TYPE_JSON,"{\"correo\": \"corrrreo3\",\"password\": \"contraseña\"}");
            //service.updateUser("z",body).enqueue(object :
            service.documentoList(1).enqueue(object : Callback<List<Documento>> {
                override fun onResponse(call: Call<List<Documento>>, response: Response<List<Documento>>) {
                    println("USUARIO REGISTRADO")
                    if (response.isSuccessful()) {
                        println("SUCESS")
                        var u : List<Documento>? = response.body()
                        println("size "+u?.size)
                        for (us in u!!){
                            //println("usuario "+ us?.nombre+" id:"+us?.id)
                            println("usuario")
                        }
                    }
                    //Toast.makeText(this@SignUp, "error", Toast.LENGTH_SHORT)

                }

                override fun onFailure(call: Call<List<Documento>>, t: Throwable) {
                    println("FALLO REGISTRO")
                }
            })
        }

        resetButton.setOnClickListener{
            t.cancel()
            val pantallaResetPassword = Intent(this, Reset::class.java)
            startActivity(pantallaResetPassword)
        }

        signUpForButton.setOnClickListener{
            t.cancel()
            val pantallaSingUp = Intent(this, SignUp::class.java)
            startActivity(pantallaSingUp)
        }

    }

    private fun showAlert(){
        val builder = AlertDialog.Builder(this)
        builder.setTitle("Error")
        builder.setMessage(R.string.loginEmpty)
        builder.setPositiveButton("Aceptar",null)
        val dialog: AlertDialog = builder.create()
        dialog.show()
    }


    private fun showGeneral(username:String,password:String){
        val pantallaGeneral = Intent(this, General::class.java)
        pantallaGeneral.putExtra("user", username)
        pantallaGeneral.putExtra("password", password)
        startActivity(pantallaGeneral)
    }
}