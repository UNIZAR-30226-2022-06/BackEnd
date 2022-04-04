package backend;

import java.util.List;


import backend.clasesDB.Documento;
import backend.clasesDB.Usuario;
import okhttp3.RequestBody;
import okhttp3.ResponseBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.DELETE;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.PUT;
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

    @DELETE("deleteUsuario/{nomUsuario}/")
    Call<ResponseBody> deleteUser(@Path("nomUsuario") String nomUsuario);

    @GET("Usuarios/")
    Call<List<Usuario>> userList();

    @GET("Documentos/{nomUsuario}")
    Call<Documento> getDocumento(@Path("idDoc") String idDoc);

    @POST("createDocumento/")
    Call<Documento> createDocumento(@Body Documento doc);

    @PUT("updateDocumento/{idDocDestino}/")
    Call<Documento> updateDocumento(@Path("idDoc") Integer idDocDestino, @Body RequestBody body);

    @GET("Documentos/")
    Call<List<Documento>> documentoList(@Query("page") Integer page);

}
