package backend;

import java.sql.Connection;
import java.sql.SQLException;

import javax.sql.DataSource;



public class UsuarioFacade {
	
	private DataSource dataSource;

	public UsuarioFacade() throws InternalErrorException {  
		System.out.println ("He llegado a la creaci�n de la fachada correctamente...");
		this.dataSource = new SimpleDataSource();   
		System.out.println ("Parece que soy capaz de crear la fachada correctamente...");
	}
	
	/** Registra un usuario en la base de datos **/
	public void registrarUsuario(usuarioVO usuarioVO) throws InternalErrorException, NotLegalAccountException{
		usuarioDAO userDAO = new usuarioDAO();
		Connection connection =null;
		try {
			connection = this.dataSource.getConnection();
			//connection = ConnectionManager.getConnection();
			if (connection == null) System.out.println("Conexi�n es: null");
			if (connection != null) System.out.println("Conexi�n es: not null "+ connection);
			if (userDAO.exist(connection, usuarioVO.getNombreUsuario())) {
				System.out.println("Ya existe un usuario en el sistema con esos par�metros");
				throw new NotLegalAccountException();
			} else{
					userDAO.create(connection, usuarioVO);
			}
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

	/** Devuelve los datos de un usuario en la BBDD identificado por un Nombre Usuario**/
	public usuarioVO encontrarUsuario(String nombreUsuario) throws InternalErrorException, NotLegalAccountException{
		usuarioDAO userDAO = new usuarioDAO();
		Connection connection =null;
		usuarioVO result = null;
		try {
			connection = this.dataSource.getConnection();
			if (userDAO.exist(connection, nombreUsuario)) {
				result = userDAO.find(connection, nombreUsuario);
			} else {
				System.out.println("No existe usuario del sistema con ese NombreUsuario");
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

	/** Valida que la contrasena password coincide con el usuario nombreUsuario **/
	public boolean validarUsuario(String nombreUsuario, String password) throws InternalErrorException, NotLegalAccountException{
		usuarioDAO userDAO = new usuarioDAO();
		Connection connection = null;
		usuarioVO user = null;
		boolean validar;
		try {
			connection = this.dataSource.getConnection();
			if (userDAO.exist(connection, nombreUsuario)) {
				user = userDAO.find(connection, nombreUsuario);
				if((user.getPassword()).equals(password)){
					validar = true;
				} else{
					validar = false;
				}
				return validar;
			} else {
				System.out.println("No existe usuario del sistema con ese NombreUsuario");
				throw new NotLegalAccountException();				
			}
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
