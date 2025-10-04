def inverti_parole(frase: str) -> str:
    """
    Inverte l'ordine delle parole in una frase.

    Esempio:
    >>> inverti_parole("ciao come stai")
    'stai come ciao'
    """
    # Suddivide la frase in parole usando split()
    parole = frase.split()
    # Inverte la lista con slicing
    parole_invertite = parole[::-1]
    # Ricompone la frase con join() per efficienza
    frase_invertita = " ".join(parole_invertite)
    return frase_invertita


# Esempio d'uso
frase = "oggi è una bella giornata"
print(f"Frase originale: {frase}")
print(f"Frase invertita: {inverti_parole(frase)}")
