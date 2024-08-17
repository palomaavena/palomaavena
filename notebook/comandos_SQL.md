# Glossário SQL - Tradução e Funcionalidade

<br>

| Palavra SQL | Tradução | Função | Exemplo | Tradução do Exemplo |
| --- | --- | --- | --- | --- |
| SELECT | Selecionar | Seleciona dados de uma tabela. | SELECT * FROM livros; | Selecione todos os dados da tabela "livros". |
| FROM | De | Especifica a tabela de onde os dados serão selecionados. | SELECT * FROM livros; | Selecione os dados da tabela "livros". |
| WHERE | Onde | Filtra os registros com base em uma condição. | SELECT * FROM livros WHERE genero = 'Ficção'; | Selecione os livros onde o gênero seja "Ficção". |
| AND | E | Combina múltiplas condições com "E" lógico. | SELECT * FROM livros WHERE genero = 'Ficção' AND ano_publicacao > 2000; | Selecione os livros onde o gênero seja "Ficção" e o ano de publicação seja maior que 2000. |
| OR | Ou | Combina múltiplas condições com "OU" lógico. | SELECT * FROM livros WHERE genero = 'Ficção' OR genero = 'Romance'; | Selecione os livros onde o gênero seja "Ficção" ou "Romance". |
| LIKE | Semelhante a | Faz comparações de padrões usando caracteres curinga (%, _). | SELECT * FROM livros WHERE titulo LIKE '%Harry Potter%'; | Selecione os livros cujo título contenha a palavra "Harry Potter". |
| NOT | Não | Nega uma condição. | SELECT * FROM livros WHERE ano_publicacao NOT BETWEEN 2000 AND 2010; | Selecione os livros que não foram publicados entre 2000 e 2010. |
| IN | Dentro de | Verifica se um valor está dentro de uma lista. | SELECT * FROM livros WHERE genero IN ('Ficção', 'Fantasia'); | Selecione os livros cujo gênero seja "Ficção" ou "Fantasia". |
| BETWEEN | Entre | Filtra valores dentro de um intervalo. | SELECT * FROM livros WHERE ano_publicacao BETWEEN 1990 AND 2000; | Selecione os livros publicados entre 1990 e 2000. |
| ORDER BY | Ordenar por | Ordena os resultados em ordem crescente ou decrescente. | SELECT * FROM livros ORDER BY ano_publicacao DESC; | Selecione os livros ordenados pelo ano de publicação em ordem decrescente. |
| ASC | Ascendente | Ordena em ordem crescente (padrão). | SELECT * FROM livros ORDER BY titulo ASC; | Selecione os livros ordenados pelo título em ordem crescente. |
| DESC | Decrescente | Ordena em ordem decrescente. | SELECT * FROM livros ORDER BY ano_publicacao DESC; | Selecione os livros ordenados pelo ano de publicação em ordem decrescente. |
| LIMIT | Limitar | Limita o número de registros retornados. | SELECT * FROM livros LIMIT 5; | Selecione os 5 primeiros livros da tabela. |
| GROUP BY | Agrupar por | Agrupa linhas com valores iguais em uma coluna. | SELECT genero, COUNT(*) AS num_livros FROM livros GROUP BY genero; | Agrupe os livros por gênero e conte o número de livros em cada gênero. |
| COUNT(*) | Contar | Conta o número de registros em um grupo. | SELECT COUNT(*) FROM livros; | Conte o número total de livros na tabela. |
| SUM() | Somar | Soma os valores de uma coluna. | SELECT SUM(preco) FROM livros; | Some o preço de todos os livros da tabela. |
| AVG() | Média | Calcula a média dos valores de uma coluna. | SELECT AVG(preco) FROM livros; | Calcule a média do preço dos livros na tabela. |
| MIN() | Mínimo | Encontra o valor mínimo de uma coluna. | SELECT MIN(ano_publicacao) FROM livros; | Encontre o ano de publicação mais antigo dos livros. |
| MAX() | Máximo | Encontra o valor máximo de uma coluna. | SELECT MAX(ano_publicacao) FROM livros; | Encontre o ano de publicação mais recente dos livros. |
| DISTINCT | Distintos | Retorna apenas valores únicos de uma coluna. | SELECT DISTINCT genero FROM livros; | Selecione apenas os gêneros distintos (sem repetições) da tabela. |
| AS | Como | Renomeia uma coluna no resultado da consulta. | SELECT id AS livro_id, titulo AS nome_livro FROM livros; | Renomeie as colunas "id" para "livro_id" e "titulo" para "nome_livro". |
| CREATE TABLE | Criar Tabela | Cria uma nova tabela no banco de dados. | CREATE TABLE livros (id INTEGER PRIMARY KEY, titulo TEXT, ...); | Crie uma nova tabela chamada "livros" com as colunas especificadas. |
| INTEGER | Inteiro | Define uma coluna do tipo inteiro. | id INTEGER PRIMARY KEY, | Defina a coluna "id" como um número inteiro. |
| TEXT | Texto | Define uma coluna do tipo texto. | titulo TEXT, | Defina a coluna "titulo" como texto. |
| REAL | Real | Define uma coluna do tipo número de ponto flutuante. | preco REAL | Defina a coluna "preco" como um número real. |
| PRIMARY KEY | Chave Primária | Define uma coluna como chave primária, garantindo unicidade de registros. | id INTEGER PRIMARY KEY, | Defina a coluna "id" como a chave primária, garantindo que cada livro tenha um ID único. |
| FOREIGN KEY | Chave Estrangeira | Cria um relacionamento com outra tabela. | FOREIGN KEY (livro_id) REFERENCES livros(id) | Defina "livro_id" como chave estrangeira, referenciando a tabela "livros". |
| REFERENCES | Referencia | Especifica a tabela e a coluna referenciada pela chave estrangeira. | FOREIGN KEY (livro_id) REFERENCES livros(id) | Faça com que a chave estrangeira "livro_id" se refira à coluna "id" da tabela "livros". |
| INSERT INTO | Inserir em | Insere novos dados em uma tabela. | INSERT INTO livros (titulo, genero, ...) VALUES ('Dom Quixote', 'Ficção', ...); | Insira um novo livro com os dados "Dom Quixote", "Ficção", etc. na tabela "livros". |
| VALUES | Valores | Especifica os valores para cada coluna dos novos registros. | INSERT INTO livros (titulo, genero, ...) VALUES ('Dom Quixote', 'Ficção', ...); | Especifique os valores para "titulo", "genero", etc. |
| UPDATE | Atualizar | Altera dados em registros existentes. | UPDATE livros SET preco = 30.00 WHERE id = 1; | Atualize o preço do livro com ID 1 para 30.00. |
| SET | Definir | Define novos valores para as colunas a serem atualizadas. | UPDATE livros SET preco = 30.00 WHERE id = 1; | Defina o novo preço do livro como 30.00. |
| DELETE | Excluir | Remove registros de uma tabela. | DELETE FROM livros WHERE id = 1; | Exclua o livro com ID 1 da tabela. |
| TRUNCATE TABLE | Truncar Tabela | Remove todos os dados de uma tabela, mantendo a estrutura. | TRUNCATE TABLE livros; | Exclua todos os dados da tabela "livros", mas mantenha a estrutura da tabela. |
| ALTER TABLE | Alterar Tabela | Modifica a estrutura de uma tabela. | ALTER TABLE livros ADD COLUMN idioma TEXT; | Adicione uma nova coluna chamada "idioma" do tipo texto à tabela "livros". |
| RENAME TABLE | Renomear Tabela | Renomeia uma tabela. | RENAME TABLE livros TO obras_literarias; | Renomeie a tabela "livros" para "obras_literarias". |
| BEGIN TRANSACTION | Iniciar Transação | Inicia um bloco de comandos como uma única transação. | BEGIN TRANSACTION; | Inicie uma transação. |
| COMMIT | Confirmar | Confirma as alterações de uma transação. | COMMIT; | Confirme as alterações da transação atual. |
| ROLLBACK | Reverter | Reverte as alterações de uma transação. | ROLLBACK; | Reverte as alterações da transação atual. |
| SAVEPOINT | Ponto de Salvamento | Cria um ponto de salvamento dentro de uma transação. | SAVEPOINT meu_ponto; | Crie um ponto de salvamento chamado "meu_ponto" dentro da transação atual. |
| GRANT | Conceder | Concede permissões de acesso a usuários. | GRANT SELECT, INSERT ON livros TO usuario_admin; | Conceda ao usuário "usuario_admin" permissões de seleção e inserção na tabela "livros". |
| REVOKE | Revogar | Revoca permissões de acesso de usuários. | REVOKE INSERT ON livros FROM usuario_admin; | Revogue a permissão de inserção na tabela "livros" do usuário "usuario_admin". |
| JOIN | Juntar | Combina dados de duas ou mais tabelas. | SELECT * FROM livros JOIN autores ON livros.autor_id = autores.id; | Junte a tabela "livros" com a tabela "autores" usando a coluna "autor_id" como chave. |
| ON | Em | Especifica a condição de relacionamento para juntar tabelas. | SELECT * FROM livros JOIN autores ON livros.autor_id = autores.id; | Junte as tabelas usando a condição "livros.autor_id = http://autores.id/". |
| EXISTS | Existe | Verifica se uma subconsulta retorna algum resultado. | SELECT * FROM livros WHERE EXISTS (SELECT 1 FROM autores WHERE id = livros.autor_id); | Selecione os livros que existem na tabela "autores". |
| UNION | União | Combina resultados de duas consultas, removendo duplicatas. | SELECT titulo FROM livros WHERE genero = 'Ficção' UNION SELECT titulo FROM livros WHERE genero = 'Romance'; | Combine os títulos de livros de ficção com os títulos de livros de romance, removendo duplicatas. |
| UNION ALL | União Tudo | Combina resultados de duas consultas, incluindo duplicatas. | SELECT titulo FROM livros WHERE genero = 'Ficção' UNION ALL SELECT titulo FROM livros WHERE genero = 'Romance'; | Combine os títulos de livros de ficção com os títulos de livros de romance, incluindo duplicatas. |
| INTERSECT | Interseção | Retorna apenas as linhas que aparecem em ambos os conjuntos de resultados. | SELECT titulo FROM livros WHERE ano_publicacao > 2000 INTERSECT SELECT titulo FROM livros WHERE genero = 'Ficção'; | Selecione os títulos de livros publicados após 2000 que também sejam do gênero "Ficção". |
| EXCEPT | Exceto | Retorna apenas as linhas que aparecem no primeiro conjunto de resultados, mas não no segundo. | SELECT titulo FROM livros WHERE genero = 'Ficção' EXCEPT SELECT titulo FROM livros WHERE ano_publicacao > 2000; | Selecione os títulos de livros de ficção que não foram publicados após 2000. |

Fonte: Camila Ribeiro
