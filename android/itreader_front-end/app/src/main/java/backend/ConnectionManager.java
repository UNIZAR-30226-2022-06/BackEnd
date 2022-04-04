package backend;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;

import retrofit2.Call;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;

public class ConnectionManager
{
    // Credenciales de la Base de Datos
    private static final String HOST = "ec2-54-216-17-9.eu-west-1.compute.amazonaws.com";
    private static final String DATABASE = "dbj8n8nq07300c";
    private static final String USER = "jfugjnegtzvfbn";
    private static final String PASS = "f2b7e008af4ce1e53dc463f922969ca5f9f685c10b00c06cea8fead273491b9b";
    private static final String PATH = DATABASE+"?user="+USER+"&password="+PASS;

    // JDBC nombred el driver y URL de BD
    private static final String JDBC_DRIVER = "org.postgresql.Driver";
    private static final String DB_URL = "jdbc:postgresql://"+HOST+":5432/"+DATABASE+"?sslmode=require";

    public static final String BASE_URL = "https://db-test-unizar-1234.herokuapp.com/univibesApp/";


    // Devuelve una nueva conexion.
    public final static Connection getConnection() throws SQLException {

        Connection conn = null;
        try{
            //STEP 1: Register JDBC driver
            Class.forName(JDBC_DRIVER);
            //STEP 2: Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL,USER,PASS);
            //conn = DriverManager.getConnection(DB_URL);
            if (conn != null) {
                System.out.println("Tengo conexi�n :)");
            }
            return conn;
        } catch (Exception e) {
            e.printStackTrace();
            System.out.println("FALLLO!");
            return null;
        }

    }

    // Libera la conexion, devolviendola al pool
    public final static void releaseConnection(Connection conn) throws SQLException {
        conn.close();
    }
}
