package backend.clasesDB;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class Documento {
    @SerializedName("id")
    private Integer id;
    @SerializedName("nombre")
    private String nombre;
    @SerializedName("formato")
    private String formato;
    @SerializedName("linkDocumento")
    private String linkDocumento;

    public Documento(Integer id, String nombre, String formato, String linkDocumento) {
        this.id = id;
        this.nombre = nombre;
        this.formato = formato;
        this.linkDocumento = linkDocumento;
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
}
