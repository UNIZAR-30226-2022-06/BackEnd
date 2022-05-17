package com.softkare.itreader.fragments

import android.Manifest
import android.app.Activity
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import android.widget.Toast
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.core.content.ContextCompat
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.softkare.itreader.R
import com.softkare.itreader.adapter.documentAdapter
import com.softkare.itreader.backend.Documento
import com.softkare.itreader.backend.MyApiEndpointInterface
import com.softkare.itreader.sharedPreferences
import okhttp3.MediaType
import okhttp3.MultipartBody
import okhttp3.RequestBody
import okhttp3.ResponseBody
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.io.File


class MyBooksFragment : Fragment() {
    lateinit var list : List<Documento>
    lateinit var mCtx : Context
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view = inflater.inflate(R.layout.fragment_my_books, container, false)
        val recyclerView : RecyclerView = view.findViewById(R.id.recyclerDocs)
        val buttonUpload : ImageButton = view.findViewById(R.id.btnUpload)

        recyclerView.layoutManager= LinearLayoutManager(context)
        getList(recyclerView)

        buttonUpload.setOnClickListener() {
            //TODO: Llamar a servicio --> createDocumento
            var permisoConcedido = true
            if(ContextCompat.checkSelfPermission(mCtx, Manifest.permission.READ_EXTERNAL_STORAGE)
                != PackageManager.PERMISSION_GRANTED){
                permisoConcedido = false
                val requestPermissionLauncher =
                    registerForActivityResult(
                        ActivityResultContracts.RequestPermission()
                    ) { isGranted: Boolean ->
                        if (isGranted) {
                            permisoConcedido = true
                        }
                    }
                requestPermissionLauncher.launch(
                    Manifest.permission.READ_EXTERNAL_STORAGE)
            }
            if(permisoConcedido){
                var chooseFileIntent = Intent(Intent.ACTION_OPEN_DOCUMENT)
                chooseFileIntent.addCategory(Intent.CATEGORY_OPENABLE);
                chooseFileIntent.setType("*/*")
                val mimeTypes = arrayOf<String>("application/pdf", "application/epub")
                chooseFileIntent = Intent.createChooser(chooseFileIntent, "Choose a file")

                var resultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
                    if (result.resultCode == Activity.RESULT_OK) {
                        // There are no request codes
                        val data: Intent? = result.data
                        val fileUri = data?.data
                        val filePath = fileUri?.path
                        val file = File(filePath)

                        uploadFile(file,fileUri)
                    }
                }

                resultLauncher.launch(chooseFileIntent)


            }else{
                val t = Toast.makeText(activity, "Sin permisos necesarios", Toast.LENGTH_SHORT)
                t.show()
            }
        }

        return view
    }


    private fun uploadFile(file: File, fileUri: Uri?){
        val retrofit = Retrofit.Builder()
            .baseUrl(MyApiEndpointInterface.BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
        val service = retrofit.create(MyApiEndpointInterface::class.java)
        // SE DEBE LLAMAR AL SERVICIO DE LOS DOCUMENTOS SUBIDOS POR EL USUARIO
        val requestFile = RequestBody.create(
            MediaType.parse(mCtx.contentResolver.getType(fileUri!!)),
            file
        )

        val body = MultipartBody.Part.createFormData("file", file.name, requestFile)

        service.subirLibro(sharedPreferences.prefs.getUsername(),body).enqueue(object : Callback<ResponseBody> {
            override fun onResponse(call: Call<ResponseBody>, response: Response<ResponseBody>) {
                if(response.body() != null){
                    println("LIBRO SUBIDO")
                }else{
                    showAlert()
                }
            }

            override fun onFailure(call: Call<ResponseBody>, t: Throwable) {
                println("ERROR AL SUBIR LIBRO")
            }

        })
    }
    
    private fun getList(recyclerView: RecyclerView) {
        val retrofit = Retrofit.Builder()
            .baseUrl(MyApiEndpointInterface.BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
        val service = retrofit.create(MyApiEndpointInterface::class.java)
        // SE DEBE LLAMAR AL SERVICIO DE LOS DOCUMENTOS SUBIDOS POR EL USUARIO
        service.documentoList().enqueue(object : Callback<List<Documento>> {
            override fun onResponse(call: Call<List<Documento>>, response: Response<List<Documento>>) {
                if(response.body() != null){
                    list = response.body()!!
                    recyclerView.adapter = documentAdapter(list)
                }else{
                    showAlert()
                }
            }

            override fun onFailure(call: Call<List<Documento>>, t: Throwable) {
                println("ERROR AL RECIBIR LOS DOCUMENTOS DEL USUARIO")
            }

        })
    }

    private fun showAlert(){
        val builder = AlertDialog.Builder(mCtx)
        builder.setTitle("Error")
        builder.setMessage(getString(R.string.no_books))
        builder.setPositiveButton("Ok",null)
        val dialog: AlertDialog = builder.create()
        dialog.show()
    }
}