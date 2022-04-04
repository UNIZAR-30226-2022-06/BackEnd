package backend;

public class NotLegalAccountException extends Exception{
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private String mess = "Somebody has created an account with this login. So another one cannot be created. Besides, remember, you must be at least 18 in order to create an account";
	
	public NotLegalAccountException () {
		
	}
	public String toString() {
		return mess;
	}

}
