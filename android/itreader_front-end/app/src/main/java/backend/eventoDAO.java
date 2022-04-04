package backend;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


public class eventoDAO {
	
	/* A�ADE UN NUEVO EVENTO A LA BASE DE DATOS */
	public void create(Connection connection, eventoVO evento) throws InternalErrorException{
		PreparedStatement preparedStatement = null;
		try {	
			// Abrimos la conexi�n e inicializamos los par�metros 
			preparedStatement = connection.prepareStatement("INSERT INTO public.eventos("
					+ "nombre, descripcion, nomusuario, fecha, tipoacceso, aforo, categoria)"
					+ "	VALUES (?, ?, ?, ?, ?, ?, ?);");
			preparedStatement.setString(1, evento.getNombre());
			preparedStatement.setString(2, evento.getDescripcion());
			preparedStatement.setString(3, evento.getNomUsuario());
			preparedStatement.setDate(4, evento.getFecha());
			preparedStatement.setString(5, evento.getTipoAcceso());
			preparedStatement.setInt(6, evento.getAforo());
			preparedStatement.setString(7, evento.getCategoria());
			/* Execute query. */
		    int insertedRows = preparedStatement.executeUpdate();
		    if (insertedRows == 0) {
		    	throw new SQLException("Can not add row to table 'eventos'");
		    }
		    if (insertedRows > 1) {
		    	throw new SQLException("Duplicate row in table 'eventos'");
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
		
	/* COMPRUEBA SI EXISTE UN EVENTO CON UN NOMBRE */
	public boolean existNombre(Connection connection, String nombre) throws InternalErrorException {
		boolean result;
		PreparedStatement preparedStatement = null;
		ResultSet resultSet = null;
		try {
			// Abrimos la conexi�n e inicializamos los par�metros 
			preparedStatement = connection.prepareStatement("Select count(*) cuenta From eventos Where nombre = ?");
			preparedStatement.setString(1, nombre);
			// Ejecutamos la consulta 
			resultSet = preparedStatement.executeQuery();
			resultSet.next();
			int n = resultSet.getInt(1);
			// Leemos resultados 
			if(n >= 1) {
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

	/* COMPRUEBA SI EXISTE UN EVENTO CON UN ID */
	public boolean existId(Connection connection, int id) throws InternalErrorException {
		boolean result;
		PreparedStatement preparedStatement = null;
		ResultSet resultSet = null;
		try {
			// Abrimos la conexi�n e inicializamos los par�metros 
			preparedStatement = connection.prepareStatement("Select count(*) cuenta From eventos Where eventoid = ?");
			preparedStatement.setInt(1, id);
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
	
	/* DEVUELVE LOS DATOS DEL EVENTO IDENTIFICADO CON UN ID */
	public eventoVO find(Connection connection, int id) throws InternalErrorException {
		PreparedStatement preparedStatement = null;
		ResultSet resultSet = null;
		eventoVO evento = null;
		try {
			// Abrimos la conexi�n e inicializamos los par�metros  
			preparedStatement = connection.prepareStatement("Select * from eventos where eventoid = ?");
			preparedStatement.setInt(1, id);
			resultSet = preparedStatement.executeQuery();
			resultSet.next();
			evento = new eventoVO(resultSet.getString("nombre"), resultSet.getString("descripcion"),
					resultSet.getString("nomUsuario"),resultSet.getDate("fecha"),resultSet.getString("tipoAcceso"),
					resultSet.getInt("aforo"), resultSet.getString("categoria"));
			return evento;
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
