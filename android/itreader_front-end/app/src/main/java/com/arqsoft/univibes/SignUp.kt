package com.arqsoft.univibes

import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import backend.MyApiEndpointInterface
import backend.clasesDB.Usuario
import backend.usuarioVO
import okhttp3.MediaType
import okhttp3.RequestBody
import org.json.JSONArray
import org.json.JSONException
import org.json.JSONObject
import retrofit2.*
import retrofit2.converter.gson.GsonConverterFactory


class SignUp : AppCompatActivity(){
    override fun onCreate(savedInstanceState: Bundle?) {
        setTheme(R.style.AppTheme)
        super.onCreate(savedInstanceState)
        setContentView(R.layout.signup_activity)
        registro()
    }

    private fun registro(){

        val username = findViewById<EditText>(R.id.usernameEditText)
        val password = findViewById<EditText>(R.id.passwordEditText)
        val name = findViewById<EditText>(R.id.nameEditText)
        val email = findViewById<EditText>(R.id.mailEditText)

        val signUp: Button = findViewById(R.id.SignUpButton)

        var t = Toast.makeText(this, R.string.ErrorRegistro, Toast.LENGTH_SHORT)

        signUp.setOnClickListener{
            if(email.text.isEmpty() || username.text.isEmpty() || password.text.isEmpty() || name.text.isEmpty()   ){
                t.cancel()
                t = Toast.makeText(this, R.string.ErrorRegistro, Toast.LENGTH_SHORT)
                t.show()
            }else{
                t.cancel()
                //Toast.makeText(this, concatenaStrings(username.text.toString()) , Toast.LENGTH_SHORT).show()
                //goLogin(username.text.toString())
                val c : Context = this
                //val user = Usuario(name.text.toString(),username.text.toString(),password.text.toString(),email.text.toString(),23,123456,5.0, null)
                val user = Usuario(
                    null,
                    "c",
                    null,
                    null,
                    null
                )
                println("username "+username.text.toString())

                // Trailing slash is needed
                val retrofit = Retrofit.Builder()
                    .baseUrl(MyApiEndpointInterface.BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .build()
                var u : Usuario? = null
                val service = retrofit.create(MyApiEndpointInterface::class.java)
                val user2 = Usuario(
                    name.text.toString(),
                    username.text.toString(),
                    password.text.toString(),
                    email.text.toString(),
                    true
                )
                val user3 = Usuario(null,null,null,null,null)

                val j = JSONObject()
                val j2 = JSONObject()
                //try {
                    j.put("nombre", "er2")
                    j.put("correo", "nuevocorreo2")
                /*} catch (e: JSONException) {
                    // TODO Auto-generated catch block
                    e.printStackTrace()
                */


                val jsonArray = JSONArray()
                jsonArray.put(j)

                val J = JSONObject()
                J.put("amigos", jsonArray)

                val MEDIA_TYPE_JSON : MediaType? = MediaType.parse("application/json; charset=utf-8");
                println("json: "+j.toString())
                //"{\"amigos\": [{\"nomUsuario\": \"c\"}]}"
                val body : RequestBody = RequestBody.create(MEDIA_TYPE_JSON,"{\"nombre\": \"er\",\"correo2\": \"nuevocorreo2\"}");
                service.updateUser("r",body,/*null,null,null,null*/).enqueue(object : Callback<Usuario>{
                    override fun onResponse(call: Call<Usuario>, response: Response<Usuario>) {
                        println("USUARIO REGISTRADO")
                        if (response.body() != null) {
                            u = response.body()!!
                            println("usuario "+ u?.nombre+" id:"+u?.id)
                        }
                        //Toast.makeText(this@SignUp, "error", Toast.LENGTH_SHORT)

                    }

                    override fun onFailure(call: Call<Usuario>, t: Throwable) {
                        println("FALLO REGISTRO")
                    }
                })
                goLogin(username.text.toString())

            }
        }
    }

    fun onResponse(call: Call<usuarioVO>, response: Response<usuarioVO>) {
        if (response.isSuccessful()) {
            val user: usuarioVO? = response.body()
            if (user != null) {
                println("usuario: "+user.nombreUsuario)
            }
        } else {
            println(response.errorBody())
        }
    }

    private fun goLogin(username: String){
        val pantallaLogin = Intent(this, SignIn::class.java)
        startActivity(pantallaLogin)
    }

    private fun concatenaStrings(username: String):String {
        val builder = StringBuilder()
        builder.append(username)
            .append(" ")
            .append(getString(R.string.RegistroCreado))
        return builder.toString()
    }
}