package backend;

public class InternalErrorException extends Exception{
	
	private static final long serialVersionUID = 1L;
	private Exception exception = null;
		
	public InternalErrorException (Exception e) {
		this.exception = e;
	}
		
	public Exception getException() {
		return this.exception;
	}
}
