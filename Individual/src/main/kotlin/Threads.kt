import com.github.britooo.looca.api.core.Looca

fun main() {
    val looca = Looca()

    var Processador = looca.processador

    var ID = Processador.id
    var Nome = Processador.nome
    var Fabricante = Processador.fabricante
    var Frequencia = Processador.frequencia
    var Identificador = Processador.identificador
    var Microarquitetura = Processador.microarquitetura
    var CpusFisicas = Processador.numeroCpusFisicas
    var CpusLogicas = Processador.numeroCpusLogicas
    var PacotesFisicos = Processador.numeroPacotesFisicos
    var Uso = Processador.uso


    println("""
            ID: $ID 
            Nome: $Nome 
            Fabricante: $Fabricante 
            Frequencia: $Frequencia 
            Identificador: $Identificador 
            Microarquitetura: $Microarquitetura 
            CpusFisicas: $CpusFisicas 
            CpusLogicas: $CpusLogicas 
            PacotesFisicos: $PacotesFisicos 
            Uso: $Uso 
        """.trimIndent())



}