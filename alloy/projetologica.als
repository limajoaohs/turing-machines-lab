module ProjetoLogica 

sig Usuario {
}

sig Carona {
	motorista : one Usuario,
	passageiros : some Usuario,
	origem: one Regiao,
	destino: one Regiao
}

sig Regiao {
}

sig Cidade {
}

sig Aulas {
}

// ufcg

fact {
	some Carona
	all c: Carona | #(c.passageiros) <= 4
	all c1, c2 : Carona| !(c1=c2) implies no(c1.motorista & c2.motorista)
	all c1, c2 : Carona| !(c1=c2) implies no(c1.passageiros & c2.passageiros)
	all c1, c2 : Carona| !(c1=c2) implies no(c1.motorista & c2.passageiros)
	all c: Carona | c.motorista !in c.passageiros
	all c: Carona | !(c.origem= c.destino)
}

run {
}for 5