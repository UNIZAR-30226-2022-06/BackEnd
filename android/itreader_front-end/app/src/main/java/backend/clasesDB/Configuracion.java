package backend.clasesDB;

import com.google.gson.annotations.SerializedName;

public class Configuracion {

    @SerializedName("id")
    private Integer id;
    @SerializedName("letraSize")
    private String letraSize;
    @SerializedName("letraStyle")
    private String letraStyle;
    @SerializedName("colorFondo")
    private String colorFondo;

    public Configuracion(Integer id, String letraSize, String letraStyle, String colorFondo) {
        this.id = id;
        this.letraSize = letraSize;
        this.letraStyle = letraStyle;
        this.colorFondo = colorFondo;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getLetraSize() {
        return letraSize;
    }

    public void setLetraSize(String letraSize) {
        this.letraSize = letraSize;
    }

    public String getLetraStyle() {
        return letraStyle;
    }

    public void setLetraStyle(String letraStyle) {
        this.letraStyle = letraStyle;
    }

    public String getColorFondo() {
        return colorFondo;
    }

    public void setColorFondo(String colorFondo) {
        this.colorFondo = colorFondo;
    }
}
