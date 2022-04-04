package backend;

import java.sql.Connection;
import java.sql.SQLException;
import javax.sql.DataSource;



public class EventoFacade {
	
	private DataSource dataSource;

	public EventoFacade() throws InternalErrorException {  
		System.out.println ("He llegado a la creaci�n de la fachada correctamente...");
		this.dataSource = new SimpleDataSource();   
		System.out.println ("Parece que soy capaz de crear la fachada correctamente...");
	}
	
	/** Registra un evento en la BBDD **/
	public void registrarEvento(eventoVO eventoVO) throws InternalErrorException, NotLegalAccountException{
		eventoDAO eventoDAO = new eventoDAO();
		Connection connection =null;
		try {
			connection = this.dataSource.getConnection();
			if (connection == null) System.out.println("Conexi�n es: null");
			if (connection != null) System.out.println("Conexi�n es: not null "+ connection);
			eventoDAO.create(connection, eventoVO);	
		} catch (SQLException e) {
			System.out.println("Error.." + e);
			throw new InternalErrorException(e);
		} finally {
			try {
				if (connection !=null) {
					connection.close();
				}
			} catch (SQLException e) {
				throw new InternalErrorException(e);
			}
		}
	}

	/** Devuelve los datos de un evento en la BBDD identificado por id **/
	public eventoVO encontrarEvento(int id) throws InternalErrorException, NotLegalAccountException{
		eventoDAO eventoDAO = new eventoDAO();
		Connection connection =null;
		eventoVO result = null;
		try {
			connection = this.dataSource.getConnection();
			if (eventoDAO.existId(connection, id)) {
				result = eventoDAO.find(connection, id);
			} else {
				System.out.println("No existe usuario del sistema con ese ID");
				throw new NotLegalAccountException();				
			}
			return result;
		} catch (SQLException e) {
			System.out.println("Error.." + e);
			throw new InternalErrorException(e);
		} finally {
			try {
				if (connection !=null) {
					connection.close();
				}
			} catch (SQLException e) {
				throw new InternalErrorException(e);
			}
		}	
	}

}
