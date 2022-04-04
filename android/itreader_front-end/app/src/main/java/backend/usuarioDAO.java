package backend;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;



public class usuarioDAO {
	
	/* A�ADE UN NUEVO USUARIO A LA BASE DE DATOS */
	public static void create(Connection connection, usuarioVO user) throws InternalErrorException{
		PreparedStatement preparedStatement = null;
		try {	
			// Abrimos la conexi�n e inicializamos los par�metros 
			preparedStatement = connection.prepareStatement("INSERT INTO public.usuarios("
					+ "nombre, nomusuario, password, correo, edad, telefono, valoracion)"
					+ "	VALUES (?, ?, ?, ?, ?, ?, ?);");
			preparedStatement.setString(1, user.getNombre());
			preparedStatement.setString(2, user.getNombreUsuario());
			preparedStatement.setString(3, user.getPassword());
			preparedStatement.setString(4, user.getEmail());
			preparedStatement.setInt(5, user.getEdad());
			preparedStatement.setInt(6, user.getTelefono());
			preparedStatement.setInt(7, user.getValoracion());
			/* Execute query. */
		    int insertedRows = preparedStatement.executeUpdate();
		    if (insertedRows == 0) {
		    	throw new SQLException("Can not add row to table 'usuario'");
		    }
		    if (insertedRows > 1) {
		    	throw new SQLException("Duplicate row in table 'usuario'");
		    }
		    preparedStatement.close();
		} catch (SQLException e) {
			System.out.println("Error.." + e);		        	
		    throw new InternalErrorException(e);
		} finally {
		    try {
		    	preparedStatement.close();
		    } catch (SQLException e) {
		    	throw new InternalErrorException(e);
		    }	        
		}	
	}
		
	/* COMPRUEBA SI EXISTE UN USUARIO CON UN NOMBRE DE USUARIO */
	public static boolean exist(Connection connection, String nombreUsuario) throws InternalErrorException {
		boolean result;
		PreparedStatement preparedStatement = null;
		ResultSet resultSet = null;
		try {
			// Abrimos la conexi�n e inicializamos los par�metros 
			preparedStatement = connection.prepareStatement("SELECT count(*) FROM usuarios WHERE nomusuario = ?");
			if(preparedStatement == null) System.out.println("stat null");
					else System.out.println("stat no null");
			preparedStatement.setString(1, nombreUsuario);
			// Ejecutamos la consulta 
			resultSet = preparedStatement.executeQuery();
			resultSet.next();
			int n = resultSet.getInt(1);
			// Leemos resultados 
			if(n == 1) {
				result = true;
			} else { 
				result = false;  
			} 
			return result;
		} catch (SQLException e) {
		    e.printStackTrace();
		    throw new InternalErrorException(e);
		} finally {
			try {
		    	preparedStatement.close();
		    } catch (SQLException e) {
		    	throw new InternalErrorException(e);
		    }
		}
	}
	
	/* DEVUELVE LOS DATOS DEL USUARIO IDENTIFICADO CON UN NOMBRE DE USUARIO */
	public static usuarioVO find(Connection connection, String nombreUsuario) throws InternalErrorException {
		PreparedStatement preparedStatement = null;
		ResultSet resultSet = null;
		usuarioVO user = null;
		try {
			// Abrimos la conexi�n e inicializamos los par�metros  
			preparedStatement = connection.prepareStatement("Select * from usuarios where nomUsuario = ?");
			preparedStatement.setString(1, nombreUsuario);
			resultSet = preparedStatement.executeQuery();
			resultSet.next();
			user = new usuarioVO(resultSet.getString("nombre"), resultSet.getString("nomUsuario"),
					resultSet.getString("password"),resultSet.getString("correo"),resultSet.getInt("edad"),
					resultSet.getInt("telefono"), resultSet.getInt("valoracion"));
			return user;
			} catch (SQLException e) {
				e.printStackTrace();
		        throw new InternalErrorException(e);    
		    } finally {
		        try {
		        	resultSet.close();
		        	preparedStatement.close();
		       	} catch (SQLException e) {
		        	throw new InternalErrorException(e);
		       	}
		    }
		}
}
