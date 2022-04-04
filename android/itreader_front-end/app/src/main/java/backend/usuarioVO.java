package backend;

import com.google.gson.annotations.SerializedName;

public class usuarioVO {
	/*private String nombre;
	private String nombreUsuario;
	private String password;
	private String email;
    private int edad;
    private int telefono;
    private int valoracion;*/
	@SerializedName("pk")
	int pk;

	@SerializedName("nombre")
	String nombre;

	@SerializedName("nomUsuario")
	String nombreUsuario;

	@SerializedName("password")
	String password;

	@SerializedName("email")
	String email;

	@SerializedName("edad")
	int edad;

	@SerializedName("telefono")
	int telefono;

	@SerializedName("valoracion")
	int valoracion;
	
	/**
	 * Constructor
	 */
	public usuarioVO(String nombre, String nombreUsuario, String password,
			String email, int edad, int telefono, int valoracion) {
		this.nombre = nombre;
		this.nombreUsuario = nombreUsuario;
		this.password = password;
		this.email = email;
		this.edad = edad;
		this.telefono = telefono;
		this.valoracion = valoracion;
	}

	/* nombre */
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	/* nombreUsuario */
	public String getNombreUsuario() {
		return nombreUsuario;
	}

	public void setNombreUsuario(String nombreUsuario) {
		this.nombreUsuario = nombreUsuario;
	}
	/* password */
	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}
	/* email */
    public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}
	/* edad */
    public Integer getEdad() {
		return edad;
	}

	public void setEdad(Integer edad) {
		this.edad = edad;
	}
	/* telefono */
    public Integer getTelefono() {
		return telefono;
	}

	public void setTelefono(Integer telefono) {
		this.telefono = telefono;
	}
	/* valoracion */
    public Integer getValoracion() {
		return valoracion;
	}

	public void setValoracion(Integer valoracion) {
		this.valoracion = valoracion;
	}
	
}
