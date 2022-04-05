package backend.clasesDB;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Libro {

    @SerializedName("id")
    @Expose
    private Integer id;
    @SerializedName("nombre")
    @Expose
    private String nombre;
    @SerializedName("formato")
    @Expose
    private String formato;
    @SerializedName("linkDocumento")
    @Expose
    private String linkDocumento;
    @SerializedName("linkPortada")
    @Expose
    private String linkPortada;
    @SerializedName("ISBN")
    @Expose
    private String ISBN;
    @SerializedName("autor")
    @Expose
    private String autor;

    public Libro(String nombre, String formato, String linkDocumento, String linkPortada, String ISBN, String autor) {
        this.nombre = nombre;
        this.formato = formato;
        this.linkDocumento = linkDocumento;
        this.linkPortada = linkPortada;
        this.ISBN = ISBN;
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

    public String getLinkPortada() {
        return linkPortada;
    }

    public void setLinkPortada(String linkPortada) {
        this.linkPortada = linkPortada;
    }

    public String getISBN() {
        return ISBN;
    }

    public void setISBN(String ISBN) {
        this.ISBN = ISBN;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }
}
