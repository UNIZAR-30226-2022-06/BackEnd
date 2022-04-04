package backend.clasesDB;

import com.google.gson.annotations.SerializedName;

public class Libro {

    @SerializedName("id")
    private Integer id;
    @SerializedName("nombre")
    private String nombre;
    @SerializedName("formato")
    private String formato;
    @SerializedName("linkDocumento")
    private String linkDocumento;
    @SerializedName("ISBN")
    private Integer ISBN;
    @SerializedName("descripcion")
    private String descripcion;
    @SerializedName("autor")
    private String autor;

    public Libro(Integer id, String nombre, String formato, String linkDocumento, Integer ISBN, String descripcion, String autor) {
        this.id = id;
        this.nombre = nombre;
        this.formato = formato;
        this.linkDocumento = linkDocumento;
        this.ISBN = ISBN;
        this.descripcion = descripcion;
        this.autor = autor;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getFormato() {
        return formato;
    }

    public void setFormato(String formato) {
        this.formato = formato;
    }

    public String getLinkDocumento() {
        return linkDocumento;
    }

    public void setLinkDocumento(String linkDocumento) {
        this.linkDocumento = linkDocumento;
    }

    public Integer getISBN() {
        return ISBN;
    }

    public void setISBN(Integer ISBN) {
        this.ISBN = ISBN;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }
}
