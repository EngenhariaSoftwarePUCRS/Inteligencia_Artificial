import java.util.ArrayList;

public class AlgoritmoAStar {
    private ArrayList<Nodo> conexoes;
    private ArrayList<Nodo> visitados;
    private ArrayList<Nodo> desconhecidos;
    private int matrizDistancias[][];
    private int matrizCoordenadas[][];
    private Cidades arqControl;

    private int quantNos;
    private Nodo noInicial;
    private Nodo noFinal;
    private Nodo noCorrente;
    
    public AlgoritmoAStar() {
        conexoes = new ArrayList<Nodo>();
        visitados = new ArrayList<Nodo>();
        desconhecidos = new ArrayList<Nodo>();
        arqControl = new Cidades();
    }
    
    public void carregaDados(String arquivo, int idNoInicial, int idNoFinal) {
        arqControl.readArquivo(arquivo);
        quantNos = arqControl.getQuantidade();
        matrizDistancias = arqControl.getDistancias();
        matrizCoordenadas = arqControl.getCoordenadas();
        
        for(int i = 0; i < quantNos; i++) {
            desconhecidos.add(new Nodo(i));
        }
        
        noInicial = containsNo(desconhecidos, idNoInicial);
        noFinal = containsNo(desconhecidos, idNoFinal);
        desconhecidos.remove(idNoInicial);
        noCorrente = noInicial;
    }
    
    public String encontraCaminho() {
        Nodo aux = null;
        String caminho = "";
        int distancia = 0;

        while (noFinal != noCorrente) {
            visitados.add(noCorrente);
            conexoes.remove(noCorrente);
            insereconexoes(noCorrente.getId());
            noCorrente = proximoNo();
            if (noCorrente == null) {
                return "Nao Existe caminho.";
            }
        }
        
        aux = noFinal;
        distancia = noFinal.getPeso();
        while (aux != null) {
            caminho = (aux.getId() + 1) + " " + caminho;
            aux = aux.getAnt();
        }

        return "Caminho: " + caminho + "  Distancia: " + distancia;
    }
    

    private void insereconexoes(int id){
        Nodo aux;
        
        for (int i = 0; i < quantNos; i++) {
            if (matrizDistancias[id][i] > 0) {
                aux = containsNo(desconhecidos, i);
                int novoPeso = matrizDistancias[id][i] + noCorrente.getPeso(); 
                if (aux != null) {
                    if (!visitados.contains(aux)) {
                        aux.setPeso(novoPeso);
                        aux.setAnt(noCorrente); 
                        conexoes.add(aux);
                        desconhecidos.remove(aux);
                    }
                } else {
                    aux = containsNo(conexoes, i);
                    if (aux != null) {
                        if (aux.getPeso() > novoPeso) {
                            aux.setPeso(novoPeso);
                            aux.setAnt(noCorrente);
                        }
                    }
                }
            }
        }
    }
    

    private Nodo proximoNo(){
        Nodo prox;
        int menor;
        int aux = 0;
        if (conexoes.isEmpty()) {
            return null;
        }
        
        prox = conexoes.get(0);
        int[] coord1 = matrizCoordenadas[prox.getId()]; 
        int[] coord2 = matrizCoordenadas[noFinal.getId()]; 
        menor = prox.getPeso() + heuristica(coord1[0], coord1[1], coord2[0], coord2[1]);
        
        for (Nodo cur : conexoes) {
            coord1 = matrizCoordenadas[cur.getId()]; 
            aux = heuristica(coord1[0], coord1[1], coord2[0], coord2[1]);
            //se atual melhor que menor
            if ((cur.getPeso() + aux) < menor) {
                menor = cur.getPeso() + aux;
                prox = cur;
            }
        }
        return prox;
    }
    
    private int heuristica(
        int latitudeCidade1, int longitudeCidade1,
        int latitudeCidade2, int longitudeCidade2
    ) {
        return Math.abs(latitudeCidade1 - latitudeCidade2) + Math.abs(longitudeCidade1 - longitudeCidade2);
    }

    private Nodo containsNo(ArrayList<Nodo> list, int id){
        for (Nodo cur : list) {
            if (cur.getId() == id) {
                return cur;
            }
        }
        return null;
    }
    
    public static void main(String args[]) {
        AlgoritmoAStar algoritmo = new AlgoritmoAStar();
		algoritmo.carregaDados(args[0], (Integer.parseInt(args[1]) - 1), (Integer.parseInt(args[2]) - 1));
		System.out.println(algoritmo.encontraCaminho());
	}
}
