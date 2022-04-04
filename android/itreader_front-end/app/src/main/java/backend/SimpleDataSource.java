package backend;
import java.io.PrintWriter;
import java.sql.SQLException;
import java.sql.SQLFeatureNotSupportedException;
import java.util.logging.Logger;
import java.sql.Connection;
import javax.sql.DataSource;

public class SimpleDataSource implements DataSource{

public Connection getConnection() throws SQLException {
	System.out.println("A ver si consigo una conexión:    ");
    return ConnectionManager.getConnection();
}

public Connection getConnection(String username, String password)
    throws SQLException {

    throw new UnsupportedOperationException("Not implemented");

}

public PrintWriter getLogWriter() throws SQLException {
    throw new UnsupportedOperationException("Not implemented");
}

public void setLogWriter(PrintWriter out) throws SQLException {
    throw new UnsupportedOperationException("Not implemented");
}

public void setLoginTimeout(int seconds) throws SQLException {
    throw new UnsupportedOperationException("Not implemented");
}

public int getLoginTimeout() throws SQLException {
    throw new UnsupportedOperationException("Not implemented");
}

public boolean isWrapperFor(Class<?> iface) throws SQLException {
    throw new UnsupportedOperationException("Not implemented");
}

public <T> T unwrap(Class<T> iface) throws SQLException	{
    throw new UnsupportedOperationException("Not implemented");
}

@Override
public Logger getParentLogger() throws SQLFeatureNotSupportedException {
	// TODO Auto-generated method stub
	return null;
}

/* Test code. Uncomment for testing. */
public static void main (String[] args) {

    try {

        /* Trying to get a connection. */
        System.out.println("Trying to get a connection");
        DataSource dataSource = new SimpleDataSource();
        Connection connection = dataSource.getConnection();

        /* Close connection. */
        connection.close();

        /* Test OK. */
        System.out.println("Test OK");

    } catch (Exception e) {
        e.printStackTrace();
        System.out.println("Test FAIL");
    }

}
}