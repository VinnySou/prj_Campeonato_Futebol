SELECT
    t.id AS time_id,
    t.nome AS time_nome,
    COUNT(CASE WHEN p.time_casa_id = t.id AND p.gols_time_casa > p.gols_time_visitante THEN 1 END) AS vitorias,
    COUNT(CASE WHEN p.time_visitante_id = t.id AND p.gols_time_visitante > p.gols_time_casa THEN 1 END) AS vitorias_visitante,
    COUNT(CASE WHEN p.time_casa_id = t.id AND p.gols_time_casa = p.gols_time_visitante THEN 1 END) AS empates,
    COUNT(CASE WHEN p.time_visitante_id = t.id AND p.gols_time_visitante = p.gols_time_casa THEN 1 END) AS empates_visitante,
    COUNT(CASE WHEN p.time_casa_id = t.id AND p.gols_time_casa < p.gols_time_visitante THEN 1 END) AS derrotas,
    COUNT(CASE WHEN p.time_visitante_id = t.id AND p.gols_time_visitante < p.gols_time_casa THEN 1 END) AS derrotas_visitante,
    SUM(CASE WHEN p.time_casa_id = t.id THEN p.gols_time_casa ELSE 0 END) +
    SUM(CASE WHEN p.time_visitante_id = t.id THEN p.gols_time_visitante ELSE 0 END) AS gols_marcados,
    SUM(CASE WHEN p.time_casa_id = t.id THEN p.gols_time_visitante ELSE 0 END) +
    SUM(CASE WHEN p.time_visitante_id = t.id THEN p.gols_time_casa ELSE 0 END) AS gols_sofridos,
    (COUNT(CASE WHEN p.time_casa_id = t.id AND p.gols_time_casa > p.gols_time_visitante THEN 1 END) +
     COUNT(CASE WHEN p.time_visitante_id = t.id AND p.gols_time_visitante > p.gols_time_casa THEN 1 END)) * 3 +
    (COUNT(CASE WHEN p.time_casa_id = t.id AND p.gols_time_casa = p.gols_time_visitante THEN 1 END) +
     COUNT(CASE WHEN p.time_visitante_id = t.id AND p.gols_time_visitante = p.gols_time_casa THEN 1 END)) AS pontos
FROM
    campeonato_de_futebol.times t
LEFT JOIN
    campeonato_de_futebol.partidas p ON t.id IN (p.time_casa_id, p.time_visitante_id)
GROUP BY
    t.id, t.nome
ORDER BY
    pontos DESC, gols_marcados DESC, (gols_marcados - gols_sofridos) DESC;
