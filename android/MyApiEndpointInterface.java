package com.softkare.itreader.backend;

import java.io.File;
import java.util.List;


import com.softkare.itreader.backend.Usuario;
import com.softkare.itreader.backend.Documento;
import com.softkare.itreader.backend.Libro;

import okhttp3.MultipartBody;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
import retrofit2.http.Part;
import retrofit2.http.Path;
import retrofit2.http.Query;


public interface MyApiEndpointInterface {

    public static final String BASE_URL = "https://db-itreader-unizar.herokuapp.com/itreaderApp/";

    // Request method and URL specified in the annotation

    @GET("Usuarios/{nomUsuario}")
    Call<Usuario> getUser(@Path("nomUsuario") String nomUsuario);

    @POST("createUsuario/")
    Call<Usuario> createUser(@Body Usuario user);

    //@PUT("update/{userId}/")
    //Call<Usuario> updateUser(@Path("userId") int userId, @Body Usuario user);
    //@Multipart
    @PUT("updateUsuario/{nomUsuario}/")
    Call<Usuario> updateUser(@Path("nomUsuario") String nomUsuarioDestino,
                             @Body RequestBody body/*,
                             @Body RequestBody nomUsuarios,
                             @Body RequestBody password,
                             @Body RequestBody correo,
                             @Body RequestBody esAdmin*/
                            );

    @PUT("addDocsUsuario/{nomUsuario}/")
    Call<Usuario> addDocsUser(@Path("nomUsuario") String nomUsuarioDestino, @Body RequestBody body);

    @PUT("deleteDocUsuario/{nomUsuario}/")
    Call<Usuario> deleteDocUser(@Path("nomUsuario") String nomUsuarioDestino, @Query("nomLibro") String nomLibro);

    @DELETE("deleteUsuario/{nomUsuario}/")
    Call<ResponseBody> deleteUser(@Path("nomUsuario") String nomUsuario);

    @GET("Usuarios/")
    Call<List<Usuario>> userList();

    @GET("Documentos/{nomUsuario}")
    Call<Documento> getDocumento(@Path("idDoc") String idDoc);

    @POST("createDocumento/")
    Call<Documento> createDocumento(@Body Documento doc);

    @POST("createLibro/")
    Call<Libro> createLibro(@Body Libro libro);

    @PUT("updateDocumento/{idDocDestino}/")
    Call<Documento> updateDocumento(@Path("idDoc") Integer idDocDestino, @Body RequestBody body);

    @GET("Documentos/")
    Call<List<Documento>> documentoList(/*@Query("page") Integer page*/);

    @GET("Libros/")
    Call<List<Libro>> libroList();

    @GET("UsuariosCorreo/{correo}")
    Call<Usuario> checkUser(@Path("correo")String correo);

    @GET("enviarCorreo/{correo}")
    Call<Usuario> enviarCorreo(@Path("correo")String correo);
     
    @FormUrlEncoded
    @POST("subirLibro/")
    Call<ResponseBody> subirLibro(@Field("usuario") String usuario, @Field("cover") File cover);
    
    @POST("subirLibro2/{filename}/")
    Call<ResponseBody> subirLibro2(@Path("filename") String filename, @Query("usuario") String usuario, @Part MultipartBody.Part file);
    //Call<ResponseBody> subirLibro(@Part("description") RequestBody description, @Part MultipartBody.Part file);

    @GET("leerLibro/{nombre}/{pagina}")
    Call<ResponseBody> leerLibro(@Path("nombre") String nombre, @Path("pagina") Integer pagina);

    @GET("leerLibro/{usuario}/{nombre}/{pagina}")
    Call<ResponseBody> leerLibroUsuario(@Path("usuario") String usuario, @Path("nombre") String nombre, @Path("pagina") Integer pagina);


}
