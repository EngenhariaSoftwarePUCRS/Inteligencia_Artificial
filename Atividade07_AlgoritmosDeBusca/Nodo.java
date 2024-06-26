public class Nodo{

	private int peso;
	private int idNo;
	private Nodo ant;
	
	public Nodo(int id){
		this.idNo = id;
		peso= 0;
		ant = null;
	}
	
	public int getId(){
		return idNo;
	}
	
	public void setPeso(int peso){
		this.peso = peso;
	}
	
	public void setAnt(Nodo n){
		ant = n;
	}
	
	public Nodo getAnt(){
		return ant;
	}
	
	public int getPeso(){
		return peso;
	}
}