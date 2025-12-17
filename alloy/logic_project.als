module ProjetoLogica 

// Representa o usúario cadastrado no sitema de caronas, que pode receber e oferecer caronas, 
//e que necesssita estar matriculado na UFCG, e ser frequente nas aulas
sig Usuario {
	aluno: one Aluno
}

//Representa uma Carona do sistema e seus devidos atributos.
sig Carona {
	motorista : one Usuario,
	passageiros : some Usuario,
	origem: one Regiao,
	destino: one Regiao,
	horario: one Horario
}

// Representa uma região, que é uma espécie de bairro da cidade
sig Regiao {
	moradores : some Usuario
}

// Representa uma cidade, pode ser tanto Campina Grande, quanto outras
sig Cidade {
	regioes: some Regiao
}

//Representa uma Aula(Cadeira) em que o aluno está matriculado
sig Aula {
	frequentes: set Aluno
}

//Representa um horário
sig Horario {
}

// Representa um aluno
sig Aluno {
}

// representa a "entidade" UFCG, que se refere tanto à localidade, quanto aos alunos e se estão matriculados, ou não
one sig ufcg extends Regiao {
	alunos: some Aluno,
	aulas: some Aula
}

// ufcg

fact {
	some Carona
	//Garante que o máximo de passageiros na Carona é 4
	all c: Carona | #(c.passageiros) <= 4
	//Garante que o mesmo motorista não pode oferecer duas caronas distintas no mesmo horário
	all c1, c2 : Carona| (c1.horario=c2.horario) && !(c1=c2) implies no(c1.motorista & c2.motorista)
	//Garante que o mesmo passageiro não possa pegar  duas caronas distintas no mesmo horário
	all c1, c2 : Carona| (c1.horario=c2.horario) && !(c1=c2) implies no(c1.passageiros & c2.passageiros)
	//Garante que o motorista de uma Carona, em um determinado horário, não seja o passageiro de
	//de uma outra Carona no mesmo horário
	all c1, c2 : Carona| (c1.horario=c2.horario) && !(c1=c2) implies no(c1.motorista & c2.passageiros)
	// Garante que o motorista não esteja no conjunto de passageiros simultaneamente
	all c: Carona | c.motorista !in c.passageiros
	//Garante que a origem e o destino não sejam iguais 
	all c: Carona | !(c.origem= c.destino)
	// Pelo menos a origem, ou o destino precisam ser a UFCG
	all c: Carona | (c.origem = ufcg) or (c.destino = ufcg)
	//Toda carona precisa ter como motorista um aluno
	all c: Carona | !(c.motorista.aluno = none)
	//Toda carona precisa ter como passageiros alunos
	all c: Carona | !(c.passageiros.aluno = none)
	//Cada aluno deve ser, necessariamente, matriculado na UFCG e frequente nas aulas
	all u: ufcg, a: Aluno, U: Usuario | (!(a in u.alunos) or !(a in u.aulas.frequentes)) implies !(U.aluno = a) 
	//Se dois usuários são diferentes, os alunos associados a eles são diferentes também
	all u1, u2: Usuario | !(u1 = u2)  implies !(u1.aluno = u2.aluno)
}

// ----------------------------------------------------------------
// SEÇÃO DE VERIFICAÇÕES (ASSERTS)
// ----------------------------------------------------------------

// Assert 1: Verifica se o aluno associado ao motorista não está também na lista de alunos dos passageiros.
// Espera-se que seja válido (sem contraexemplos).
assert AlunoMotoristaNaoEhPassageiro {
    all c: Carona | c.motorista.aluno !in c.passageiros.aluno
}
check AlunoMotoristaNaoEhPassageiro for 4

// Assert 2: Verifica se toda carona que sai da UFCG tem pelo menos 2 passageiros.
// Espera-se que seja inválido (Alloy deve encontrar um contraexemplo).
assert CaronaSaindoDaUFCGTemMinimoDoisPassageiros {
    all c: Carona | c.origem = ufcg implies #(c.passageiros) >= 2
}
check CaronaSaindoDaUFCGTemMinimoDoisPassageiros for 4

// ----------------------------------------------------------------
// SEÇÃO DE CENÁRIO EXEMPLO (RUN)
// ----------------------------------------------------------------

// Predicado que descreve um cenário específico: uma carona lotada saindo de um bairro para a UFCG.
pred CenarioCaronaCheiaIndoParaUFCG {
    one c: Carona {
        // A carona está com a capacidade máxima de passageiros
        #(c.passageiros) = 4
        // O destino é a UFCG
        c.destino = ufcg
        // A origem não é a UFCG (logo, é um bairro)
        c.origem != ufcg
        // O motorista mora na região de origem da carona
        c.motorista in c.origem.moradores
    }
}
run CenarioCaronaCheiaIndoParaUFCG for 7