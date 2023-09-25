let minhaLista: number[] = [1,2,3];

function pegaPrimeiroElemento<T>(lista: T[]): T{
    return lista[0];
}

pegaPrimeiroElemento(minhaLista);

pegaPrimeiroElemento<string>(['a', 'b']);