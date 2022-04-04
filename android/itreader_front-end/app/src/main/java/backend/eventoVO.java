package backend;

import java.sql.Date;

public class eventoVO {
	private String nombre;
	private String descripcion;
	private String nomUsuario;
	private Date fecha;
    private String tipoAcceso;
    private int aforo;
    private String categoria;
	
	/**
	 * Constructor
	 */
	public eventoVO(String nombre, String descripcion, String nomUsuario,
			Date fecha, String tipoAcceso, int aforo, String categoria) {
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.nomUsuario = nomUsuario;
		this.fecha = fecha;
		this.tipoAcceso = tipoAcceso;
		this.aforo = aforo;
		this.categoria = categoria;
	}

	/* nombre */
	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	/* descripcion */
	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	/* nomUsuario */
	public String getNomUsuario() {
		return nomUsuario;
	}

	public void setNomUsuario(String nomUsuario) {
		this.nomUsuario = nomUsuario;
	}
	/* fecha */
    public Date getFecha() {
		return fecha;
	}

	public void setFecha(Date fecha) {
		this.fecha = fecha;
	}
	/* tipoAcceso */
    public String getTipoAcceso() {
		return tipoAcceso;
	}

	public void setTipoAcceso(String tipoAcceso) {
		this.tipoAcceso = tipoAcceso;
	}
	/* aforo */
    public Integer getAforo() {
		return aforo;
	}

	public void setAforo(Integer aforo) {
		this.aforo = aforo;
	}
	/* categoria */
    public String getCategoria() {
		return categoria;
	}

	public void setCategoria(String categoria) {
		this.categoria = categoria;
	}
	
}
