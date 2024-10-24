SELECT
    t.id AS time_id,
    t.nome AS time_nome,
    GROUP_CONCAT(j.nome ORDER BY j.numero ASC SEPARATOR ', ') AS jogadores
FROM
    campeonato_de_futebol.times t
LEFT JOIN
    campeonato_de_futebol.jogadores j ON t.id = j.time_id
GROUP BY
    t.id, t.nome
ORDER BY
    t.nome;
