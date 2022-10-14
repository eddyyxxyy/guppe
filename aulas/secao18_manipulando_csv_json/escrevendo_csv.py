"""
Escrevendo em arquivos CSV

reader() -> Leitor
writer() -> Escritor

writerow() -> Escreve uma linha


# writer() gera um objeto para que possamos escrever
# em um arquivo CSV.
# writerow() para escrever uma linha. Este método
# recebe uma lista.

from csv import writer

with open('arquivos/movies.csv', 'w', newline='') as file:
    writer_csv = writer(file)
    movie = None
    writer_csv.writerow(['Title', 'Genre', 'Duration'])
    while movie != 'end_op':
        movie = input('Title: ')
        if movie != 'end_op':
            genre = input('Genre: ')
            duration = input('Duration (minutes): ')
            writer_csv.writerow([movie, genre, duration])
"""

# DictWriter

# OBS: As chaves do dict devem ser as mesmas que as utilizadas
# no cabeçalho

from csv import DictWriter

with open('arquivos/movies2.csv', 'w', newline='') as file:
    file_header = ['Title', 'Genre', 'Duration']
    file_dictwriter = DictWriter(file, fieldnames=file_header)
    file_dictwriter.writeheader()
    movie = None
    while movie != 'end_op':
        movie = input('Title: ')
        if movie != 'end_op':
            genre = input('Genre: ')
            duration = input('Duration: ')
            file_dictwriter.writerow(
                {'Title': movie, 'Genre': genre, 'Duration': duration}
            )
