package backend.clasesDB;

import com.google.gson.annotations.SerializedName;

public class Marca {

    @SerializedName("id")
    private Integer id;
    @SerializedName("nombre")
    private String nombre;
    @SerializedName("pagina")
    private String pagina;
    @SerializedName("offset")
    private String offset;
    @SerializedName("esUltimaLeida")
    private Boolean esUltimaLeida;
    @SerializedName("usuario")
    private Usuario usuario;
    @SerializedName("documento")
    private Documento documento;

    public Marca(Integer id, String nombre, String pagina, String offset, Boolean esUltimaLeida, Usuario usuario, Documento documento) {
        this.id = id;
        this.nombre = nombre;
        this.pagina = pagina;
        this.offset = offset;
        this.esUltimaLeida = esUltimaLeida;
        this.usuario = usuario;
        this.documento = documento;
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

    public String getPagina() {
        return pagina;
    }

    public void setPagina(String pagina) {
        this.pagina = pagina;
    }

    public String getOffset() {
        return offset;
    }

    public void setOffset(String offset) {
        this.offset = offset;
    }

    public Boolean getEsUltimaLeida() {
        return esUltimaLeida;
    }

    public void setEsUltimaLeida(Boolean esUltimaLeida) {
        this.esUltimaLeida = esUltimaLeida;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        this.usuario = usuario;
    }

    public Documento getDocumento() {
        return documento;
    }

    public void setDocumento(Documento documento) {
        this.documento = documento;
    }
}
